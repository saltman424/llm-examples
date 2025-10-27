from ...helpers import print_divider
from ...llm import llm
from ...state import State
from .node import Node

class StorySelection(Node):
  def __call__(self, state: State) -> State:
    """Selects which story to tell."""
    initial_prompt = f"You are providing a list of improvised choose-your-own-adventure stories. Give three distinct story titles in a numbered list with no other formatting:"
    response = llm.invoke(initial_prompt).content
    user_input_prompt = f"\nSuggested stories:\n{response}\n\nWhich would you like?\n"
    user_input = input(user_input_prompt)
    final_prompt = f"""You are identifying which story the user has chosen. If they have chosen from the list, only give the title they have chosen. Otherwise, give the shortest possible title or description that captures the user's desires.

{user_input_prompt}
User: {user_input}

Requested story: """
    requested_story = state["requested_story"] = llm.invoke(final_prompt).content
    print(f"\nExcellent choice! I'll begin telling you the story of:\n{requested_story}")
    print_divider()
    return state