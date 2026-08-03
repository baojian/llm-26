---
title: "Final Lecture — Course Summary (NLP & LLMs, Spring 2026)"
duration: 40 minutes
audience: students (final review / discussion)
---

# Final Lecture: The Whole Course in 40 Minutes

**One-sentence story of the course:**
> We started from raw text and a counting table, and we ended at a model that can
> read, reason, follow instructions, and look things up. Every lecture removed one
> limitation of the previous one. Tonight we walk that staircase from the bottom to the top.

**The single thread that connects all 10 lectures:** every model in this course is just
estimating `P(next token | context)`. What changed each week was (1) how we represent the
context, (2) how we learn the parameters, and (3) how we make the output *useful*.

---

## Timing Plan (40 min)

| Segment | Topic | Time |
|---|---|---|
| 0 | Framing: the one equation | 3 min |
| 1 | Foundations of text (L01–L03) | 7 min |
| 2 | Neural sequence models → Transformer (L04–L05) | 8 min |
| 3 | Pretraining & GPT (L06) | 5 min |
| 4 | Evaluation & BERT (L07, L09-BERT) | 5 min |
| 5 | Post-training: SFT → RM → PPO → GRPO (L08–L09) | 8 min |
| 6 | Retrieval & RAG (L10) + the road ahead | 3 min |
| 7 | Discussion questions / wrap-up | 1 min |

> Speaker tip: keep one running diagram on the board — a horizontal arrow labeled
> **text → tokens → embeddings → attention → pretraining → alignment → retrieval**.
> Add a checkmark to each box as you finish a segment.

---

## Segment 0 — The One Equation (3 min)

Write this on the board and leave it there all lecture:

$$P(w_{1:T}) = \prod_{t=1}^{T} P(w_t \mid w_{1:t-1})$$

- Every model we built is a different machine for computing the right-hand factor.
- **n-gram:** truncate the context to the last N−1 words and *count*.
- **Neural LM / RNN:** compress the context into a learned hidden vector.
- **Transformer / GPT:** let every position attend to every earlier position.
- The training objective never really changed: **minimize cross-entropy / perplexity on next-token prediction.** What changed is the *function class* and the *data scale*.

**Discussion hook:** "If the objective is the same as a 2003 model, why is GPT-5 so much
better?" → answer threads through the whole lecture: representation power + scale + post-training.

---

## Segment 1 — Foundations of Text: L01–L03 (7 min)

### L01 Tokenization — *turning strings into a vocabulary*
- **Why we can't use words directly:** open vocabulary, OOV words, morphology, other languages, code, emoji.
- **BPE (Byte-Pair Encoding):** start from characters/bytes, repeatedly merge the most frequent adjacent pair until you hit the target vocab size. Greedy, frequency-driven.
- **WordPiece (BERT):** merge the pair that most increases corpus likelihood, i.e. maximize $\frac{P(\text{pair})}{P(\text{first})P(\text{second})}$ — picks pairs that "belong together," not just frequent ones.
- **Heaps' Law** $|V| = kT^{\beta}$ ($\beta \approx 0.4$–$0.75$): vocabulary keeps growing with corpus size → motivates *subword* units as the compromise between characters (too long) and words (too many).
- **Takeaway:** tokenization is a *design choice* with real downstream cost — it sets sequence length, model parameter count (embedding table), and how gracefully rare words degrade.

### L02 N-gram Language Models — *the first real LM*
- **Markov assumption:** $P(w_t \mid w_{1:t-1}) \approx P(w_t \mid w_{t-N+1:t-1})$.
- **MLE estimate:** $q(w_N \mid w_{1:N-1}) = \frac{C(w_{1:N})}{C(w_{1:N-1})}$ — just normalized counts.
- **The sparsity wall:** most possible n-grams are never seen → zero probability → infinite perplexity. This is *the* problem that motivates everything neural.
- **Smoothing:** add-k, interpolation, Katz back-off, **Kneser–Ney** (best classical baseline — uses *continuation counts*: how many distinct contexts a word completes, not raw frequency).
- **Perplexity:** $\text{PPL} = 2^{-\frac{1}{M}\log_2 P(w_{1:M})}$ — "average branching factor," the number of words the model is effectively choosing among. **Lower is better.** This is still how we report LM quality today.
- **Takeaway:** n-grams fail not because counting is wrong, but because *discrete symbols don't generalize*. "Dog" and "puppy" share no statistics. → We need representations where similar words are *close*.

