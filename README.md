# hw2-
# Week 2: Build and Evaluate a Simple GenAI Workflow

## Project Overview

This project builds a simple GenAI workflow for summarizing internal meeting notes into structured action items.

The workflow is designed for a team lead or project manager who wants to turn messy meeting notes or transcript excerpts into a clear follow-up summary.

## Workflow Definition

- **Workflow chosen:** Summarizing meetings into action items
- **User:** Team lead, manager, or project coordinator
- **Input:** Raw meeting notes or transcript excerpts
- **Output:** A structured summary with key decisions, action items, owners, deadlines, risks, and follow-up questions
- **Why this task is valuable:** This task is repetitive, text-heavy, and useful to partially automate because teams often spend time manually cleaning notes after meetings

## Repository Contents

- `app.py` — Python script that calls the Gemini API and generates outputs
- `prompts.md` — initial prompt and two revisions
- `eval_set.json` — small stable evaluation set with representative test cases
- `report.md` — assignment report
- `README.md` — project summary and video link

## Setup

1. Install Python 3.9+
2. Install dependency:

```bash
pip install -U google-genai
