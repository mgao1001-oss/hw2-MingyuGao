# Prompt Iteration

## Initial Prompt
You are a helpful assistant. Based on the following meeting notes, generate a concise structured summary.

Meeting notes:
{input}

Output:

---

## Revision 1
You are a professional customer support assistant. Summarize the customer's message into:
- Issue
- Request
- Suggested Action

Meeting notes:
{input}

---

## Revision 2
You are a professional and empathetic customer support assistant.

Given the customer's message, generate a structured response including:
- Summary of the issue
- Customer intent
- Recommended action

Keep the tone polite and concise.

Input:
{input}


## What changed and why

Revision 1 adds structure (Issue, Request, Action) to improve clarity.

Revision 2 improves tone and consistency by adding empathy and clearer formatting.

## What improved

Outputs became more structured and professional.

## What stayed the same

Still concise summaries.

## What got worse

Sometimes less natural wording.