### L03 Word Embeddings — *meaning as geometry*
- **Distributional hypothesis** (Firth): "a word is known by the company it keeps." Similar contexts ⇒ similar meaning.
- **Word2Vec (Skip-gram):** predict context words from a center word; objective $\sum_t \sum_{j} \log P(w_{t+j}\mid w_t)$ with $P(c\mid w) \propto \exp(v_c \cdot v_w)$.
- **Negative sampling:** replace the $|V|$-way softmax with a handful of binary "real vs. fake context" decisions → makes training on billions of words feasible.
- **Two evaluations:** *intrinsic* (analogies: king − man + woman ≈ queen; cosine similarity) vs. *extrinsic* (does it help a downstream classifier?). Always prefer extrinsic.
- **Classifiers along the way:** Naive Bayes (generative, independence assumption) → Logistic Regression / softmax (discriminative). Softmax + cross-entropy is the *same output head* used by every neural model afterward.
- **Takeaway:** embeddings fix the generalization problem of n-grams — but Word2Vec gives each word *one* vector regardless of context. "bank" (river) = "bank" (money). → We need *contextual* representations.

**Bridge to Segment 2:** Foundations are about *what a token is* and *how to represent it*.
The rest of the course is about *how to mix representations across a sequence*.

---

## Segment 2 — Neural Sequence Models → Transformer: L04–L05 (8 min)

### L04 Neural LMs — *learned context, but sequential*
- **NPLM (Bengio 2003):** concatenate the embeddings of the last n−1 words, push through a tanh hidden layer, softmax over vocab: $y = b + Wx + U\tanh(d + Hx)$. First neural model to beat n-grams — and it *learns embeddings as a byproduct*.
- **RNN / LSTM:** process tokens one at a time, carry a hidden state. **LSTM gates** (input / forget / output) let gradients survive across long sequences → solves vanishing gradients.
- **Seq2Seq (encoder–decoder):** encode the whole input into one vector, decode the output. Worked for translation **but** the single fixed context vector is a *bottleneck* — long sentences lose information.
- **Attention (Bahdanau 2015):** let the decoder look back at *all* encoder states, weighted by relevance, instead of one frozen vector. This is the seed of everything next.
- **Takeaway:** two unsolved pains remain — (1) recurrence is *sequential* → can't parallelize over a GPU; (2) long-range dependencies still travel through O(n) steps.

### L05 The Transformer — *attention is all you need*
- **Core idea:** throw away recurrence. Let every position directly attend to every other position in one step.
- **Scaled dot-product attention:**
$$\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$
Query asks, Key advertises, Value carries the content; the $\sqrt{d_k}$ keeps the softmax from saturating.
- **Multi-head attention:** run h attention computations in parallel subspaces, concat. Different heads learn different relations (syntax, coreference, position).
- **Positional encoding:** attention is order-blind, so inject position via sinusoids $PE_{(pos,2i)}=\sin(pos/10000^{2i/d})$ (or learned positions).
- **The block:** `x → MultiHeadAttention → +residual & LayerNorm → FFN → +residual & LayerNorm`. Stack N of these.
- **Encoder vs. decoder:** encoder attends both directions (→ BERT); decoder uses a **causal mask** so position t sees only ≤ t (→ GPT).
- **Why it won:** (1) fully parallel over sequence length → exploits GPUs → enables scale; (2) constant path length between any two tokens → genuinely long-range. **Architecture stopped changing here** — GPT, BERT, LLaMA, Qwen are all this block.
- **Takeaway:** the Transformer is the *substrate*. Everything after L05 is about what we *train it on* and *how we steer it*, not how we wire the neurons.

**Bridge:** same block, two destinies — mask it one way and scale up → GPT (generation);
mask it the other way and pretrain with masking → BERT (understanding).

---

## Segment 3 — Pretraining & GPT: L06 (5 min)

- **Decoder-only, autoregressive:** GPT keeps only the masked decoder stack and trains on plain next-token prediction over enormous unlabeled corpora. No labels needed — the text *is* the supervision.
- **Why this is a big deal:** one objective, unlimited data. Pretraining learns grammar, facts, translation, and rudimentary reasoning *for free*, as side effects of predicting the next token.
- **Scaling laws:** loss falls as a smooth power law in (parameters, data, compute). Bigger + more data ⇒ predictably better. This turned model-building into an *engineering / budgeting* problem.
- **The GPT line as a story of scale:**
  - GPT-1 (2018, ~117M): pretrain-then-finetune works.
  - GPT-2 (2019, 1.5B): zero-shot tasks emerge; "just scale it."
  - GPT-3 (2020, 175B): **in-context / few-shot learning** — learn a task from the prompt, no weight updates.
  - GPT-4 (2023) → GPT-5 (2025): multimodal, stronger reasoning, undisclosed internals.
- **Inference knobs:** temperature $p_i = \frac{\exp(z_i/T)}{\sum_j\exp(z_j/T)}$ (low T = sharp/greedy, high T = diverse), plus top-k / nucleus (top-p) sampling.
- **Takeaway:** pretraining gives a model that *knows a lot* but **doesn't reliably do what you ask** — it completes text, it doesn't follow instructions or respect preferences. That gap is the entire motivation for post-training (Segment 5).

