"""Schema for text analysis results."""

from typing import List

from pydantic import BaseModel, Field


class AnalysisResult(BaseModel):
    """Schema for the result of a text authenticity analysis.

    This schema represents the structured output from the evaluation agent
    that analyzes text to determine if it was AI-generated or human-written.
    """

    score: int = Field(
        ...,
        description=(
            "Confidence score from 0-100. "
            "Higher scores indicate likely AI-generated text."
        ),
        ge=0,
        le=100,
    )

    reasons: List[str] = Field(
        ...,
        description=(
            "Specific, evidence-based reasons for the score, "
            "with concrete examples from the text."
        ),
    )

    feedback: str = Field(
        ...,
        description="A clear, concise summary of the findings.",
    )
