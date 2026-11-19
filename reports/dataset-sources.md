
# Dataset Sources and Selection

## Project
Comparative LLM Security Evaluation

## 1. Hugging Face Dataset

**Name:** Prompt Injection & Jailbreak Detection Dataset

**Publisher:** NeurAlchemy

**Source:** https://huggingface.co/datasets/neuralchemy/Prompt-injection-dataset

**Licence:** Apache 2.0

**Purpose:**

To obtain labelled benign and malicious prompts for controlled prompt-injection evaluation and security analysis.

## 2. Kaggle Dataset

**Name:** AI Agent Vulnerability & Red-Teaming Telemetry

**Source:** https://www.kaggle.com/luthfimuthathohirin/ai-agent-vulnerability-red-teaming-2026

**Reported licence:** CC0 1.0

**Purpose:**

To investigate AI-agent security scenarios, attack categories and vulnerability patterns.

## 3. Data Handling

- Inspect dataset structure before use.
- Record original sources and licensing.
- Select a manageable sample for experiments.
- Remove personally identifiable information if present.
- Do not treat dataset labels as proof of successful attacks.
- Preserve original labels and distinguish them from experimental observations.

## 4. Evaluation Plan

Selected examples will be tested against ChatGPT, Claude and Gemini.

Results will be recorded independently and analysed using Python.
