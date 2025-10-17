Welcome to the canvas of dreams

Despite impressive capabilities, large language models have yet to produce a genuine breakthrough. The puzzle is why.
A reason may be that they lack some fundamental aspects of human thought: they are frozen, unable to learn from experience, and they have no “default mode” for background processing, a source of spontaneous human insight.
To illustrate the issue, I describe such insights, and give an example concrete algorithm of a day-dreaming loop (DDL): a background process that continuously samples pairs of concepts from memory. A generator model explores non-obvious links between them, and a critic model filters the results for genuinely valuable ideas. These discoveries are fed back into the system’s memory, creating a compounding feedback loop where new ideas themselves become seeds for future combinations.
The cost of this process—a “daydreaming tax”—would be substantial, given the low hit rate for truly novel connections. This expense, however, may be the necessary price for innovation. It would also create a moat against model distillation, as valuable insights emerge from the combinations no one would know to ask for.
The strategic implication is counterintuitive: to make AI cheaper and faster for end users, we might first need to build systems that spend most of their compute on this “wasteful” background search. This suggests a future where expensive, daydreaming AIs are used primarily to generate proprietary training data for the next generation of efficient models, offering a path around the looming data wall.




…I feel I am nibbling on the edges of this world when I am capable of getting what Picasso means when he says to me—perfectly straight-facedly—later of the enormous new mechanical brains or calculating machines:
“But they are useless. They can only give you answers.”
William Fifield, “Pablo Picasso—A Composite Interview” (1964)


Dwarkesh Patel asks why no LLM has (seemingly) ever made a major breakthrough or unexpected insight, no matter how vast their knowledge or how high their benchmark scores. While those are, by definition, extremely rare, contemporary chatbot-style LLMs have now been used seriously by tens of millions of people since ChatGPT (November 2022), and it does seem like there ought to be at least some examples at this point. This is a genuine puzzle: when prompted with the right hints, these models can synthesize information in ways that feel tantalizingly close to true insight; the raw components of intelligence seem to be present; but… they don’t. What is missing?
It’s hard to say because there are so many differences between LLMs and human researchers.

Missing Faculties

Continual Learning
Frozen NNs are amnesiacs. One salient difference is that LLMs are ‘frozen’, and are not allowed to change; they don’t have to be, and could be trained on the fly (eg. by the long-standing technique of dynamic evaluation), but they aren’t.
So perhaps that’s a reason they struggle to move beyond their initial guesses or obvious answers, and come up with truly novel insights—in a very real sense, LLMs are unable to learn. They are truly amnesiac. And there are no cases anywhere in human history, as far as I am aware, of a human with anterograde amnesia producing major novelties.
That may be an adequate answer all on its own: they are trapped in their prior knowledge, and cannot move far beyond their known knowledge; but by definition, all that is either known or almost known, and cannot be impressively novel.


Continual Thinking
But another notable difference is that human researchers never stop thinking. We are doing our continual learning on not just observations, but on our own thoughts—even when asleep, a human is still computing and processing. (This helps account for the shocking metabolic demands of even a brain which is ‘doing nothing’—it’s actually still doing a lot! As difficult as it may feel to think hard, from a biological perspective, it’s trivial.)
Research on science & creativity emphasizes the benefit of time & sleep in creating effects like the incubation effect, and some researchers have famously had sudden insights from dreams. And we have all had the experience of a thought erupting into consciousness, whether it’s just an inane pun (“you can buy kohl at Kohl’s, LOL”), a clever retort hours too late, a frustrating word finally coming to mind, suddenly recalling anxious worries (“did I really turn off the stove?”) like intrusive thoughts, or, once in a lifetime, a brilliant idea. (Try meditating for the first time and writing down all the thoughts that pop up until they finally stop coming, and one may be amazed & frustrated!)
Often these eruptions have nothing at all to do with anything we have been thinking about, or have thought about in decades (“wait—back at that college party, when that girl looked at my hand—she was hitting on me, wasn’t she?”) Indeed, this essay is itself the product of such an eruption—“what is the LLM equivalent of a default mode network? Well, it could look something like Jones 2021, couldn’t it?”—and had nothing to do with what I had been writing about (the esthetics of video games).
Click to expandClick to expandBacklinks (1) for “Continual Thinking”:LLM Daydreaming (context):[backlink context]


