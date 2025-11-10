import math
import operator
import traceback
import pandas as pd
import numpy as np
from RestrictedPython import compile_restricted
from RestrictedPython.Guards import (
  guarded_iter_unpack_sequence, 
  safe_builtins,
  safer_getattr
)
from RestrictedPython.PrintCollector import PrintCollector
from ...state import State
from .node import Node

class ExecutePython(Node):
  def __call__(self, state: State) -> State:
    """Executes Python code to analyze the data."""
    python = state["python"]
    print("‣ Executing Python code to analyze the data...")
    state = execute(python, state)
    if "summary" in state:
      print("‣ Results of Python analysis:")
      print(state["summary"])
    elif "python_error" in state:
      print("‣ Encountered error:")
      print(state["python_error"])
    return state
  
def execute(code: str, state: State) -> State:
  """
  Safely execute Python code using RestrictedPython. This prevents dangerous
  operations like file I/O, network access, imports, etc.
  """
  try:
    # Compile the code with restrictions
    byte_code = compile_restricted(
      code,
      filename='<inline>',
      mode='exec'
    )

    df = state["data"].copy()
    printed = PrintCollector()

    # Set up a safe execution environment
    safe_locals = {'printed': printed}
    safe_globals_dict = {
      '__builtins__': safe_builtins,
      '__builtins__': safe_builtins,
      '__metaclass__': type,
      '__name__': 'restricted_module',
      '_apply_': lambda func, *args, **kwargs: func(*args, **kwargs),
      '_getattr_': safer_getattr,
      '_getattr_': safer_getattr,
      '_getitem_': lambda obj, k: obj[k],
      '_getiter_': guarded_iter_unpack_sequence,
      '_getiter_': guarded_iter_unpack_sequence,
      '_iadd_': operator.iadd,
      '_idiv_': operator.itruediv,
      '_imul_': operator.imul,
      '_inplacevar_': _inplacevar,
      '_isub_': operator.isub,
      '_iter_unpack_sequence_': guarded_iter_unpack_sequence,
      '_iter_unpack_sequence_': guarded_iter_unpack_sequence,
      '_print_': printed,
      'data': df,
      'df': df,
      'np': np,
      'pd': pd,
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
  
    # Execute the code
    exec(byte_code, safe_globals_dict, safe_locals)
    state["summary"] = safe_locals["result"] if "result" in safe_locals else printed.txt
    return state
 
  except Exception as e:
    state["python_error"] = f"{str(e)}\n{traceback.format_exc()}"
    return state

ops = {
  '+=': operator.iadd,
  '-=': operator.isub,
  '*=': operator.imul,
  '/=': operator.itruediv,
  '//=': operator.ifloordiv,
  '%=': operator.imod,
  '**=': operator.ipow,
  '&=': operator.iand,
  '|=': operator.ior,
  '^=': operator.ixor,
  '<<=': operator.ilshift,
  '>>=': operator.irshift,
}
def _inplacevar(op_name, x, y):
  if op_name in ops:
    return ops[op_name](x, y)
  # Fallback: try to get the operator by name from operator module
  op_func = getattr(operator, op_name.strip('_'), None)
  if op_func:
    return op_func(x, y)
  raise ValueError(f"Unknown operator: {op_name}")