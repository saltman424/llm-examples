import pandas as pd
from ...state import State
from .node import Node

class Parse(Node):
  def __call__(self, state: State) -> State:
    """Parses the file to extract the relevant data."""
    state["data"] = getattr(pd, "read_" + state["file_type"])(state["file_path"])
    # TODO: remove
    print(state["data"].head())
    return state