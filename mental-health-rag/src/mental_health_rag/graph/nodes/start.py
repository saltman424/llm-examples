from ...helpers import print_divider
from ...state import State
from .node import Node

class Start(Node):
  def __call__(self, state: State) -> State:
    """Asks for the users initial query."""
    state["original_query"] = input("What would you like to know about mental health conditions?\n> ")
    print_divider()
    return state