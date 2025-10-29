from ...helpers import AVAILABLE_FILE_TYPES
from ...state import State
from .node import Node

class ConfirmFileType(Node):
  def __call__(self, state: State) -> State:
    """Determines which answer is the best, if any of them."""
    file_type = state["file_type"]
    while True:
      default_file_type_info = f" (leave blank for '{file_type}')" if file_type else ""
      response = input(f"File Type{default_file_type_info}: ").lower()
      if response in AVAILABLE_FILE_TYPES:
        state["file_type"] = response
        return state
      elif response.strip() == "" and file_type:
        return state
      available_file_types_joined = ",".join(AVAILABLE_FILE_TYPES)
      print(f"Unexpected file type. Supported file types: {available_file_types_joined}. Try again.")