from . import graph
from .state import State

# Main execution
def main():
  agent = graph.create_agent()
  state = State()
  agent.invoke(state)

if __name__ == "__main__":
  main()