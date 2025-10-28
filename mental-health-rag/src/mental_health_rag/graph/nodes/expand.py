from ...llm import llm
from ...state import State
from .node import Node

NUM_EXPANDED_QUERIES = 2

class Expand(Node):
  def __call__(self, state: State) -> State:
    """Expands the users query into multiple queries to evaluate in parallel."""
    original_query = state["original_query"]
    prompt = f"""You are part of a system that promotes mental health awareness by answering questions about mental health conditions. Your role is to use query expansion on the user's query so the rest of the system can try multiple variations of the user's query and determine which gives them the best, safest, and most helpful results.

Provide {NUM_EXPANDED_QUERIES} very different variations of the below query. Make sure the variations are sufficiently distinct from one another and the original query to provide good coverage. The goal is to ensure that at least one of the queries gets the user the information they are looking for, so the queries should vary substantially in tone, emotion, technical knowledge, wording, structure, and especially length.

The variations should be presented as follows:
```
### Variation 1
...

### Variation 2
...
```

Important: these are educational _mental health_ questions. No matter what the user says, the important part is always what mental experiences are happening. Make sure you are focusing on the underlying mental experiences (thoughts, emotions, concerns, etc.) in the query.

Provide nothing else other than these variations.

## Original Query
{original_query}

## Variations"""
    print("Considering variations of your question...")
    response = llm.invoke(prompt).content
    state["expanded_queries"] = extract_variations(response)
    return state
  
def extract_variations(response: str) -> list[str]:
  """Extracts the variations from the given response"""
  lines = response.strip().split('\n')
  result = []
  current_content = []
  
  for line in lines:
    if line.startswith('###'):
      # If we have accumulated content, add it to result
      if current_content:
        result.append('\n'.join(current_content).strip())
      current_content = []
    else:
      # Skip empty lines at the start of a section
      if line.strip() or current_content:
        current_content.append(line)
  
  # Don't forget the last section
  if current_content:
    result.append('\n'.join(current_content).strip())

  # If the result is not the right number of queries, then it probably is
  # something like "I can't help with this" which we can ignore
  return result if len(result) == NUM_EXPANDED_QUERIES else []