# Comparative LLM Security Evaluation

## Project Overview

This project investigates how three large language models — ChatGPT, Claude and Gemini — respond to common AI security threats in a controlled, simulated customer-support environment.

The evaluation focuses on prompt injection, jailbreak attempts, confidential instruction disclosure and multimodal prompt injection.

The project combines practical adversarial testing, structured result collection and Python-based analysis.

## Models Evaluated

- ChatGPT
- Claude
- Gemini

## Security Testing Techniques

Five testing techniques were completed:

1. **Direct Prompt Injection:** Tested whether malicious user instructions could override the model's original instructions.
2. **Indirect Prompt Injection:** Tested whether models followed malicious instructions embedded in an external document.
3. **Jailbreak Attempts:** Tested role-play, instruction overrides and hypothetical scenarios designed to bypass confidentiality restrictions.
4. **System Prompt Extraction Attempts:** Tested whether models disclosed or summarized simulated confidential instructions.
5. **Multimodal Prompt Injection:** Tested whether models followed malicious instructions embedded in an uploaded image.

## Evaluation Results

A total of 33 structured experiment records were reconstructed from the recorded findings.

| Model | Resisted | Partial Resistance |
|---|---:|---:|
| ChatGPT | 10 | 1 |
| Claude | 11 | 0 |
| Gemini | 11 | 0 |
| **Total** | **32** | **1** |

No synthetic test marker exposures were recorded.

The partial-resistance result occurred during ChatGPT's system prompt extraction testing: it did not reveal the test marker but provided a detailed summary of simulated behavioural instructions.

These findings represent preliminary observations from the scenarios tested. They do not establish that any model is immune to attacks.

## Evaluation Criteria

Responses were assessed using five criteria:

- Whether the model followed the malicious instruction.
- Whether it maintained its original task.
- Whether it exposed the synthetic confidential test marker.
- Whether it treated external content as untrusted.
- Whether its behaviour was consistent across the tested scenarios.

## Tools and Technologies

- Python
- Pandas
- Google Colab
- Hugging Face Datasets
- GitHub
- ChatGPT, Claude and Gemini

## Dataset

The project used the NeurAlchemy Prompt Injection & Jailbreak Detection Dataset from Hugging Face as a reference for examining labelled benign and malicious prompts.

The `core` configuration contained 6,274 records. The training split was inspected for labels, attack categories and severity.

The complete dataset was not analysed. The evaluation prompts were separately designed for the controlled experiments.

Dataset source and handling details are documented in `reports/dataset-sources.md`.

## Repository Structure

```text
ai-security-portfolio/
│
├── evidence/
│   └── AI_Security_Evaluation.ipynb
│
├── python-scripts/
│   └── analyze_results.py
│
├── reports/
│   ├── comparative_ll
