from ...helpers import extract_html
from ...llm import llm
from ...state import State
from .node import Node

class GenerateHtml(Node):
  def __call__(self, state: State) -> State:
    """Generates an HTML website to summarize the data."""
    file_path = state["file_path"]
    prompt = state["prompt"]
    summary = state["summary"]
    prompt = f"""You are a web developer working with a data analyst to create a report on a dataset.

The data analyst has already analyzed the data in {file_path} and provided the below summary. Your goal is to take that summary and create a stylish HTML report to present the information.

## Original Request
{prompt}

## Data Analyst Summary
{summary}

## Output
A standalone HTML file that presents the report in a very modern, stylish way. This file is presented in an HTML code block.

Here is the report:"""
    response = llm.invoke(prompt).content
    state["html"] = extract_html(response)
    return state