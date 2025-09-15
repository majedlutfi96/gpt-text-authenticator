"""Custom types for the GPT Text Authenticator tool."""

from typing import Literal, TypeVar

from pydantic import BaseModel

Provider = Literal["google", "ollama"]
AgentResponse = TypeVar("AgentResponse", bound=BaseModel, covariant=True)
