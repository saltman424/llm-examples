from ...state import State
from .node import Node

class UserChoice(Node):
  def __call__(self, state: State) -> State:
    """Gets the user input for the next step of the story."""
    user_input = input("You: ")
    state["story"] += f"\nUser: {user_input}"
    return state