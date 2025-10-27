from ...llm import llm
from ...state import State
from .node import Node

STORY_OVER_LINE = "THE END"

class NarrationContinued(Node):
  def __call__(self, state: State) -> State:
    """Gets the user input for the next step of the story."""
    requested_length = state["requested_length"]
    requested_story = state["requested_story"]
    story = state["story"]
    prompt = f"""You are the narrator for this choose-your-own-adventure story:
{requested_story}

Continue the story below. If you feel it is at a satisfying ending point (both in terms of narrative and length), finish the story and add one final line: "{STORY_OVER_LINE}". Otherwise, lead the story to the next choice.

Keep in mind, the user wants this story's length to be: {requested_length}

{story}
Narrator: """
    story_continuation = f"Narrator: {llm.invoke(prompt).content}"
    print(story_continuation)
    state["story"] += f"\n{story_continuation}"
    state["finished"] = state["story"].endswith(STORY_OVER_LINE)
    return state