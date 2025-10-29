from pathlib import Path
import pandas as pd

AVAILABLE_FILE_TYPES = [ key.removeprefix("read_") for key in pd.__dict__.keys() if key.startswith("read_") ]

WEBSITE_FILE = Path(__file__).parent.parent.parent / 'dist/index.html'

def print_divider():
  print("=" * 60)

def extract_html(response: str) -> int:
  """
  Extracts the HTML content from the response
  """
  for code_block_start in ["```html", "```"]:
    if code_block_start in response:
      return response.split(code_block_start)[1].split("```")[0].strip()