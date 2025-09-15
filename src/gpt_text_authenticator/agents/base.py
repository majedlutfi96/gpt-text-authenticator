"""Base definitions and protocols for all agents."""

from typing import Any, Protocol, runtime_checkable

from langchain_core.runnables import RunnableConfig

from ..types import AgentResponse


@runtime_checkable
class RunnableAgent(Protocol[AgentResponse]):
    """A generic protocol defining the common interface for all agents."""

    def invoke(
        self,
        input: dict[str, Any],
        config: RunnableConfig | None = None,
        **kwargs: Any,
    ) -> AgentResponse:
        """Invoke the agent with the given input.

        This signature is compatible with LangChain's standard Runnable interface.

        Args:
            input: The input data for the agent, typically a dictionary.
            config: An optional runtime configuration for the agent.
            **kwargs: Additional keyword arguments.

        Returns:
            A specific Pydantic model instance, defined by the TypeVar.

        """
        ...
