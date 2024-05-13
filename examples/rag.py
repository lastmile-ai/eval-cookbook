"""The RAG evaluation API runs evaluation criteria (ex: faithfulness) 
    of generative AI outputs from a RAG system.

Particularly, we evaluate based on this triplet of information:

1. User query
2. Data that goes into the LLM
3. LLM's output response

The  `get_rag_eval_scores()` function returns a faithfulness score from 0 to 1.
"""

import os
import sys
from textwrap import dedent

import dotenv
import pandas as pd

from lastmile_eval.rag import get_rag_eval_scores


def main():
    rag_scores_example_1()
    rag_scores_example_2()
    return 0


def get_lastmile_api_token():
    """See README.md for mor information."""
    dotenv.load_dotenv()
    api_token = os.getenv("LASTMILE_API_TOKEN")
    assert api_token is not None
    return api_token


def rag_scores_example_1():
    print("\n\nRAG scores example 1:")
    statement1 = "the sky is red"
    statement2 = "the sky is blue"

    queries = ["what color is the sky?", "is the sky blue?"]
    data = [statement1, statement1]
    responses = [statement1, statement2]
    api_token = get_lastmile_api_token()
    result = get_rag_eval_scores(
        queries,
        data,
        responses,
        api_token,
    )

    print("Result: ", result)

    # result will look something like:
    # {'p_faithful': [0.9955534338951111, 6.857347034383565e-05]}


def rag_scores_example_2():
    print("\n\nRAG scores example 2:")
    questions = ["what is the ultimate purpose of the endpoint?"] * 2

    data1 = """
    Server-side, we will need to expose a prompt_schemas endpoint 
    which provides the mapping of model name → prompt schema 
    which we will use for rendering prompt input/settings/metadata on the client
    """

    data = [data1] * 2

    responses = ["""client rendering""", """metadata mapping"""]

    print(f"Input batch:")
    df = pd.DataFrame(
        {"question": questions, "data": data, "response": responses}
    )
    print(df)

    api_token = get_lastmile_api_token()

    result_dict = get_rag_eval_scores(
        questions,
        data,
        responses,
        api_token,
    )

    df["p_faithful"] = result_dict["p_faithful"]

    print(
        dedent(
            """
            Given a question and reference data (assumed to be factual), 
            the faithfulness score estimates whether 
            the response correctly answers the question according to the given data.
            """
        )
    )
    print("Dataframe with scores:")
    print(df)


if __name__ == "__main__":
    sys.exit(main())
