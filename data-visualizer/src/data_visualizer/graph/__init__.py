from langgraph.graph import StateGraph, END
from ..state import State
from . import nodes

MAX_PYTHON_ATTEMPTS = 3
MAX_HTML_ATTEMPTS = 3

# Build the graph into an agent
def create_agent():
    """Create and compile the LangGraph workflow."""
    workflow = StateGraph(State)
    
    # Nodes
    workflow.add_node(nodes.start.name, nodes.start)
    workflow.add_node(nodes.determine_file_type.name, nodes.determine_file_type)
    workflow.add_node(nodes.confirm_file_type.name, nodes.confirm_file_type)
    workflow.add_node(nodes.parse.name, nodes.parse)
    workflow.add_node(nodes.generate_python.name, nodes.generate_python)
    workflow.add_node(nodes.execute_python.name, nodes.execute_python)
    workflow.add_node(nodes.generate_html.name, nodes.generate_html)
    workflow.add_node(nodes.validate_html.name, nodes.validate_html)
    workflow.add_node(nodes.save_html.name, nodes.save_html)
    workflow.add_node(nodes.open_html.name, nodes.open_html)

    # Entry point
    workflow.set_entry_point(nodes.start.name)

    # Edges
    workflow.add_edge(nodes.start.name, nodes.determine_file_type.name)
    workflow.add_edge(nodes.determine_file_type.name, nodes.confirm_file_type.name)
    workflow.add_edge(nodes.confirm_file_type.name, nodes.parse.name)
    workflow.add_edge(nodes.parse.name, nodes.generate_python.name)
    # - Data Analysis
    workflow.add_edge(nodes.generate_python.name, nodes.execute_python.name)
    workflow.add_conditional_edges(
      nodes.execute_python.name,
      lambda state: "python_error" in state and state["python_attempts"] < MAX_PYTHON_ATTEMPTS, 
      {
        True: nodes.generate_python.name,
        False: nodes.generate_html.name
      }
    )
    # - Reporting
    workflow.add_conditional_edges(
      nodes.generate_html.name,
      lambda state: state["html_attempts"] >= MAX_HTML_ATTEMPTS, 
      {
        True: nodes.save_html.name,
        False: nodes.validate_html.name
      }
    )
    workflow.add_conditional_edges(
      nodes.validate_html.name,
      lambda state: "html_error" in state, 
      {
        True: nodes.generate_html.name,
        False: nodes.save_html.name
      }
    )
    workflow.add_edge(nodes.save_html.name, nodes.open_html.name)
    workflow.add_edge(nodes.open_html.name, END)

    return workflow.compile()