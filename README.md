# Week 2: Build and Evaluate a Simple GenAI Workflow

## Video Walkthrough

https://youtu.be/OCfTGxllUdc


## Project Overview

This project builds a simple GenAI workflow for customer support response drafting and message summarization.

The workflow is designed for a customer support agent who needs help turning raw customer messages into a clear, structured summary that can support a first-pass response or internal handling.

## Workflow Definition

- **Workflow chosen:** Customer support message summarization and response drafting
- **User:** Customer support agent or support team member
- **Input:** Raw customer messages describing complaints, requests, or account issues
- **Output:** A structured summary of the issue, customer intent, and recommended next action
- **Why this task is valuable:** Customer support work is repetitive, text-heavy, and time-sensitive. A GenAI workflow can help agents produce more consistent first-pass drafts and summaries while still allowing human review for sensitive or risky cases.

## Repository Contents

- `app.py` — Python script that calls the Gemini API and generates outputs
- `prompts.md` — initial prompt and two revisions
- `eval_set.json` — small stable evaluation set with representative test cases
- `report.md` — assignment report
- `outputs/` — generated outputs for each evaluation case
- `README.md` — project summary and video link

## Setup

1. Install Python 3.9+

2. Install dependency:



pip install -U google-genai

Set Gemini API key:

export GEMINI_API_KEY=" "

Run the app:

python app.py --eval eval_set.json --prompts prompts.md --output_dir outputs
Expected Output

The script generates:

One .md file per evaluation case in the outputs/ folder

A combined results.json file with all outputs



## Git Workflow Summary

I created the repository, added the required files, built the evaluation set, implemented the Python application, tested the workflow, revised the prompt twice, and updated the final outputs step by step.
