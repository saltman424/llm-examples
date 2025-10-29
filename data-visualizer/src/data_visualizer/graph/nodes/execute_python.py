import math
import sys
from io import StringIO
from RestrictedPython import compile_restricted
from RestrictedPython.Guards import guarded_iter_unpack_sequence, safe_builtins
from ...helpers import print_divider
from ...llm import llm
from ...state import State
from .node import Node

class Summarize(Node):
  def __call__(self, state: State) -> State:
    """Determines which answer is the best, if any of them."""
    file_path = state["file_path"]
    data = state["data"]
    prompt = state["prompt"]
    prompt = f"""You are a seasoned data analyst and Python developer helping prepare a report on a given dataset. Your goal is to collect relevant summary statistics from the data for another analyst to use in their report.

You are analyzing: {file_path}.

You 
    """
    review = llm.invoke(prompt).content
    state["summary"] = 
    return state
  
def execute(code: str) -> str:
  """
  Safely execute Python code using RestrictedPython.
  This prevents dangerous operations like file I/O, network access, imports, etc.
  """
  try:
    # Compile the code with restrictions
    byte_code = compile_restricted(
      code,
      filename='<inline>',
      mode='exec'
    )
    
    # Set up a safe execution environment
    safe_locals = {}
    safe_globals_dict = {
      '__builtins__': safe_builtins,
      '_getiter_': guarded_iter_unpack_sequence,
      '_iter_unpack_sequence_': guarded_iter_unpack_sequence,
      # Allow safe mathematical operations
      'math': math,
      'math': math,
      'abs': abs,
      'round': round,
      'min': min,
      'max': max,
      'sum': sum,
      'len': len,
      'range': range,
      'enumerate': enumerate,
      'zip': zip,
      'sorted': sorted,
      'list': list,
      'dict': dict,
      'set': set,
      'tuple': tuple,
      'str': str,
      'int': int,
      'float': float,
      'bool': bool,
    }

    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
  
    try:
      # Execute the code
      exec(byte_code, safe_globals_dict, safe_locals)

      # Get the output
      output = captured_output.getvalue()

      # If there's a result variable, include it
      if 'result' in safe_locals:
          output += f"\nResult: {safe_locals['result']}"

      return output

    finally:
      sys.stdout = old_stdout
          
  except Exception as e:
      return f"Error executing code: {str(e)}"