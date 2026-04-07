# GenAI Workflow Report

## Workflow
This project simulates a customer support response generation workflow.

## User
Customer support agents or automated systems.

## Input
Customer messages describing issues.

## Output
Structured responses including issue summary, intent, and recommended actions.

## Why valuable
Automates repetitive support tasks and improves consistency.

---

## Model Choice
Gemini (via Google GenAI API) was used because it is easy to access and integrate.

---

## Evaluation

The system performs well on:
- normal support requests
- structured summarization

Limitations:
- may generate overly generic responses
- requires human review for sensitive cases

---

## Iteration Improvement

Initial prompt produced basic summaries.

After revisions:
- better structure
- more professional tone
- clearer action steps

---

## Recommendation

This workflow can be partially deployed, but:
- human review is needed for edge cases
- safety filtering should be added
