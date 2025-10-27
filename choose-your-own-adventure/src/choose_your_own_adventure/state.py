from typing import TypedDict

class State(TypedDict):
  requested_length: str
  requested_story: str
  story: str
  finished: bool = False