"""A factory for creating langchain models."""

from typing import Optional

from langchain_core.language_models import BaseChatModel

from gpt_text_authenticator.types import Provider


def create_chat_model(
    provider: Provider = "google",
    model: Optional[str] = None,
    api_key: Optional[str] = None,
) -> BaseChatModel:
    """Create a chat model based on the provider and model name.

    Args:
        provider: The provider to use for the chat model.
        model: The name of the model to use.
        api_key: The API key to use for authentication with the provider.

    Returns:
        A BaseChatModel instance.

    Raises:
        ValueError: If the provider is not supported.
        ValueError: If the API key is not provided for the providers that require it.

    """
    if not api_key and provider != "ollama":
        raise ValueError("API key is required for the provider")

    match provider:
        case "google":
            from langchain_google_genai import ChatGoogleGenerativeAI

            return ChatGoogleGenerativeAI(
                model=model,
                api_key=api_key,
            )
        case _:
            raise ValueError(f"Unsupported provider: {provider}")
