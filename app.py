import os
import json
import argparse
from pathlib import Path
from google import genai

MODEL_NAME = "gemini-3-flash-preview"

def load_eval_set(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def call_gemini(client, prompt):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text

def build_user_input(case):
    return f"""
You are a helpful assistant. Based on the following meeting notes, generate a concise structured summary.

Meeting notes:
{case["input"]}

Output:
"""

def main():
    parser = argparse.ArgumentParser(description="Evaluate a simple GenAI workflow.")
    parser.add_argument("--eval", default="eval_set.json")
    parser.add_argument("--output_dir", default="outputs")
    args = parser.parse_args()

    if not os.getenv("GEMINI_API_KEY"):
        raise EnvironmentError("GEMINI_API_KEY is not set.")

    client = genai.Client()

    eval_cases = load_eval_set(args.eval)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    all_results = []

    for case in eval_cases:
        prompt = build_user_input(case)
        result_text = call_gemini(client, prompt)

        result = {
            "id": case["id"],
            "input": case["input"],
            "expected": case["expected"],
            "model_output": result_text
        }

        all_results.append(result)

        case_file = output_dir / f"{case['id']}.md"
        with open(case_file, "w", encoding="utf-8") as f:
            f.write(f"# {case['id']}\n\n")
            f.write(f"## Input\n{case['input']}\n\n")
            f.write(f"## Expected\n{case['expected']}\n\n")
            f.write(f"## Model Output\n{result_text}\n")

        print("=" * 60)
        print(f"CASE: {case['id']}")
        print(result_text)
        print()

    results_file = output_dir / "results.json"
    with open(results_file, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    print(f"Saved outputs to: {output_dir}")

if __name__ == "__main__":
    main()
