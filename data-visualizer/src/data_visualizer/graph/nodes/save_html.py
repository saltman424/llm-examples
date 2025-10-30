from ...helpers import WEBSITE_FILE
from ...state import State
from .node import Node

class SaveHtml(Node):
  def __call__(self, state: State) -> State:
    """Saves the HTML."""
    html = state["html"]
    WEBSITE_FILE.parent.mkdir(exist_ok=True, parents=True)
    WEBSITE_FILE.write_text(html)
    return state