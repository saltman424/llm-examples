from typing import TypedDict
import pandas as pd

class State(TypedDict):
  file_path: str
  file_type: str
  prompt: str
  data: pd.DataFrame
  python: str
  summary: str
  python_error: str
  python_attempts: int
  html: str
  html_error: str
  html_attempts: int