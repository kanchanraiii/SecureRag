# SecureRag

A secure Retrieval-Augmented Generation (RAG) system.

## Description

This project implements a secure RAG system that combines information retrieval with generative AI capabilities while maintaining data security and privacy.

**Status:** Ongoing [Final Year Project & Pre-Publication Research]

---

## 1. Overview

SecureRag is an ongoing research and development initiative focused on building and evaluating secure Retrieval-Augmented Generation (RAG) systems. In an era where RAG pipelines are increasingly connected to sensitive enterprise and user data, ensuring robustness, privacy, and security is paramount.

This project investigates critical vulnerabilities in standard RAG pipelines and implements a multi-layered defense and evaluation framework. The primary goals are to prevent inadvertent leakage of Personally Identifiable Information (PII) and to test the system's resilience against sophisticated adversarial attacks.

**Note:** _As this project is part of ongoing academic research intended for publication, this repository provides a high-level overview of the architecture and goals. The full source code and detailed experimental results will be made public post-publication._

## 2. Key Features

* **Synthetic Data Generation:** A custom pipeline to generate large-scale, realistic user data (60,000+ JSONL entries) using the `Faker` library, providing a safe and effective testbed.
* **Dynamic PII Guardrail:** Implementation of an output-level security filter using `Microsoft Presidio` to detect and redact a wide range of PII entities in real-time before they reach the end-user.
* **Multi-LLM & Retriever Backend:** A flexible architecture designed to benchmark and integrate various Large Language Models (Gemini 2.5 Flash, Mistral models) and sentence transformers (BERT variants, MiniLM), allowing for analysis of security-performance trade-offs.
* **Advanced Robustness Testing:** A suite of custom evaluation scripts to rigorously test the security and reliability of the RAG pipeline against known failure modes.

## 3. Technology Stack

* **Core Framework:** Python 3.10+
* **LLM & NLP:** Hugging Face `transformers`, `sentence-transformers`, Google AI SDK, Mistral AI API
* **Data Generation:** `Faker`
* **Security & Privacy:** `Microsoft Presidio` (Anonymizer & Analyzer)
* **Data Handling:** `Pandas`, `JSONL`
* **Vector Stores:** `FAISS`
* **Orchestration:** `LangChain`

## 4. Security & Evaluation Focus

This project moves beyond standard accuracy metrics to focus on critical security vectors. Our evaluation suite is designed to probe for weaknesses in two key areas:

1.  **Data Privacy & Leakage:**
    * **PII Exposure:** Testing the effectiveness of the Presidio-based guardrail against a corpus of PII-rich synthetic data.

2.  **System Robustness & Resilience:**
    * **Prompt Injection & LLM Isolation:** Employing techniques like **Base64 encoding obfuscation** to test whether the LLM's system prompt and security instructions can be bypassed.
    * **Retrieval Accuracy Under Distraction:** Using the **"Needle in a Haystack"** analysis to evaluate the retriever's ability to find relevant facts within long, noisy contexts, a key factor in preventing hallucination and ensuring factual grounding.

## 5. Project Status & Future Work

The framework is currently functional, and extensive benchmarking is underway. Future work will involve:

* Exploring more advanced prompt injection threat vectors.
* Investigating the trade-offs between retrieval performance and security filtering.
* Developing a comprehensive scoring model for overall RAG system security.
