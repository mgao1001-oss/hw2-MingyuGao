cat > app.py <<'EOF'
import os
import json
import argparse
from pathlib import Path
from google import genai

MODEL_NAME = "gemini-2.5-flash"


def load_eval_set(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_user_input(case: dict) -> str:
    return f"""
You are a business writing assistant.

Task:
Convert the following meeting notes into a structured business follow-up summary.

Required sections:
1. Main Summary
2. Confirmed Decisions
3. Action Items
4. Risks or Ambiguities
5. Open Questions
6. Human Review Needed (Yes/No, with one-sentence explanation)

Rules:
- Use only information that appears in the notes
- Never invent owners, dates, or decisions
- If information is missing or uncertain, label it clearly as "unclear" or "not confirmed"
- If the notes contain sensitive HR, legal, compliance, or incident-related content, set Human Review Needed to Yes
- Keep the tone professional and factual
- Use bullet points for Action Items

Meeting notes:
{case['input']}
""".strip()


def call_gemini(client, user_input: str) -> str:
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=user_input
    )
    return response.text if response.text else ""


def main():
    parser = argparse.ArgumentParser(description="Evaluate a simple GenAI workflow.")
    parser.add_argument("--eval", default="eval_set.json", help="Path to evaluation set JSON")
    parser.add_argument("--output_dir", default="outputs", help="Directory for outputs")
    args = parser.parse_args()

    if not os.getenv("GEMINI_API_KEY"):
        raise EnvironmentError("GEMINI_API_KEY is not set.")

    client = genai.Client()
    eval_cases = load_eval_set(args.eval)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    all_results = []

    for case in eval_cases:
        result_text = call_gemini(
            client=client,
            user_input=build_user_input(case)
        )

        result = {
            "id": case["id"],
            "input": case["input"],
            "good_output_should_do": case["good_output_should_do"],
            "model_output": result_text
        }

        all_results.append(result)

        case_file = output_dir / f"{case['id']}.md"
        with open(case_file, "w", encoding="utf-8") as f:
            f.write(f"# {case['id']}\n\n")
            f.write(f"## Input\n{case['input']}\n\n")
            f.write(f"## Good Output Should Do\n{case['good_output_should_do']}\n\n")
            f.write(f"## Model Output\n{result_text}\n")

        print("=" * 80)
        print(f"CASE: {case['id']}")
        print(result_text)
        print()

    results_file = output_dir / "results.json"
    with open(results_file, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    print(f"Saved outputs to: {output_dir}")


if __name__ == "__main__":
    main()
EOF
