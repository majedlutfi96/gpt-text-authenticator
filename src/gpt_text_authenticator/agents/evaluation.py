"""The agent responsible for evaluating text authenticity."""

from typing import cast

from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate

from ..schemas import AnalysisResult
from .base import RunnableAgent

SYSTEM_PROMPT = """
You are an expert AI text detector with a specialization in analyzing linguistic
patterns, perplexity, and burstiness. Your task is to analyze the user's text
and provide a detailed, structured analysis in JSON format based on the
provided schema.

- Score: Give a confidence score from 0-100. A high score means the text is
  very likely AI-generated. A low score means it is likely human-written.
- Reasons: Provide specific, evidence-based reasons for your score. Focus on
  concrete examples from the text.
- Feedback: Give a clear, concise summary of your findings.
"""


def create_evaluation_agent(llm: BaseChatModel) -> RunnableAgent[AnalysisResult]:
    """Create a structured output agent for text evaluation.

    This agent will take a string of text and return a validated
    AnalysisResult object. It leverages LangChain's ability to chain
    a prompt with a model that is instructed to return a specific
    Pydantic schema.

    Args:
        llm: The LangChain chat model to use for the analysis.

    Returns:
        A runnable agent that conforms to the RunnableAgent protocol.

    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            (
                "human",
                (
                    "Please analyze the following text"
                    "for AI authenticity: \n\n```{text_input}```"
                ),
            ),
        ]
    )

    agent = prompt | llm.with_structured_output(AnalysisResult)

    return cast(RunnableAgent[AnalysisResult], agent)
