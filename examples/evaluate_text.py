"""Example script demonstrating how to use the GPT Text Authenticator to evaluate text.

This example shows how to:
1. Initialize the authenticator with different providers
2. Evaluate text for AI authenticity
3. Work with the analysis results
"""

import os
from typing import cast

from dotenv import load_dotenv

from gpt_text_authenticator.authenticator import GPTTextAuthenticator
from gpt_text_authenticator.schemas import AnalysisResult
from gpt_text_authenticator.types import Provider


def main() -> None:
    """Run the text evaluation example."""
    # Load environment variables from .env file
    load_dotenv()

    # Get API credentials from environment variables
    provider_str = os.getenv("provider", "google")
    # Validate provider is one of the allowed values
    if provider_str not in ("google", "ollama"):
        raise ValueError(f"Invalid provider: {provider_str}.")
    provider = cast(Provider, provider_str)  # Cast to the correct type

    api_key = os.getenv("api_key")
    model = os.getenv("model", "gemini-2.5-pro")  # Default model

    # Sample texts to evaluate
    human_text = (
        "The sunset painted the sky with hues of orange and purple, "
        "a beautiful backdrop as I walked along the beach. The waves "
        "crashed against the shore, a rhythmic sound that always "
        "brings me peace."
    )

    ai_text = (
        "The implementation of quantum algorithms necessitates a comprehensive "
        "understanding of both quantum mechanics and computational theory. "
        "The efficiency of these algorithms is predicated on the exploitation "
        "of quantum phenomena such as superposition and entanglement."
    )

    # Initialize the authenticator
    print(f"Initializing authenticator with provider: {provider}, model: {model}")
    authenticator = GPTTextAuthenticator(provider, model, api_key)

    # Evaluate human-written text
    print("\n--- Evaluating potentially human-written text ---")
    human_result = authenticator.evaluate_text(human_text)
    print_result(human_result, human_text)

    # Evaluate AI-generated text
    print("\n--- Evaluating potentially AI-generated text ---")
    ai_result = authenticator.evaluate_text(ai_text)
    print_result(ai_result, ai_text)


def print_result(result: AnalysisResult, text: str) -> None:
    """Print the analysis result in a readable format.

    Args:
        result: The analysis result from the authenticator
        text: The text that was analyzed

    """
    print(f"Text: {text[:50]}...")
    print(f"AI Score: {result.score}/100")
    print("Reasons:")
    for i, reason in enumerate(result.reasons, 1):
        print(f"  {i}. {reason}")
    print(f"Feedback: {result.feedback}")

    # Classification based on score
    if result.score < 30:
        classification = "Likely human-written"
    elif result.score > 70:
        classification = "Likely AI-generated"
    else:
        classification = "Uncertain origin"

    print(f"Classification: {classification}")


if __name__ == "__main__":
    main()
