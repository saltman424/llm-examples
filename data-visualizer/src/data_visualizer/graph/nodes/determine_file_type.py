from ...helpers import AVAILABLE_FILE_TYPES
from ...llm import llm
from ...state import State
from .node import Node

class DetermineFileType(Node):
  def __call__(self, state: State) -> State:
    """Determines the appropriate file type based on the file name."""
    file_path = state["file_path"]
    prompt = f"""You are attempting to determine the file type of this file: {file_path}

You are only allowed to return one of these types: {",".join(AVAILABLE_FILE_TYPES)}

Make your best guess. ONLY return one word, the file type itself. Put NOTHING else.

File type:"""
    file_type = llm.invoke(prompt).content.lower()
    state["file_type"] = file_type if file_type in AVAILABLE_FILE_TYPES else None
    return state