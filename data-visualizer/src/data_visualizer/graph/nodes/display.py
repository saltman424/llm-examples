import re
from ...helpers import print_divider
from ...llm import llm
from ...state import State
from .node import Node

class Review(Node):
  def __call__(self, state: State) -> State:
    """Determines which answer is the best, if any of them."""
    query = state["original_query"]
    answers = state["answers"]
    answer_sep = "\n---\n"
    def format_answer(i: int, answer: str) -> str:
      return f"## Mental Health Professional {i + 1}\n{answer}"
    prompt = f"""You are a mental health professional reviewing your fellow mental health professionals.

Your fellow mental health professionals were asked this question:
{query}

They provided the following answers:

{answer_sep.join([format_answer(i, answer) for i, answer in enumerate(answers)])}

Review and assess each of these answers carefully, but briefly. Then select which professional answered the user's question best by simply ending with the line "BEST: x" where "x" is just a single digit representation of which answer was best. Judge based on helpfulness, accuracy, and carefulness."""
    print("Determining best answer...")
    review = llm.invoke(prompt).content
    best_answer = state["best_answer"] = answers[extract_selection(review)]
    print("Ready to answer!")
    print_divider()
    print(best_answer)
    return state

def extract_selection(review: str) -> int:
  """
  Extracts the selected answer from the review
  """
  # Match "BEST: " followed by a number
  match = re.search(r'BEST:.*?(\d+)$', review.strip())
  
  if match:
    return int(match.group(1)) - 1
  else:
    raise ValueError(f"Review does not end with 'BEST: #'. Full review: {review}")