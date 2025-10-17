"""Simple memory store used by the daydreaming loop."""

from __future__ import annotations

import json
import random
import threading
import time
import uuid
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


@dataclass(slots=True)
class MemoryEntry:
    """A unit of knowledge stored in the system."""

    id: str
    content: str
    kind: str = "concept"
    created_at: float = field(default_factory=lambda: time.time())
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_json(self) -> dict[str, Any]:
        data = asdict(self)
        data["metadata"] = dict(self.metadata)
        return data

    @classmethod
    def from_json(cls, payload: dict[str, Any]) -> "MemoryEntry":
        return cls(
            id=payload["id"],
            content=payload["content"],
            kind=payload.get("kind", "concept"),
            created_at=payload.get("created_at", time.time()),
            metadata=dict(payload.get("metadata", {})),
        )


class MemoryStore:
    """Thread-safe store for concepts and ideas."""

    def __init__(self, *, persistence_path: str | Path | None = None) -> None:
        self._entries: list[MemoryEntry] = []
        self._lock = threading.RLock()
        self._path = Path(persistence_path) if persistence_path else None
        if self._path:
            self._load()

    # ------------------------------------------------------------------
    # Basic operations
    # ------------------------------------------------------------------
    def __len__(self) -> int:  # pragma: no cover - trivial
        return len(self._entries)

    def __iter__(self) -> Iterator[MemoryEntry]:  # pragma: no cover - trivial
        yield from list(self._entries)

    def add_entry(self, content: str, *, kind: str = "concept", metadata: dict[str, Any] | None = None) -> MemoryEntry:
        entry = MemoryEntry(id=str(uuid.uuid4()), content=content, kind=kind, metadata=metadata or {})
        with self._lock:
            self._entries.append(entry)
            self._persist()
        return entry

    def add_entries(self, entries: Iterable[MemoryEntry]) -> None:
        with self._lock:
            self._entries.extend(entries)
            self._persist()

    def get_recent(self, n: int) -> Sequence[MemoryEntry]:
        with self._lock:
            return list(sorted(self._entries, key=lambda e: e.created_at, reverse=True)[:n])

    def prune(self, max_items: int) -> None:
        with self._lock:
            if max_items < 0:
                raise ValueError("max_items must be non-negative")
            if len(self._entries) <= max_items:
                return
            self._entries.sort(key=lambda e: e.created_at, reverse=True)
            self._entries = self._entries[:max_items]
            self._persist()

    # ------------------------------------------------------------------
    # Sampling utilities
    # ------------------------------------------------------------------
    def sample_pairs(self, k: int) -> list[tuple[MemoryEntry, MemoryEntry]]:
        """Sample ``k`` concept pairs without replacement.

        Sampling favours diversity by shuffling and pairing adjacent items.
        The order of entries is randomized on every call.
        """

        if k < 1:
            raise ValueError("k must be >= 1")

        with self._lock:
            if len(self._entries) < 2:
                return []
            entries = list(self._entries)

        random.shuffle(entries)
        pairs: list[tuple[MemoryEntry, MemoryEntry]] = []
        idx = 0
        while idx + 1 < len(entries) and len(pairs) < k:
            left, right = entries[idx], entries[idx + 1]
            if left.id != right.id:
                pairs.append((left, right))
            idx += 2

        return pairs

    # ------------------------------------------------------------------
    # Persistence helpers
    # ------------------------------------------------------------------
    def _load(self) -> None:
        if not self._path or not self._path.exists():
            return
        try:
            raw = json.loads(self._path.read_text())
        except json.JSONDecodeError as exc:  # pragma: no cover - load errors are rare
            raise ValueError(f"Failed to parse memory file {self._path}: {exc}") from exc
        entries = [MemoryEntry.from_json(item) for item in raw]
        self._entries = entries

    def _persist(self) -> None:
        if not self._path:
            return
        payload = [entry.to_json() for entry in self._entries]
        tmp_path = self._path.with_suffix(".tmp")
        tmp_path.write_text(json.dumps(payload, indent=2, sort_keys=True))
        tmp_path.replace(self._path)


__all__ = ["MemoryEntry", "MemoryStore"]
