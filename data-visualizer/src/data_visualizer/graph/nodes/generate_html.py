from ...helpers import extract_code
from ...llm import llm
from ...state import State
from .node import Node

class GenerateHtml(Node):
  def __call__(self, state: State) -> State:
    """Generates an HTML website to summarize the data."""
    file_path = state["file_path"]
    prompt = state["prompt"]
    summary = state["summary"]
    # TODO: if there is an HTML error, include the previous HTML and error in
    # the prompt so it can be fixed
    prompt = f"""You are a web developer working with a data analyst to create a report on a dataset.

The data analyst has already analyzed the data in {file_path} and provided you with the summary data. Your goal is to create a stylish HTML report based on the summary data. The summary data is very raw, so you should use your judgement in what results to present and how. Do not just dump the raw summary data into HTML. Be thoughtful about what the user is interested in and create an appropriate report.

## Original Request
{prompt}

## Data Analyst Summary
{summary}

## Output
A standalone HTML file that presents the report in a very modern, stylish way (by including CSS in a <style> element). This file is presented in an HTML code block. This HTML code must be finalized. It is not a template. No interpolation, transformation, replacement, or other postprocessing will be done. It will be displayed exactly as is.

Here is the report:"""
    print("‣ Generating a report in HTML...")
    response = llm.invoke(prompt).content
    state["html"] = extract_code(response, "html")
    if "html_error" in state:
      del state["html_error"]
    if "html_attempts" in state:
      state["html_attempts"] += 1
    else:
      state["html_attempts"] = 1
    return state