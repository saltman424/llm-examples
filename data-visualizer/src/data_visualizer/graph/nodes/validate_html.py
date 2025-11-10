from lxml import etree
from io import StringIO 
from ...state import State
from .node import Node

class ValidateHtml(Node):
  def __call__(self, state: State) -> State:
    """Validates the HTML to make sure it is correct."""
    html = state["html"]
    print("‣ Validating the HTML report...")
    if html is None:
      state["html_error"] = "Did not generate an HTML code block"
      return state
    parser = etree.HTMLParser(recover=False)
    try:
      etree.parse(StringIO(html), parser)
    except Exception as e:
      state["html_error"] = str(e)
    if "html_error" in state:
      html_error = state["html_error"]
      print(f"Identified issue: {html_error}")
    return state