from ...helpers import print_divider
from ...state import State
from .node import Node

class Start(Node):
  def __call__(self, state: State) -> State:
    """Retrieves the initial inputs."""
    state["file_path"] = input("File: ")
    state["prompt"] = input("Prompt: ")
    print_divider()
    return state