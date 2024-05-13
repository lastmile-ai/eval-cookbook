#!/usr/bin/env python3

"""
To use the prompt iteration UI, you must implement
an executable that reads the prompt from stdin and writes
the response to stdout.

The script must return 0 on success and non-zero on failure.


This is an example of such a script.

"""


import sys


def moon_phase():
    # Mock implementation :)
    return "full"


def run_openai(prompt: str) -> str:
    if moon_phase() == "full":
        # Mock implementation :)
        return f"My name is GPT-4. How can I assist you with {prompt}?"
    else:
        raise ValueError("I can only assist you during a full moon.")


def run_my_llm(prompt: str) -> str:
    openai_response = run_openai(prompt.strip())
    return openai_response.strip()


def main(argv: list[str]) -> int:
    prompt = sys.stdin.read()
    response = run_my_llm(prompt)
    sys.stdout.write(response)
    return 0


if __name__ == "__main__":
    exit_code = main(sys.argv)
    sys.exit(exit_code)
