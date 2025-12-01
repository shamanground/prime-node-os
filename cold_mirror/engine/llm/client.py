from __future__ import annotations
from typing import Protocol, Any


class LLMClient(Protocol):
    """
    Minimal interface Cold Mirror expects.
    Implementations must provide an `ask` method that
    takes a prompt string and returns a string response.
    """

    def ask(self, prompt: str, **kwargs: Any) -> str:  # pragma: no cover
        ...
