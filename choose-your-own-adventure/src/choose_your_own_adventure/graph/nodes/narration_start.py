from ...llm import llm
from ...state import State
from .node import Node

class NarrationStart(Node):
  def __call__(self, state: State) -> State:
    """Starts the story off."""
    requested_story = state["requested_story"]
    prompt = f"""You are the narrator for this choose-your-own-adventure story:
{requested_story}

You are starting the story and narrating all the way to the first choice.

Narrator: """
    response = llm.invoke(prompt).content
    state["story"] = f"Narrator: {response}"
    print(state["story"])
    return state