from abc import ABC, abstractmethod

from ...state import State

class Node(ABC):
  name: str

  def __init__(self):
    super().__init__()
    self.name = self.__class__.__name__

  @abstractmethod
  def __call__(self, state: State) -> State:
    pass