---

## Segment 4 — Evaluation & BERT: L07 (+ BERT) (5 min)

### How do we even know a model is good?
- **GLUE / SuperGLUE:** a *suite* of NLU tasks (sentiment, entailment, paraphrase, QA) under one leaderboard. Forces general capability, not one-task overfitting. SuperGLUE was created once models *saturated* GLUE.
- **Knowledge & reasoning benchmarks:** **MMLU** (57 subjects, multitask knowledge), **HellaSwag** (adversarially-filtered commonsense completion), **SWAG**, **CoQA**. Newer frontier: HLE ("Humanity's Last Exam"), ARC-AGI.
- **Evaluation paradigms:** fill-mask probability, label-likelihood comparison, and chat/instruction-style — *the same model scores differently depending on how you ask.*
- **Discussion point:** benchmarks drive the field but get gamed (contamination, saturation). "When a measure becomes a target, it ceases to be a good measure." (Goodhart)

### BERT — the other branch of the Transformer
- **Bidirectional encoder**, pretrained with **Masked LM**: mask ~15% of tokens, predict them from *both* sides: $\mathcal{L}_{\text{MLM}} = -\sum_{i \in \text{masked}} \log p_\theta(x_i \mid x_{\setminus i})$. Plus Next-Sentence Prediction.
- **Use it by fine-tuning:** stick a head on the `[CLS]` token → $\hat{y} = \text{softmax}(W h_{\text{[CLS]}})$ for classification, NER, QA.
- **GPT vs. BERT in one line:** BERT *understands* (encoder, bidirectional, great for classification/retrieval); GPT *generates* (decoder, causal, great for open-ended text). Same Transformer block, opposite masking, opposite use-case.
- **Takeaway:** evaluation and BERT close the "understanding" loop — but the headline models of 2023+ are generative + *aligned*, which is where we go next.

---

## Segment 5 — Post-training: SFT → RM → PPO → GRPO: L08–L09 (8 min)

> This is the segment that turns a *text predictor* into an *assistant*. Spend real time here.

A pretrained model maximizes "plausible continuation." We actually want "helpful, honest,
instruction-following." Post-training closes that gap in stages.

### Stage 1 — SFT (Supervised Fine-Tuning)
- Fine-tune on curated `(instruction, ideal response)` pairs; loss only on the response tokens:
  $\mathcal{L}_{\text{SFT}} = -\sum_{t \in \text{response}} \log p_\theta(x_t \mid x_{<t})$.
- Teaches *format and style* (answer the question, use the chat template). Cheap and powerful, but limited by how many gold demonstrations humans can write.

### Stage 2 — RM (Reward Modeling)
- Humans find it *easier to compare* than to write the perfect answer → collect preference pairs (chosen $y_w$ vs. rejected $y_l$).
- **Bradley–Terry loss:** $\mathcal{L}_{\text{RM}} = -\mathbb{E}\big[\log \sigma\big(r_\theta(x,y_w) - r_\theta(x,y_l)\big)\big]$ → a scalar reward model that *scores* any response.

### Stage 3 — PPO (RLHF)
- Optimize the policy to earn reward, but **anchor it to the SFT model** with a KL penalty so it doesn't drift into gibberish that games the RM:
  $$J(\phi) = \mathbb{E}\big[r_\theta(x,y) - \beta \log \tfrac{\pi_\phi(y\mid x)}{\pi^{\text{SFT}}(y\mid x)}\big]$$
- **PPO clip** keeps updates stable: with ratio $r_t = \pi_\theta/\pi_{\text{old}}$,
  $L^{\text{CLIP}} = \mathbb{E}[\min(r_t \hat{A}_t, \text{clip}(r_t, 1-\varepsilon, 1+\varepsilon)\hat{A}_t)]$.
- **The catch — reward hacking:** the RM is a proxy. Push too hard and the policy finds outputs that score high but humans dislike. The KL term is the leash. PPO also needs **3 model copies** (actor, critic, reference) → memory-hungry.
- This is the **InstructGPT** recipe — the lineage behind ChatGPT/Claude/Gemini.

### Stage 4 — GRPO (the 2025 simplification)
- **Drop the critic and the learned RM.** For each prompt, sample a *group* of G responses and use the **group mean as the baseline**:
  $$\hat{A}_i = \frac{r_i - \mu_r}{\sigma_r + \varepsilon}$$
