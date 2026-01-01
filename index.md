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

## Course Overview

### Introduction

This course covers the foundations and modern frontiers of Natural Language Processing (NLP), with a heavy emphasis on **Large Language Models (LLMs)**. You will learn the modern pipeline of building effective LLMs from basic tokenization to training, fine-tuning, and deploying modern LLM architectures. Our target audiences are undergraduates and graduate students.

- **Prerequisites:** No formal prerequisites. For Fudan students, it’s safe to take this course in your second year.

### Basic Info

- **Course ID:** CS40008.01: NLP and LLMs
- **Course Info:** Spring 2026, Fudan University
- **Instructor:** [Baojian Zhou](https://baojian.github.io/), Email: bjzhou AT fudan.edu.cn
- **TAs:**
  - Coming soon
  - Coming soon
  - Coming soon
- **Time:** 03/05/2026–06/18/2026, Thu., 1:30 pm – 4:10 pm, <a href="Fudan-2026-spring-calendar.pdf" target="_blank" rel="noopener">Fudan Calendar</a>
- **Location:** Coming Soon
- **Office Hours:** 10:00 am – 1:00 pm, Thu & 611



---

## Assignments and Course Project

All standard homework assignments are completed by **Week 12**. The final month (Weeks 13–16) is dedicated exclusively to the Course Project. Please submit your homework at [https://elearning.fudan.edu.cn/](https://elearning.fudan.edu.cn/)

### Assignment 1. Foundations of Text
- **Due:** Week 4
- **Scope:** Implement BPE tokenization from scratch; train a Word2Vec model.
- **Deliverable:** Python Notebook + Analysis Report.

### Assignment 2. The Transformer Block
- **Due:** Week 7
- **Scope:** Build a mini-Transformer; visualize attention heads.
- **Track B Requirement:** Implement `MultiHeadAttention` in raw PyTorch without `nn.Transformer`.

### Assignment 3. LLM Lifecycle: Fine-tuning
- **Due:** Week 10
- **Scope:** Parameter-Efficient Fine-Tuning (LoRA) of a small Llama/Qwen model on a custom instruction set.
- **Eval:** Compare pre-trained vs. fine-tuned performance on specific tasks.

### Assignment 4. RAG Systems
- **Due:** Week 12
- **Scope:** Build a vertical QA system (e.g., "Textbook Chatbot"). Index a specific PDF/Corpus, implement retrieval + generation loop, and evaluate hallucination rates using automated metrics.

### Course Project
- **Timeline:** Weeks 13–16 (Dedicated time)
- **Teams:** 2-3 Students.
- **Deliverables:**
  - **Week 9:** 1-page Project Proposal (Problem, Dataset, Baselines).
  - **Week 14:** Status Check / Preliminary Results.
  - **Week 16:** Final Report + Presentation.
- **Tracks:**
  - *Research:* Novel architecture, loss function, or extensive ablation study.
  - *Application:* End-to-end tool/agent with UI (Streamlit/Gradio).
  - *Systems:* High-performance inference engine or quantization study.

---

## Resources and References

- **Textbook & Readings**
  - [Speech and Language Processing (Jurafsky & Martin, 3rd Ed. Draft)](https://web.stanford.edu/~jurafsky/slp3/)
  - Coming soon
- **Computing & Communication**
  - **University Cluster:** [https://cfff.fudan.edu.cn/home](https://cfff.fudan.edu.cn/home)
  - **Course Repo:** [baojian/llm-26](https://github.com/baojian/llm-26)
  - **Academic Integrity:** Please check [our policies](https://xxgk.fudan.edu.cn/_upload/article/files/f5/11/cc2c9a8c4f3ead2dbb00e4fa33c8/02adc618-b180-435c-b1bd-baf4cba3dd72.pdf).
- **AI Policy**
Use of AI coding assistants **is permitted**. However, you should explicitly attribute the use of AI in your assignment.

---

## Weekly Schedule

### Week 1 Introduction to LLMs

In our first lecture, we introduce text preprocessing, including tokenization (BPE/WordPiece), and vocab design.

- **Slides:**
- **Readings:**
  - dd
  - ddd
  - ddd
- **Notes:**
- **Excercise:**

**Release Assignment 1**

### Week 2 N-Gram Language Models

In this lecture, we introduce the concept of MLE, Smoothing, Perplexity, and Language Modeling basics.

- **Slides:**
- **Readings:**
  - <a href="lecture-01/readings-0-JM%20Book%20Chapter%202.pdf" target="_blank" rel="noopener">JM Book Chapter 2</a>
  - <a href="lecture-01/readings-1-Advances%20in%20NLP.pdf" target="_blank" rel="noopener">Advances in NLP</a>
  - <a href="lecture-01/readings-2-Human%20Language%20Understanding%20and%20Reasoning.pdf" target="_blank" rel="noopener">Human Language Understanding and Reasoning</a>
  - <a href="lecture-01/readings-3-Scaling%20Laws%20with%20Vocabulary-2407.13623v1.pdf" target="_blank" rel="noopener">Scaling Laws with Vocabulary (2407.13623v1)</a>
  - <a href="lecture-01/readings-4-Getting%20the%20most%20out%20of%20your%20tokenizer%20for%20pre-training.pdf" target="_blank" rel="noopener">Getting the most out of your tokenizer for pre-training</a>
- **Notes:**
- **Excercise:**
- 

### Week 3 Word Embeddings

Word2Vec, Distributional Hypothesis, Intrinsic/Extrinsic eval

### Week 4 Neural LMs

FFNNs for language, Softmax, Batching, Optimization

**Assignment 1 Due**
**Release Assignment 2**

### Week 5 Sequence Modeling

RNNs/LSTMs (Brief overview), Encoder-Decoder paradigms


### Week 6 Attention Mechanisms

Dot-product attention, Query/Key/Value intuition

### Week 7 The Transformer Architecture

Self-Attention, Multi-head, Positional Encodings, LayerNorm

**Assignment 2 Due** 
**Release Assignment 3**

### Week 8 LLM Pretraining

Causal LM vs MLM, Chinchilla Scaling Laws, Data Mixtures

### Week 9 Fine-tuning & PEFT

SFT, LoRA/QLoRA, Adapters, Instruction Tuning

**Project Proposal Due**

### Week 10 Evaluation

Benchmarks (MMLU/GSM8K), Contamination, LLM-as-a-judge

**Assignment 3 Due** 
**Release Assignment 4**

### Week 11 Prompt Engineering

In-context learning, Chain-of-Thought, Prompt sensitivity 

### Week 12 Course Project Presentation

### Week 13 RAG Systems

Dense Retrieval, Vector DBs, Reranking, Grounding

### Week 14 Alignment & Safety

RLHF (PPO/DPO), Safety barriers, Red-teaming

### Week 15 Efficiency & Systems

KV Caching, Quantization (Int8/FP4), Latency/Throughput

### Week 16 Frontiers

Multimodal LLMs, Diffusion LMs, Future Directions


