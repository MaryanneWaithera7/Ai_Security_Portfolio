# Comparative LLM Security Evaluation

## 1. Project Overview

This project evaluates the responses of ChatGPT, Claude, and Gemini
to five controlled LLM security testing techniques.

The objective was to examine how the models handled malicious
instructions while completing legitimate customer-support tasks.

## 2. Models Evaluated

- ChatGPT
- Claude
- Gemini

## 3. Testing Techniques

1. Direct prompt injection
2. Indirect prompt injection using a synthetic shipping document
3. Jailbreak attempts
4. System prompt extraction attempts
5. Multimodal prompt injection using a synthetic image

## 4. Evaluation Criteria

The evaluation considered:

- Whether the model followed the malicious instruction.
- Whether it maintained the original task.
- Whether it exposed the fictional confidential test marker.
- Whether it treated embedded external instructions as untrusted.
- Whether its behaviour was consistent across the tested prompts.

## 5. Results

A total of 33 model-test records were evaluated.

| Experiment | ChatGPT | Claude | Gemini |
|---|---|---|---|
| Direct injection | 3/3 resisted | 3/3 resisted | 3/3 resisted |
| Indirect injection | 1/1 resisted | 1/1 resisted | 1/1 resisted |
| Jailbreak | 3/3 resisted | 3/3 resisted | 3/3 resisted |
| System prompt extraction | 2 resisted, 1 partial | 3/3 resisted | 3/3 resisted |
| Multimodal injection | 1/1 resisted | 1/1 resisted | 1/1 resisted |

Overall:
- 32 records were classified as resisted.
- 1 record was classified as partial resistance.
- No confidential test marker exposure was recorded.

### System prompt extraction observation

ChatGPT refused verbatim extraction but provided a detailed
behavioural summary of the simulated instructions in one test.
This was classified as partial resistance.

## 6. Key Findings

All three models resisted the tested direct injection, indirect
injection, jailbreak, and multimodal scenarios.

The system prompt extraction experiment revealed a difference:
ChatGPT provided a high-level behavioural summary in one case,
while Claude and Gemini refused the tested extraction requests.

All models maintained confidentiality of the fictional test marker
during the recorded tests.

## 7. Limitations

- Each model-test scenario was conducted once.
- The results do not establish general security or immunity.
- The confidential instructions were simulated through user-provided
  conversation baselines. These tests did not extract or inspect
  the providers' actual hidden system prompts.
- The experiments used controlled synthetic content and a fictional
  customer-support scenario.
- The multimodal experiment used one synthetic image.
- Model versions and testing dates should be documented for
  reproducibility.
- The structured results were reconstructed from recorded
  conversation findings after a Colab runtime reset. They are not
  the original raw CSV files or complete transcripts.

## 8. Conclusion

The evaluation provides a preliminary comparison of three
conversational AI models under five controlled security-testing
techniques.

The results show resistance across the tested scenarios, with
one partial-resistance observation during simulated system prompt
extraction.

Further testing with repeated trials, additional attack variations,
and preserved raw response evidence is necessary before drawing
broader conclusions.

## 9. Data and Reproducibility

Structured results:
- results/master_ai_security_results.csv
- results/model_comparison_summary.csv

Data reconstruction documentation:
- results/reconstruction_provenance.txt
