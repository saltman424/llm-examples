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
  try:
    main()
  except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nMake sure:")
    print("1. Ollama is installed and running")
    print("2. You have pulled the llama3.2 model: ollama pull llama3.2")
    print("3. Required packages are installed: pip install langgraph langchain-ollama RestrictedPython")