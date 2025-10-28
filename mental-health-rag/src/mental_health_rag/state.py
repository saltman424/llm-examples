from typing import TypedDict

class State(TypedDict):
  original_query: str
  expanded_queries: list[str]
  answers: list[str]
  best_answer: str