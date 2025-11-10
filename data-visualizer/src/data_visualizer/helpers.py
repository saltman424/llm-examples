import re
import io
from pathlib import Path
import pandas as pd
from .state import State

AVAILABLE_FILE_TYPES = [ key.removeprefix("read_") for key in pd.__dict__.keys() if key.startswith("read_") ]

WEBSITE_FILE = Path(__file__).parent.parent.parent / 'dist/index.html'

def print_divider():
  print("=" * 60)

def extract_info(state: State) -> str:
  df = state["data"]
  buffer = io.StringIO()
  df.info(buf=buffer)
  return buffer.getvalue()

def extract_code(response: str, language: str | list[str] = None) -> str:
    """
    Extracts the desired code block from the response
    """    
    # Build pattern for specific languages if provided
    if language is not None:
      if isinstance(language, str):
        languages = [language]
      else:
        languages = language
      
      # Try to find code blocks with the specified language(s)
      for lang in languages:
        pattern = rf"```{re.escape(lang)}\n(.*?)```"
        match = re.search(pattern, response, re.DOTALL)
        if match:
            return match.group(1).strip()
  
    # Fall back to finding any code block (``` followed by optional language, then newline)
    pattern = r"```(?:\w+)?\n(.*?)```"
    match = re.search(pattern, response, re.DOTALL)
    if match:
      return match.group(1).strip()
    
    # Last resort: assumes the whole response is the code
    return response