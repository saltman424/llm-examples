import pandas as pd
from ...helpers import print_divider
from ...state import State
from .node import Node

pd.set_option('display.max_columns', None)

class Parse(Node):
  def __call__(self, state: State) -> State:
    """Parses the file to extract the relevant data."""
    print_divider()
    print("‣ Loading data...")
    state["data"] = getattr(pd, "read_" + state["file_type"])(state["file_path"])
    print("‣ Data loaded:")
    print(state["data"].head())
    return state