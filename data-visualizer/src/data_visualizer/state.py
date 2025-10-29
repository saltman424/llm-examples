from typing import TypedDict
import pandas as pd

class State(TypedDict):
  file_path: str
  file_type: str
  prompt: str
  data: pd.DataFrame
  summary: str
  html: str
  html_error: str