from langgraph.graph import StateGraph, END
from ..state import State
from . import nodes

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
    workflow.add_edge(nodes.generate_python.name, nodes.generate_html.name)
    workflow.add_edge(nodes.generate_html.name, nodes.validate_html.name)
    workflow.add_edge(nodes.validate_html.name, nodes.save_html.name)
    workflow.add_edge(nodes.save_html.name, nodes.open_html.name)
    workflow.add_edge(nodes.open_html.name, END)

    return workflow.compile()