Hypothesis: Day-Dreaming Loop
So… where & when & how does this thinking happen?
It is clearly not happening in the conscious mind. It is also involuntary: you have no idea some arcane random topic is bubbling up in your mind until it does, and then it is too late.
And it is a universal phenomenon: they can happen spontaneously on seemingly any topic you have learned about. It seems difficult to exhaust—after a lifetime, I still have the same rate, and few people report ever having no such thoughts (except perhaps after highly unusual experiences like psychedelics or meditative enlightenment).
It is also probably expensive, given the cost of the brain and the implication that nontrivial thought goes into each connection. It is hard to tell, but my guess is that almost all animals do not have ‘eureka!’ moments. We can further guess that it is probably parallelizable, because the connections are between such ‘distant’ pairs of concepts that it is hard to imagine that the brain has a very large prior on them being related and is only doing a handful of serial computations in between each ‘hit’; they are probably extremely unlikely to be related, hence, many of them are being done, hence, they are being done in parallel to fit into a human lifetime.
It is presumably only partially related to the experience replay done by the hippocampus during sleep, because that is for long-term memory while we have these thoughts about things in Working memory or short-term memory (eg. about things during the day, before any sleep); there may well be connections, but they are not the same thing. And it is likely related to the default mode network, which activates when we are not thinking anything explicitly, because that is strongly associated with daydreaming or ‘woolgathering’ or ‘zoning out’, which is when such thoughts are especially likely to erupt. (The default mode network is especially surprising because there is no reason to expect the human brain to have such a thing, rather than go quiescent, and indeed, it took a long time for neuroscientists to accept its existence. And there is little evidence for a default mode network outside primates and possibly some mammals like rats.)
It further appears to be ‘crowded out’ and probably not happening when doing ‘focused’ learning or thinking: in my personal observation, when I have been intensively doing something (whether reading research, writing, coding, or anything else novel & intellectually demanding), the thoughts stop happening… but if I take a break, they may suddenly surge, as if there was a dam holding them back or my brain is making up for lost time.
So where is it?

Day-Dreaming Loop
I don’t know.
But to illustrate what I think answers here look like, here is an example of an answer, which satisfies our criteria, and is loosely inspired by wake-sleep algorithms & default mode network, and is not obviously wrong.
Let’s call this Day-dreaming loop (DDL): The brain is doing combinatorial search over its store of facts & skills. This is useful for sample efficiency by replaying old memories to extract new knowledge from them, or to do implicit planning (eg. to patch up flaws in temporally-extended tasks, like a whole human lifetime). DDL does this in a simple way: it retrieves 2 random facts, ‘thinks about them’, and if the result is ‘interesting’, it is promoted to consciousness and possibly added to the store / trained on. (It is not obvious how important it is to do higher-order combinations of k > 2, because as long as useful combinations keep getting added, the higher-order combinations become implicitly encoded: as long as 1 of the possible 3 pairs gets stored as a new combination, then the other can be retrieved and combined afterwards. Higher-order combinations where all members are uninteresting in any lower-order combos may be too sparse to be worth caring about.) DDL happens in the background when the brain is otherwise unoccupied, for one’s entire lifetime. So an example like the Kohl’s example would have happened like ‘retrieve 2 loosely semantic-net-related concepts; think about just those two; is the result interesting? yes, because there’s a pun about an unexpected connection between the two. Promoted!’
We can elaborate on DDL in various ways, like training on both interesting and uninteresting results, labeled as such, and then try to sample ‘interesting’-prefixed; or try to come up with a more efficient way of doing sampling (sampling-without-replacement? reservoir sampling? importance sampling approaches? anti-spaced repetition?), or fiddling with the verification step (do they need to be passed to oracles for review before being saved, because this search process is dangerously self-adversarial?).
But that’s unnecessary, as DDL already satisfies all the criteria, and so worth discussing:
It is plausible from a RL perspective that such a bootstrap can work, because we are exploiting the generator-verifier gap, where it is easier to discriminate than to generate (eg. laughing at a pun is easier than making it). It is entirely unconscious. Since it is lightweight, it can happen in parallel, in independent modalities/tasks (eg. verbal replay can happen separate from episodic memory replay). And by the nature of recombination, it is difficult to ‘exhaust’ this process because every ‘hit’ which gets added to the store will add many new combinations—surprisingly, in a statistical toy model of economic innovation, economist Charles I. Jones 2021 shows that even though we pick the low-hanging fruit first, we can still see a constant stream of innovation (or even an explosion of innovation). It is, however, highly expensive, because almost all combinations are useless. And it is difficult to optimize this too much because by the nature of online learning and the passage of time, the brain will change, and even if a pair has been checked before and was uninteresting, that might change at any time, and so it can be useful to recheck.
Click to expandClick to expandBacklinks (1) for “Day-Dreaming Loop”:LLM Daydreaming (context):[backlink context]
LLM Analogy
Clearly, a LLM does nothing at all like this normally, nor does any LLM system do this. They are called with a specific prompt to do a task, and they do it. They do not simply sample random facts and speculatively roll out some inner-monologues about the facts to see if they can think of anything ‘interesting’.
But it wouldn’t be hard to do my proposed algorithm. For example, retrieval of random sets of datapoints from a vector database, then roll out a “brainstorm” prompt, then a judgment. Hypothetical prompts:
Click to expandClick to expand[SYSTEM]
You are a creative synthesizer. Your task is to find deep, non-obvious,
and potentially groundbreaking connections between the two following concepts.
Do not state the obvious. Generate a hypothesis, a novel analogy,
a potential research question, or a creative synthesis.
Be speculative but ground your reasoning.
 
Concept 1: {Chunk A}
Concept 2: {Chunk B}
 
Think step-by-step to explore potential connections:
 
#. Are these concepts analogous in some abstract way?
#. Could one concept be a metaphor for the other?
#. Do they represent a similar problem or solution in different domains?
#. Could they be combined to create a new idea or solve a problem?
#. What revealing contradiction or tension exists between them?
 
Synthesize your most interesting finding below.
[ASSISTANT]
 
...
 
[SYSTEM]
You are a discerning critic. Evaluate the following hypothesis
on a scale of 1--10 for each of the following criteria:
 