- **Verifiable rewards:** for math/code, correctness is checkable (the answer is right or wrong) → no reward model, no reward hacking, no distribution shift.
- **DeepSeek-R1-Zero:** even drop the KL penalty and clipping → an almost-pure policy gradient, $J(\theta) \propto \sum_i \sum_t \log \pi_\theta(o_{i,t}\mid q, o_{i,<t})\,\hat{A}_i$.
- **Emergent reasoning:** with a tiny format reward (use `<think>…</think>`) plus a correctness reward, the model *teaches itself chain-of-thought* — longer reasoning, self-checking — purely from RL. This is the 2025 "reasoning model" story.
- **Why it matters:** 1 model copy instead of 3 (fits bigger models), and RL on *verifiable* rewards is the current frontier of making models *reason*, not just *please*.

**Aside — DPO (the no-RL shortcut):** Direct Preference Optimization skips the RL loop
entirely and optimizes the preference data with a single classification-style loss derived
from the same KL-regularized objective. Mention it as "the other popular branch."

**Takeaway for the segment:** the trajectory is *more capability with less machinery* —
from "humans write answers" (SFT) → "humans rank answers" (RM+PPO) → "a checker grades
answers" (GRPO). Each step removes a human bottleneck.

---

## Segment 6 — Retrieval & RAG + Road Ahead: L10 (3 min)

### RAG (Retrieval-Augmented Generation)
- **Problem RAG solves:** a pretrained model's knowledge is *frozen in its weights* (parametric memory) — it goes stale, it can't cite, it hallucinates.
- **Idea:** give the model a *non-parametric memory* — an external, updatable document index it can look things up in.
- **Pipeline:** chunk docs → embed each chunk → store in a vector index → at query time, embed the question, retrieve top-k by cosine similarity, **prepend** them to the prompt, and instruct the model to answer *only from context*.
  $$\text{sim}(\mathbf{q},\mathbf{d}) = \frac{\mathbf{q}\cdot\mathbf{d}}{\|\mathbf{q}\|\,\|\mathbf{d}\|}$$
- **Key rules:** same embedding model at index- and query-time; chunk with overlap; garbage-in-garbage-out — generation quality is capped by retrieval quality.
- **Why it matters:** update knowledge without retraining, ground answers in citable sources, reduce hallucination. The dense-retrieval half is *exactly* the embedding idea from L03, grown up.

### Where the course points next (Weeks 13–16)
- Diffusion language models; deeper alignment & safety (red-teaming, jailbreaks);
  efficiency & systems (KV-cache, quantization, throughput); agents & multimodal frontiers.

---

## Segment 7 — The Staircase, in One Picture (wrap-up, 1 min)

```
text ──▶ tokens ──▶ embeddings ──▶ attention ──▶ Transformer ──▶ pretraining ──▶ alignment ──▶ retrieval
 L01      L01         L03            L04           L05            L06            L08-09          L10
 │         │           │              │             │              │               │              │
 raw     subword    meaning as    look back at   parallel +    learn from     follow         look it up
strings   units      geometry      the context   long-range    raw text       instructions   when unsure
```

**Each lecture removed one bottleneck of the one before it:**

| From | Limitation | Fixed by |
|---|---|---|
| n-grams | symbols don't generalize | embeddings (L03) |
| Word2Vec | one vector per word, no context | RNN/attention (L04) |
| RNN | sequential, short memory | Transformer (L05) |
| Transformer | needs labels / supervision | pretraining (L06) |
| pretrained GPT | doesn't follow instructions | SFT + RLHF (L08) |
| PPO/RLHF | expensive, reward hacking | GRPO + verifiable rewards (L09) |
| any LLM | frozen, hallucinating knowledge | RAG (L10) |

---

## Discussion Questions (pick a few)

1. The training objective (next-token prediction) barely changed from 2003 to 2025. So what *actually* produced the jump in capability — architecture, scale, data, or post-training? Defend a ranking.
2. Perplexity vs. benchmark accuracy vs. human preference — when do they disagree, and which would you optimize for a chatbot?
3. GPT (decoder) vs. BERT (encoder): for a *retrieval* system in RAG, which do you embed your documents with, and why?
4. RLHF aligns to *human preference*; GRPO aligns to a *verifiable checker*. What kinds of tasks can each align, and where does each break?
5. RAG fixes stale knowledge without retraining. Why not just fine-tune the new facts in? When is each the right tool?
6. Reward hacking (PPO) and benchmark gaming (Goodhart) are the same failure in two places. Where else in the pipeline does optimizing a proxy bite us?

---

## 60-Second Recap (if you run out of time, say only this)

> Everything was `P(next token | context)`. We made the *context representation* richer
> (counts → embeddings → attention), we *scaled* the Transformer on raw text until it
> learned the world (pretraining), then we *steered* it to be useful (SFT → RLHF → GRPO),
> and finally we *grounded* it in external facts (RAG). Same equation, seven removed
> bottlenecks, one assistant.
