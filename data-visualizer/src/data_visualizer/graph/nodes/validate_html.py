from lxml import etree
from io import StringIO 
from ...state import State
from .node import Node

class ValidateHtml(Node):
  def __call__(self, state: State) -> State:
    """Validates the HTML to make sure it is correct."""
    html = state["html"]
    parser = etree.HTMLParser(recover=False)
    try:
      etree.parse(StringIO(html), parser)
    except Exception as e:
      state["html_error"] = str(e)
    return state