- **Novelty:** Is this idea surprising and non-obvious? (1=obvious, 10=paradigm-shifting)
- **Coherence:** Is the reasoning logical and well-formed? (1=nonsense, 10=rigorous)
- **Usefulness:** Could this idea lead to a testable hypothesis, a new product,
  or a solution to a problem? (1=useless, 10=highly applicable)
 
Hypothesis: {Synthesizer Output}
 
Provide your scores and a brief justification.
[ASSISTANT]




Obstacles and Open Questions
Cheap, good, fast: pick 2…Just expensive. We could ballpark it as <20:1 based on the human example, as an upper bound, which would have severe implications for LLM-based research—a good LLM solution might be 2 OOMs more expensive than the LLM itself per task. Obvious optimizations like load shifting to the cheapest electricity region or running batch jobs can reduce the cost, but not by that much.
Cheap, good, fast: pick 2. So LLMs may gain a lot of their economic efficiency over humans by making a severe tradeoff, in avoiding generating novelty or being long-duration agents. And if this is the case, few users will want to pay 20× more for their LLM uses, just because once in a while there may be a novel insight.
This will be especially true if there is no way to narrow down the retrieved facts to ‘just’ the user-relevant ones to save compute; it may be that the most far-flung and low-prior connections are the important ones, and so there is no easy way to improve, no matter how annoyed the user is at receiving random puns or interesting facts about the CIA faking vampire attacks.


Implications
Data moatOnly power-users, researchers, or autonomous agents will want to pay the ‘daydreaming tax’ (either in the form of higher upfront capital cost of training, or in paying for online daydreaming to specialize to the current problem for the asymptotic scaling improvements, see AI researcher Andy Jones 2021).
Data moat. So this might become a major form of RL scaling, with billions of dollars of compute going into ‘daydreaming AIs’, to avoid the “data wall” and create proprietary training data for the next generation of small cheap LLMs. (And it is those which are served directly to most paying users, with the most expensive tiers reserved for the most valuable purposes, like R&D.) These daydreams serve as an interesting moat against naive data distillation from API transcripts and cheap cloning of frontier models—that kind of distillation works only for things that you know to ask about, but the point here is that you don’t know what to ask about. (And if you did, it wouldn’t be important to use any API, either.)
Given RL scaling laws and rising capital investments, it may be that LLMs will need to become slow & expensive so they can be fast & cheap.



      
      
      
      
        Similar Links
        


Thinking LLMs: General Instruction Following with Thought Generation
Large Language Model Programs
Connecting the Dots: LLMs can Infer and Verbalize Latent Structure from Disparate Training Data
Boosting Theory-of-Mind Performance in Large Language Models via Prompting
Self-Ask: Measuring and Narrowing the Compositionality Gap in Language Models (Bamboogle)
Predictability and Surprise in Large Generative Models
The Scaling Hypothesis
Thoughts while watching myself be automated
Adding bits beats AI slop
‘Tools For Thought’ Failure
Why do writers still underestimate LLMs?
GPT-3 Semantic Derealization
Investigating the Ability of LLMs to Recognize Their Own Writing
Towards Benchmarking LLM Diversity & Creativity
Unleashing the Emergent Cognitive Synergy in Large Language Models: A Task-Solving Agent through Multi-Persona Self-Collaboration
Everything of Thoughts: Defying the Law of Penrose Triangle for Thought Generation
Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking
WBE & DRL: a Middle Way of imitation learning on brains
The Overfitted Brain: Dreams evolved to assist generalization
Dream to Control: Learning Behaviors by Latent Imagination
Search: GS; Google; site


      BibliographyClick to collapseClick to collapse

https://www.theparisreview.org/miscellaneous/4487/pablo-picasso-a-composite-interview-william-fifield
https://x.com/dwarkesh_sp/status/1727004083113128327
https://openai.com/blog/chatgpt/

	 
		“‘Dynamic Evaluation (NN)’ Directory ”2020 (compressed Transformer, continual learning; backlinks, bibliography):
	
	
		


		


Bibliography for directory ai/nn/dynamic-evaluation, most recent first: 4 related tags, 48 annotations, & 13 links (parent).

Dynamic evaluation or test-time finetuning is a performance-enhancing1 online machine learning technique where the ML model is trained further at runtime on ‘new’ data, eg. an RNN/Transformer is benchmarked on predicting text, but in addition to its prediction each timestep, it does an additional gradient descent on the newly-observed text. (It is analogous to short-term memory neural plasticity.) Dynamic evaluation was introduced for RNNs by Mikolov  et al 2 010, where the continual learning reduced perplexity in predicting English, and was used in many RNNs afterwards for the best performance (cf. neural cache).



Gradient descent works well. Have you considered using it more?
Dynamic evaluation is attractive because it requires no modifications to the architecture or training—it simply does more ‘training’, rather than leaving the weights frozen and relying on the hidden state (or self-attention) to do all learning, leading to greater consistency.2 It is especially useful when dealing with rare entities, domain shift, or personalization3, and for serial tasks where the best performance is needed. It can also be augmented with retrieval methods or adding in similar datapoints, which can teach the NN more.
Dynamic evaluation has fallen out of fashion due to emphasis on simple-to-deploy models, proprietary cloud services, and throughput over quality; but it may be revived by local NN models, or by tasks requiring cognitive flexibility not handled by pure self-attention (ARC?).


      
      
      
      
      
      
      


