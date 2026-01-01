---
layout: default
title: "NLP & LLMs"
description: Spring 2026 @ Fudan University
theme: jekyll-theme-minimal
---

## Outline
{: .no_toc }

* TOC
{:toc}

---

# Course Overview

- **Course ID:** CS40008.01: NLP and LLMs
- **Course Info:** Spring 2026, Fudan University
- **Instructor:** [Baojian Zhou](https://baojian.github.io/), Email: bjzhou AT fudan.edu.cn
- **TAs:**
  - Coming soon
  - Coming soon
  - Coming soon
- **Time:** 03/05/2026–06/18/2026, Thu., 1:30 pm – 4:10 pm
- **Location:** Coming Soon
- **Office Hours:** 10:00 am – 1:00 pm, Thu & 611

This course covers the foundations and modern frontiers of Natural Language Processing (NLP), with a heavy emphasis on **Large Language Models (LLMs)**. You will learn the modern pipeline of building effective LLMs from basic tokenization to training, fine-tuning, and deploying modern LLM architectures.

* **Target Audience:** Mixed Undergraduate & Graduate students.
* **Prerequisites:** No formal prerequisites. For Fudan students, it’s safe to take this course in your second year.

---

# Weekly Schedule

**Note:** All standard homework assignments are completed by **Week 12**. The final month (Weeks 13–16) is dedicated exclusively to the Final Project.

| Week | Topic | Key Concepts | Lab / Assignment |
| :--- | :--- | :--- | :--- |
| **1** | **NLP Foundations** | Text preprocessing, Tokenization (BPE/WordPiece), Vocab design | *Release Assignment 1* |
| **2** | **N-Gram Models** | MLE, Smoothing, Perplexity, Language Modeling basics | |
| **3** | **Word Embeddings** | Word2Vec, Distributional Hypothesis, Intrinsic/Extrinsic eval | |
| **4** | **Neural LMs** | FFNNs for language, Softmax, Batching, Optimization | **Assn 1 Due** (Foundations) |
| **5** | **Sequence Modeling** | RNNs/LSTMs (Brief overview), Encoder-Decoder paradigms | *Release Assignment 2* |
| **6** | **Attention Mechanisms** | Dot-product attention, Query/Key/Value intuition | |
| **7** | **The Transformer** | Self-Attention, Multi-head, Positional Encodings, LayerNorm | **Assn 2 Due** (Architecture) |
| **8** | **LLM Pretraining** | Causal LM vs MLM, Chinchilla Scaling Laws, Data Mixtures | *Release Assignment 3* |
| **9** | **Fine-tuning & PEFT** | SFT, LoRA/QLoRA, Adapters, Instruction Tuning | **Project Proposal Due** |
| **10** | **Evaluation** | Benchmarks (MMLU/GSM8K), Contamination, LLM-as-a-judge | **Assn 3 Due** (Finetuning) |
| **11** | **Prompt Engineering** | In-context learning, Chain-of-Thought, Prompt sensitivity | *Release Assignment 4* |
| **12** | **Course Project** | Presentation | |
| **13** | **RAG Systems** | Dense Retrieval, Vector DBs, Reranking, Grounding | **Assn 4 Due** (Systems) |
| **14** | **Alignment & Safety** | RLHF (PPO/DPO), Safety barriers, Red-teaming | *Project Work Week* |
| **15** | **Efficiency & Systems** | KV Caching, Quantization (Int8/FP4), Latency/Throughput | *Project Work Week* |
| **16** | **Frontiers** | Multimodal LLMs, Diffusion LMs, Future Directions | **Final Project Presentation** |

---

## Assignments & Grading

Please submit your homework at [https://elearning.fudan.edu.cn/](https://elearning.fudan.edu.cn/)

### 1. Foundations of Text (10%)
* **Due:** Week 4
* **Scope:** Implement BPE tokenization from scratch; train a Word2Vec model.
* **Deliverable:** Python Notebook + Analysis Report.

### 2. The Transformer Block (15%)
* **Due:** Week 7
* **Scope:** Build a mini-Transformer; visualize attention heads.
* **Track B Requirement:** Implement `MultiHeadAttention` in raw PyTorch without `nn.Transformer`.

### 3. LLM Lifecycle: Fine-tuning (15%)
* **Due:** Week 10
* **Scope:** Parameter-Efficient Fine-Tuning (LoRA) of a small Llama/Qwen model on a custom instruction set.
* **Eval:** Compare pre-trained vs. fine-tuned performance on specific tasks.

### 4. RAG Systems (20%)
* **Due:** Week 12
* **Scope:** Build a vertical QA system (e.g., "Textbook Chatbot"). Index a specific PDF/Corpus, implement retrieval + generation loop, and evaluate hallucination rates using automated metrics.

### 5. Final Project (40%)
* **Timeline:** Weeks 13–16 (Dedicated time)
* **Teams:** 2-3 Students.
* **Deliverables:**
    * **Week 9:** 1-page Project Proposal (Problem, Dataset, Baselines).
    * **Week 14:** Status Check / Preliminary Results.
    * **Week 16:** Final Report + Presentation.
* **Tracks:**
    * *Research:* Novel architecture, loss function, or extensive ablation study.
    * *Application:* End-to-end tool/agent with UI (Streamlit/Gradio).
    * *Systems:* High-performance inference engine or quantization study.

---

## Resources

### Textbook & Readings
* **Primary:** [Speech and Language Processing (Jurafsky & Martin, 3rd Ed. Draft)](https://web.stanford.edu/~jurafsky/slp3/)

### Computing
* **University Cluster:** [https://cfff.fudan.edu.cn/home](https://cfff.fudan.edu.cn/home)

### Communication
* **Course Repo:** [baojian/llm-26](https://github.com/baojian/llm-26)
* **Discussion:** WeChat:

### Academic Integrity

* Please check [our policies](https://xxgk.fudan.edu.cn/_upload/article/files/f5/11/cc2c9a8c4f3ead2dbb00e4fa33c8/02adc618-b180-435c-b1bd-baf4cba3dd72.pdf). 

**AI Policy:** Use of AI coding assistants **is permitted**. However, you should explicitly attribute the use of AI in your assignment.
