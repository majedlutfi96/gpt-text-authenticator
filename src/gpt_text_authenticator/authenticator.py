"""The main class for the GPT Text Authenticator tool."""

from typing import Optional

from .agents import create_evaluation_agent
from .llm_factory import create_chat_model
from .schemas import AnalysisResult
from .types import Provider


class GPTTextAuthenticator:
    """The main class for the GPT Text Authenticator tool."""

    def __init__(
        self,
        provider: Provider,
        model: Optional[str] = "google",
        api_key: Optional[str] = None,
    ):
        """Initialize the GPTTextAuthenticator with a provider, model, and API key."""
        self.provider = provider
        self.model = model
        self.api_key = api_key
        self.chat_model = create_chat_model(provider, model, api_key)
        self._evaluation_agent = create_evaluation_agent(self.chat_model)

    def evaluate_text(self, text: str) -> AnalysisResult:
        """Evaluate the authenticity of the given text.

        Args:
            text: The text to evaluate.

        Returns:
            An AnalysisResult object containing the evaluation results.

        """
        results = self._evaluation_agent.invoke({"text_input": text})
        return results