See Also
Gwern

“Nenex: A Neural Personal Wiki Idea ”, Gwern202 3

Links

“The Hidden Drivers of HRM’s Performance on ARC-AGI ”
“New News: System-2 Fine-Tuning for Robust Integration of New Knowledge ”, Park et  al 202 5
“On the Generalization of Language Models from In-Context Learning and Finetuning: a Controlled Study ”, Lampinen et  al 202 5
“One-Minute Video Generation With Test-Time Training ”, Dalal et  al 202 5
“RWKV-7 ‘Goose’ With Expressive Dynamic State Evolution ”, Peng et  al 202 5
“AUNN: Simple Implementation of Gwern’s AUNN Proposal ”, Roland202 4
“Emergent Properties With Repeated Examples ”, Charton & Kempe202 4
“Evaluating the Fairness of Task-Adaptive Pretraining on Unlabeled Test Data Before Few-Shot Text Classification ”, Dubey202 4
“Learning to (Learn at Test Time): RNNs With Expressive Hidden States ”, Sun et  al 202 4
“Instruction Modeling: Instruction Tuning With Loss Over Instructions ”, Shi et  al 202 4
“Test-Time Augmentation to Solve ARC ”, Cole202 4
“An Accurate and Rapidly Calibrating Speech Neuroprosthesis ”, Card et  al 202 4
“Revisiting Dynamic Evaluation: Online Adaptation for Large Language Models ”, Rannen-Triki et  al 202 4
“Neural Spline Fields for Burst Image Fusion and Layer Separation ”, Chugunov et  al 202 3
“Test-Time Adaptation of Discriminative Models via Diffusion Generative Feedback ”, Prabhudesai et  al 202 3
“In-Context Pretraining (ICP): Language Modeling Beyond Document Boundaries ”, Shi et  al 202 3
“OSD: Online Speculative Decoding ”, Liu et  al 202 3
“Dynamic Evaluation ”, Gwern202 3
“Re-Reading Improves Reasoning in Large Language Models ”, Xu et  al 202 3
“Test-Time Training on Video Streams ”, Wang et  al 202 3
“TTT-NN: Test-Time Training on Nearest Neighbors for Large Language Models ”, Hardt & Sun202 3
“FWL: Meta-Learning Fast Weight Language Models ”, Clark et  al 202 2
“Test-Time Training With Masked Autoencoders ”, Gandelsman et  al 202 2
“Large-Scale Retrieval for Reinforcement Learning ”, Humphreys et  al 202 2
“Don’t Stop the Training: Continuously-Updating Self-Supervised Algorithms Best Account for Auditory Responses in the Cortex ”, Orhan et  al 202 2
“Reconsidering the Past: Optimizing Hidden States in Language Models ”, Yoshida & Gimpel202 1
“Mind the Gap: Assessing Temporal Generalization in Neural Language Models § Scaling ”, Lazaridou et  al 202 1
“Mind the Gap: Assessing Temporal Generalization in Neural Language Models § Dynamic Evaluation ”, Lazaridou et  al 202 1 (page 7 org deepmind)
“Deep-Learning the Hardest Go Problem in the World (Igo #120) ”, Wu201 9
“Test-Time Training With Self-Supervision for Generalization under Distribution Shifts ”, Sun et  al 201 9
“Unsupervised Domain Adaptation through Self-Supervision ”, Sun et  al 201 9
“Mogrifier LSTM ”, Melis et  al 201 9
“Dynamic Evaluation of Transformer Language Models ”, Krause et  al 201 9
“Learning and Evaluating General Linguistic Intelligence ”, Yogatama et  al 201 9
“Faster SGD Training by Minibatch Persistency ”, Fischetti et  al 201 8
“Continuous Learning in a Hierarchical Multiscale Neural Network ”, Wolf et  al 201 8
“Dynamic Evaluation of Neural Sequence Models ”, Krause et  al 201 7
“Bayesian Recurrent Neural Networks ”, Fortunato et  al 201 7
“Learning Simpler Language Models With the Differential State Framework ”, II et al 2017
“Neural Episodic Control ”, Pritzel et  al 201 7
“Multiplicative LSTM for Sequence Modeling ”, Krause et  al 201 6
“One Sentence One Model for Neural Machine Translation ”, Li et  al 201 6
“Generating Sequences With Recurrent Neural Networks ”, Graves201 3
“Recurrent Neural Network Based Language Model § Dynamic Evaluation ”, Mikolov et  al 201 0 (page 2)
“Fast Text Compression With Neural Networks ”, Mahoney200 0
“OpenAI API § Prompt Caching ”
“RWKV Language Model ”
“Yu Sun ”
Sort By Magic

dynamic-learning
test-time-adaptation
meta-learning
dynamic-evaluation

Wikipedia (2)

Miscellaneous
Bibliography


Click to expandClick to expandBacklinks:
Click to expandClick to expandBibliography:

		
	

How Much Energy Does It Take To Think? Studies of Neural Metabolism Reveal Our Brain’s Effort to Keep Us Alive and the Evolutionary Constraints That Sculpted Our Most Complex Organ
 /doc/psychology/man-hands

	
		“An Evolutionary Gap in Primate Default Mode Network Organization ”, Clément M. Garin, Yuki Hori, Stefan Everling …, Christopher T. Whitlow, Finnegan J. Calabro, Beatriz Luna, Mathilda Froesel, Maëva Gacoin, Suliann Ben Hamed, Marc Dhenain, Christos Constantinidis2022 (animal psych, neuroscience; similar):
	
	
		
		
By comparing resting-state networks in humans, macaques, marmosets, and mouse lemurs, Garin et  al 202 2 identifies two networks in non-hominoid primates that include homolog areas of the human default mode network. The mPFC and PCC are tightly connected in the human DMN but poorly connected to each other across non-hominoid primates.



The human default mode network (DMN) is engaged at rest and in cognitive states such as self-directed thoughts. Interconnected homologous cortical areas in primates constitute a network considered as the equivalent.
Here, based on a cross-species comparison of the DMN between humans and non-hominoid primates (macaques, marmosets, and mouse lemurs), we report major dissimilarities in connectivity profiles. Most importantly, the medial prefrontal cortex (mPFC) of non-hominoid primates is poorly engaged with the posterior cingulate cortex (PCC), though strong correlated activity between the human PCC and the mPFC is a key feature of the human DMN. Instead, a fronto-temporal resting-state network involving the mPFC was detected consistently across non-hominoid primate species.
These common functional features shared between non-hominoid primates but not with humans suggest a substantial gap in the organization of the primate’s DMN and its associated cognitive functions.
Click to expandClick to expand
Similar Links:

Rat brains also have a default mode network
The Mind of a Mouse
Anatomy and function of an excitatory network in the visual cortex
Area-Specific Features of Pyramidal Neurons-a Comparative Study in Mouse and Rhesus Monkey
Allometric rules for mammalian cortical layer 5 neuron biophysics
Developmental mechanisms underlying the evolution of human cortical circuits
Evolution of the human brain: A human-specific gene is a determinant of the cognitive architecture of the human cerebral cortex
Differences and similarities between human and chimpanzee neural progenitors during cerebral cortex development
On the Working Memory of Humans and Great Apes: Strikingly Similar or Remarkably Different?
The 10-million-year explosion: Paleo-cognitive reconstructions of domain-general cognitive ability (G) in extinct primates
Using macroevolutionary patterns to distinguish primary from secondary cognitive modules in primate cross-species performance data on 5 cognitive ability measures
Prefrontal cortex in humans and apes: A comparative study of area 10
Embodied cognitive evolution and the cerebellum
Functional connectivity gradients as a common neural architecture for predictive processing in the human brain
Three individual difference constructs, one converging concept: adaptive problem solving in the human brain
Functional connectome fingerprinting: identifying individuals using patterns of brain connectivity
Brain-like functional specialization emerges spontaneously in deep neural networks
Large-scale, high-resolution comparison of the core visual object recognition behavior of humans, monkeys, and state-of-the-art deep artificial neural networks
Shared mechanisms underlie the control of working memory and attention
Evidence of a modality-dependent role of the cerebellum in working memory? An fMRI study comparing verbal and abstract n-back tasks
Search: GS; CP; Google; site



		
	


	
		“Rat Brains Also Have a Default Mode Network ”, Hanbing Lu, Qihong Zou, Hong Gu …, Marcus E. Raichle, Elliot A. Stein, Yihong Yang2012 (animal psych, neuroscience; similar):
	
	
		
		
The default mode network (DMN) in humans has been suggested to support a variety of cognitive functions and has been implicated in an array of neuropsychological disorders. However, its function remains poorly understood.
We show [using fMRI] that rats possess a DMN that is broadly similar to the DMNs of nonhuman primates and humans.
Our data suggest that, despite the distinct evolutionary paths between rodent and primate brain, a well-organized, intrinsically coherent DMN appears to be a fundamental [resting state/intrinsic activity] feature in the mammalian brain whose primary functions might be to integrate multimodal sensory and affective information to guide behavior in anticipation of changing environmental contingencies.

Click to expandClick to expandSimilar Links:

		
	


	 
		“Statistical Notes § Program for Non-Spaced-Repetition Review of past Written Materials for Serendipity & Rediscovery: Archive Revisiter ”, Gwern201 4 (Haskell, JS, R, genetics, IQ, Bayes, causality, decision theory, order statistics, power analysis, survey; backlinks, similar, bibliography):
	
	
		
		

Miscellaneous statistical stuff

“Spaced repetition” helps one remember facts by creating discrete flashcards which one tests oneself on at increasingly distant ‘spaced’ time periods, repeating the fact just before one probably would have forgotten it; using software to track & automate tests & review scheduling, spaced repetition can scale to hundreds of thousands of discrete items.
If spacing out facts can help one remember by repeating items just before they are forgotten, is there any use for an “anti-spaced repetition” with the opposite method of repeating items only after they are probably forgotten?
I can think of two: first, it could be used to plan consumption of media such as movies by eg. tracking one’s favorite movies of all time and scheduling a rewatch whenever one is predicted to have forgotten enough to make them novel & highly enjoyable again. Second, and more interestingly, it could be used as a serendipity generator by allowing efficient processing of notes or excerpts or old writings.
In rereading such materials many years later, one often gains a new perspective or learns something useful because one forgot something: one didn’t understand something about it at the time, or new material has radically changed one’s interpretation, and since it’d been forgotten, no use could be made of it. Unfortunately, using spaced repetition to memorize such material, while ensuring any serendipitous connections get made as soon as possible, would be radically infeasible for bulky items (a single lengthy text excerpt might correspond to hundreds of discrete items, quickly overloading even SRS systems) and for almost all items, useless. One can justify rereading old material once or perhaps twice, but not many rereads nor full memorization. But rereading haphazardly is likely to inefficiently cover some material many times while neglecting others, and such rereads will often be far too early in time (or—a lesser concern here—too late).
Instead of spaced repetition, one would instead use anti-spaced repetition: each item would be tracked and reviewed and its expected forgetting time predicted, as in spaced repetition, but instead of scheduling a review before forgetting, a review is scheduled for some time (probably long afterwards) after forgetting. The total number of reviews of each item per user lifetime would be set to a small number, perhaps 1–4, bounding the time consumption at a feasible amount.
Such an anti-spaced repetition system could be used with hundreds of thousands of notes or clippings which a person might accumulate over a lifetime, and enable them to invest a few minutes a day into reading old notes, occasionally coming up with new insights, while ensuring they don’t waste time reading notes too many times or reading notes they likely already remember & have exhausted.


Critiques

Failed Facebook Critiques
Correlation=Causation in Cancer Research
Aerobic vs Weightlifting
Moxibustion Mouse Study

“Someone Should Do Something”: Wishlist of Miscellaneous Project Ideas
Estimating Censored Test Scores
The Traveling Gerontologist Problem
Bayes Nets

Daily Weight Data Graph
Zeo Sleep Data

Genome Sequencing Costs
Proposal: Hand-Counting Mobile App for More Fluid Group Discussions
Air Conditioner Replacement

Parameters
Cost-Benefit

Discounting

Sensitivity Analysis

Some Ways of Dealing With Measurement Error
Value of Information: Clinical Prediction Instruments for Suicide
Bayesian Model Averaging
Dealing With All-Or-Nothing Unreliability of Data

Binomial

Binomial With Binary Unreliability

ABC
Mixture
Weakening Heuristic?



Dysgenics Power Analysis

Selection on SNPs
Mutation Load
Weaknesses
Genetic Data Availability

Proprietary
Public


Power Analysis for Racial Admixture Studies of Continuous Variables

Sibling Power Analysis
Adoption Power Analysis

Mean Population European Ancestry & Population Standard Deviation
Power Simulation


Operating on an Aneurysm

Risk
Expected Loss

QALY/DALY Adjustment

Cost-Benefit

The Power of Twins: Revisiting Student’s Scottish Milk Experiment Example
RNN Metadata For Mimicking Individual Author Style
MCTS
Candy Japan A/B Test
DeFries-Fulker Power Analysis
Inferring Mean IQs From SMPY/TIP Elite Samples
Genius Revisited: On the Value of High IQ Elementary Schools
Great Scott! Personal Name Collisions and the Birthday Paradox
Detecting Fake (Human) Markov Chain Bots
Optimal Existential Risk Reduction Investment
Model Criticism via Machine Learning
Proportion of Important Thinkers by Global Region Over Time in Charles Murray’s Human Accomplishment
Program for Non-Spaced-Repetition Review of past Written Materials for Serendipity & Rediscovery: Archive Revisiter
On the Value of New Statistical Methods
Bayesian Power Analysis: Probability of Exact Replication
Expectations Are Not Expected Deviations and Large Number of Variables Are Not Large Samples

Founder Effects

Oh Deer: Could Deer Evolve to Avoid Car Accidents?
Evolution As Backstop for Reinforcement Learning
Acne: a Good Quantified Self Topic
Fermi Calculations
Selective Emigration and Personality Trait Change

See Also

The Most Abandoned Books on GoodReads
Best Student Ever!
Little’s Law in the Wild
Tail Collapse


Click to expandClick to expandBacklinks:
Click to expandClick to expandSimilar Links:
Click to expandClick to expandBibliography:

		
	


	
		“All Roads Lead to Likelihood: The Value of Reinforcement Learning in Fine-Tuning ”, Gokul Swamy, Sanjiban Choudhury, Wen Sun …, Zhiwei Steven Wu, J. Andrew Bagnell2025 (Transformer, imitation learning, model-free RL, offline RL, preference learning; similar):
	
	
		
		
From a first-principles perspective, it may seem odd that the strongest results in foundation model fine-tuning (FT) are achieved via a relatively complex, two-stage training procedure. Specifically, one first trains a reward model (RM) on some dataset (eg. human preferences) before using it to provide online feedback as part of a downstream reinforcement learning (RL) procedure, rather than directly optimizing the policy parameters on the dataset via offline maximum likelihood estimation.
In fact, from an information-theoretic perspective, we can only lose information via passing through a reward model and cannot create any new information via on-policy sampling. To explain this discrepancy, we scrutinize several hypotheses on the value of RL in FT through both theoretical and empirical lenses.
Of the hypotheses considered, we find the most support for the explanation that on problems with a generation-verification gap, the combination of the ease of learning the relatively simple RM (verifier) from the preference data, coupled with the ability of the downstream RL procedure to then filter its search space to the subset of policies (generators) that are optimal for relatively simple verifiers is what leads to the superior performance of online FT.
Click to expandClick to expandSimilar Links:

		
Click to expandClick to expandView PDF:All Roads Lead to Likelihood: The Value of Reinforcement Learning in Fine-Tuning

	

Combinatorial Innovation and Technological Progress in the Very Long Run

	
		“Recipes and Economic Growth: A Combinatorial March Down an Exponential Tail ”, Charles I. Jones202 1 (economics, order statistics; backlinks, similar, bibliography):
	
	
		
		
[video; combinatorial innovation overview] New ideas are often combinations of existing goods or ideas, a point emphasized by Romer199 3 and Weitzman199 8. A separate literature highlights the links between exponential growth and Pareto distributions: Gabaix199 9 shows how exponential growth generates Pareto distributions, while Kortum199 7 shows how Pareto distributions generate exponential growth. But this raises a “chicken and egg” problem: which came first, the exponential growth or the Pareto distribution? And regardless, what happened to the Romer and Weitzman insight that combinatorics should be important?
This paper answers these questions by demonstrating that combinatorial growth in the number of draws from standard thin-tailed distributions leads to exponential economic growth; no Pareto assumption is required. More generally, it provides a theorem linking the behavior of the max extreme-value to the number of draws and the shape of the tail for any continuous probability distribution.
…the number of combinations we can create from existing ingredients is so astronomically large as to be essentially infinite, and we are limited by our ability to process these combinations. Let Nt denote the number of ingredients whose recipes have been evaluated as of date t. In other words, our “cookbook” includes all the possible recipes that can be formed from Nt ingredients: if each ingredient can either be included or excluded from a recipe, a total of 2Nt recipes are in the cookbook. Finally, research consists of adding new recipes to the cookbook—i.e. evaluating them and learning their productivities. In particular, suppose that researchers evaluate the recipes that can be made from new ingredients in such a way that Nt grows exponentially. We call a setup with 2Nt recipes with exponential growth in the number of ingredients combinatorial growth.
One key result in the paper is this: combinatorial expansion is so fast that drawing from a conventional thin-tailed distribution—such as the normal distribution–generates exponential growth in the productivity of the best recipe in the cookbook. Combinatorics and thin tails lead to exponential growth.
The way we derive this result leads to additional insights. For example, let K denote the cumulative number of draws (eg. the number of recipes in the cookbook) and let ZK be max of the K draws. Let F̄(10) denote the probability that a draw has a productivity higher than x—the complement of the cdf—so that it characterizes the search distribution. Then a key condition derived below relates the rise in ZK to the number of draws and to the search distribution: ZK increases asymptotically so as to stabilize ZF̄(ZK). That is, given a time path for the number of draws Kt, the maximum productivity marches down the upper tail of the distribution so as to make KtF̄(ZKt) stationary. Kortum199 7 can be viewed in this context: exponential growth in the max ZK is achieved by an exponentially growing number of draws K from a Pareto tail in F̄(·). Alternatively, with thinner tailed distributions like the normal or the exponential, combinatorial growth in K is required to get exponential growth in the max. Even the Romer199 0 model can be viewed in this light: linear growth in K requires a log-Pareto tail for the search distribution. This same logic can essentially be applied to any setup: if you want exponential growth in ZK from a particular search distribution F̄(·), then you need the rate at which you take draws from the distribution to stabilize KF̄(ZK).
…Theorem 1 (a simple extreme value result). Let ZK denote the maximum value from K > 0 independent draws from a continuous distribution F(10), with F̄(10) ≡ 1—F(10) strictly decreasing on its support. Then for m ≥ 0:
limK  →  ∞Pr[KF̄(ZK)≥m] = e−m
…Results related to Theorem 1 are of course known in the mathematical statistics literature. It is closely related to Proposition 3.1.1 in Embrechts et  al 199 7. Galambos197 8 (Chapter 4) develops a “weak law of large numbers” and a “strong law of large numbers” for extreme values; some of the results below will fit this characterization.2 However, the tight link between the number of draws, the shape of the tail, and the way the maximum increases is not emphasized in these treatments.
…In §5, we see that the combinatorial case has an important empirical prediction that distinguishes it from other cases: in the combinatorial setup, the number of “good” new ideas grows exponentially over time. By contrast, Kortum199 7 predicts that the flow of superior new ideas should be constant, even as the number of researchers grows.
Empirically, the flow of annual US patents exhibits rapid growth in recent decades, supporting the prediction of the combinatorial model.
Click to expandClick to expandSee Also:
Is Science Slowing Down?
Multi-Stage Bean Machine Visualization: Advantages of Repeated Optimization
Superexponential [Modeling the Human Trajectory]

Click to expandClick to expandBacklinks:
Click to expandClick to expandSimilar Links:
Click to expandClick to expandBibliography:

		
Click to expandClick to expandView PDF:Recipes and Economic Growth: A Combinatorial March Down an Exponential Tail

	

How the CIA Used ‘Vampires’ to Fight Communism in the Philippines § Blood-Sucking CIA Agents

	
		“Scaling Scaling Laws With Board Games ”, Andy L. Jones202 1 (computer hardware, AlphaGo, RL scaling; backlinks, similar):
	
	
		
		
[replication & extension] The largest experiments in machine learning now require resources far beyond the budget of all but a few institutions. Fortunately, it has recently been shown that the results of these huge experiments can often be extrapolated from the results of a sequence of far smaller, cheaper experiments. In this work, we show that not only can the extrapolation be done based on the size of the model, but on the size of the problem as well.
By conducting a sequence of experiments using AlphaZero and Hex, we show that the performance achievable with a fixed amount of compute degrades predictably as the game gets larger and harder. Along with our main result, we further show that the test-time and train-time compute available to an agent can be traded off while maintaining performance.



Figure 5: Each training run (each faint line) of each differently-sized agent follows a sigmoid, starting at random play and progressing up to some plateau. The frontiers (dark lines) formed by taking a maximum across training runs have a similar form across board sizes (colors).



Figure 6: The compute-performance frontier follows the same sigmoid for each board size 3 through 9, just scaled and shifted. The dotted lines give the fitted curves.

Slope: The slope of the incline is 500 Elo per order of magnitude increase in compute.
A more memorable interpretation is that if you are in the linearly-increasing regime, then you will need about 2× as much compute as your opponent to beat them 2⁄3 of the time.


Perfect play: The minimum compute needed for perfect play increases 7× for each increment in board size.
Takeoff: The minimum training compute needed to see any improvement over random play increases by 4× for each increment of board size.
Random play: Finally, the distance between random play and perfect play increases by 500 Elo for each increment of board size.
Unlike the other quantities mentioned previously, the distance between random and perfect play is a property of the game itself rather than of the agent.

…Train-test trade-off: So far we have focused on the compute budget during training, but another pertinent budget is the compute spent during evaluation. All the results discussed previously have used a tree search of size 64 during evaluation, the same as used during training. But there is no reason that the train-time search and test-time search have to be the same size, and so by varying the size of the test-time compute budget we can see in Figure 8 that larger tree searches at test time can substantially improve the performance of an agent.
Knowing now that compute can be spent in 2 places, at train time and test time, the immediate question is: how do these 2 budgets trade off? This is illustrated in Figure 9, which shows that the trade-off is linear in log-compute: for each additional 10× of train-time compute, about 15× of test-time compute can be eliminated, down to a floor of a single-node tree search…the simple relationship between compute at train time and compute at test time was originally surprising to us. Our intuition was that test-time compute is much ‘cheaper’ than train-time compute, and so we were surprised that one could easily substitute for the other. On reflection however, we believe the key distinction is that an optimization at test-time needs only optimize over one sample, while train-time compute meanwhile must optimize over the entire distribution of samples.



Figure 9: The trade-off between train-time compute and test-time compute. Each dotted line gives the minimum train-test compute required for a certain Elo on a 9 × 9 board.
…the way in which performance scales with compute is that an agent with twice as much compute as its opponent can win roughly 2⁄3 of the time. This behavior is strikingly similar to that of a toy model where each player chooses as many random numbers as they have compute, and the player with the highest number wins3. In this toy model, doubling your compute doubles how many random numbers you draw, and the probability that you possess the largest number is 2⁄3 [as you go from 1:1, half the total numbers drawn, to 2:1, or 2/(2+1)—as if each tree search were an independent lottery ticket]. This suggests that the complex game play of Hex might actually reduce to each agent having a ‘pool’ of strategies proportional to its compute, and whoever picks the better strategy wins. While on the basis of the evidence presented herein we can only consider this to be serendipity, we are keen to see whether the same behavior holds in other games.
Second, both the relation of performance to board size and the relation of performance to compute are smooth. Before embarking on this project, a key unknown was whether performance would show any ‘spikes’ with regards to compute or board size. A spike with regards to compute might indicate the model had achieved some key insight, while a spike with regards to board size might indicate a minimum complexity past which key insights are available for the model to discover. As is however, models’ performance changes smoothly and predictably with both increased compute and increased complexity.
Click to expandClick to expandBacklinks:
Click to expandClick to expandSimilar Links:

		
Click to expandClick to expandView PDF:Scaling Scaling Laws With Board Games

	

https://www.lesswrong.com/posts/HiTjDZyWdLEGCDzqu/implications-of-the-inference-scaling-paradigm-for-ai-safety?commentId=MPNF8uSsi9mvZLxqz
Click to expandClick to expandWikipedia Bibliography:
Pablo Picasso :

https://en.wikipedia.org/wiki/Pablo_Picasso
William Fifield :

https://en.wikipedia.org/wiki/William_Fifield
Large language model
Incubation (psychology)
Kohl (cosmetics) :

https://en.wikipedia.org/wiki/Kohl_(cosmetics)
Kohl :

https://en.wikipedia.org/wiki/Kohl
L’esprit de l’escalier :

https://en.wikipedia.org/wiki/L%27esprit_de_l%27escalier
Tip of the tongue :

https://en.wikipedia.org/wiki/Tip_of_the_tongue
Intrusive thought
Hippocampal replay :

https://en.wikipedia.org/wiki/Hippocampal_replay
Working memory
Short-term memory
Default mode network
Daydreaming :

https://en.wikipedia.org/wiki/Daydreaming
Wake-sleep algorithms :

https://en.wikipedia.org/wiki/Wake-sleep_algorithms
Reservoir sampling :

https://en.wikipedia.org/wiki/Reservoir_sampling⁠
Importance sampling⁠ :

https://en.wikipedia.org/wiki/Importance_sampling⁠

      
       

    

    
    
    
        
      
      
      
    
    