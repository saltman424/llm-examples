import re
from ...helpers import AVAILABLE_FILE_TYPES
from ...llm import llm
from ...state import State
from .node import Node

class DetermineFileType(Node):
  def __call__(self, state: State) -> State:
    """Determines the appropriate file type based on the file name."""
    file_path = state["file_path"]
    for approach in [determine_by_extension, determine_with_llm]:
      file_type = approach(file_path)
      if file_type in AVAILABLE_FILE_TYPES:
        state["file_type"] = file_type
        break
    return state

def determine_by_extension(file_path: str) -> str | None:
  pattern = r"\.(.+)$"
  match = re.search(pattern, file_path, re.DOTALL)
  if match:
    return match.group(1).strip()

def determine_with_llm(file_path: str) -> str | None:
  prompt = f"""You are attempting to determine the file type of this file: {file_path}

You are only allowed to return one of these types: {",".join(AVAILABLE_FILE_TYPES)}

Make your best guess. ONLY return one word, the file type itself. Put NOTHING else.

File type:"""
  return llm.invoke(prompt).content.lower()