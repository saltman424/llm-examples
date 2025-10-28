from . import graph
from .helpers import print_divider
from .state import State

# Main execution
def main():
  print("\nBeginning a choose-your-own-adventure story!")
  print_divider()
  agent = graph.create_agent()
  state = State()
  agent.invoke(state)

if __name__ == "__main__":
  main()