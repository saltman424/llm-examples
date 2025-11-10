from ...helpers import extract_code, extract_info
from ...llm import llm
from ...state import State
from .node import Node

class GeneratePython(Node):
  def __call__(self, state: State) -> State:
    """Generates Python code to analyze the data."""
    file_path = state["file_path"]
    prompt = state["prompt"]
    data = state["data"]
    fixing_existing_code = "python_error" in state
    prompt = f"""You are a seasoned data analyst and Python developer helping prepare a report on a given dataset. Your goal is to collect all possible relevant summary statistics from the data for the presentation team to put in their report.{" You have previously tried to write Python code to accomplish this, but ended up encountering an error. You must now produce new code to either fix the error or try a new approach that avoids the error." if fixing_existing_code else ""}

## Data
{file_path}

### Structure
{extract_info(state)}

### Sample Rows
{data.head()}

### Basic Statistics
{data.describe()}

## Original Request
{prompt}"""
    if fixing_existing_code:
      python = state["python"]
      python_error = state["python_error"]
      prompt += f"""

## Previous Code
```python
{python}
```

## Error
{python_error}"""
    prompt += f"""

## Expected Output
Explain your thinking on what analysis needs to be done and then produce the Python code to achieve that analysis in a Python code block. This Python code should contain NO IMPORTS. Pandas (pd), Numpy (np), and the built-in Math library (math) have already been imported. No other libraries are available to you. A 'df' variable will already exist, and it will contain the DataFrame described above. You should create a 'result' variable which should contain your summary of the data. You can do whatever you need to with this variable to produce a useful summarization of the data. Just make sure it ends up as a string.

When creating the results, make sure to include logic to effectively handle the data. For example, you should try to handle NaN values, round numbers to a reasonable number of decimals, etc. You want a robust script to produce useful results.

NEVER print anything. The results will automatically get picked up. I repeat: do not include ANY print calls. Just generate the results.

Remember: {"you can simply fix your previous code or try entirely new code. It is up to you. The goal is get a useful summary through Python code that actually works." if fixing_existing_code else "the report is going to be based solely on your results. Make sure to include all potentially relevant summary statistics."}"""
    # Generating the code
    print("‣ Generating Python code to analyze the data...")
    response = llm.invoke(prompt).content
    state["python"] = extract_code(response, "python")
    if "python_attempts" in state:
      state["python_attempts"] += 1
    else:
      state["python_attempts"] = 1
    return state