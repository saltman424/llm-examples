import webbrowser
from ...helpers import WEBSITE_FILE
from ...state import State
from .node import Node

class OpenHtml(Node):
  def __call__(self, state: State) -> State:
    """Opens the HTML in the browser."""
    print("‣ Presenting the HTML report")
    webbrowser.open("file://" + str(WEBSITE_FILE.resolve()))
    return state