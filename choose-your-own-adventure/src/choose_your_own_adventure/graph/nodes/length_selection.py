from ...state import State
from .node import Node

class LengthSelection(Node):
  def __call__(self, state: State) -> State:
    """Selects how long the story should be."""
    user_input = input("How long would you like the story to be (e.g. tiny, short, normal, long)?\n")
    state["requested_length"] = user_input
    return state