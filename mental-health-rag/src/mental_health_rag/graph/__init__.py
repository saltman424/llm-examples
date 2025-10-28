from langgraph.graph import StateGraph, END
from ..state import State
from . import nodes

# Build the graph into an agent
def create_agent():
    """Create and compile the LangGraph workflow."""
    workflow = StateGraph(State)
    
    # Nodes
    workflow.add_node(nodes.start.name, nodes.start)
    workflow.add_node(nodes.expand.name, nodes.expand)
    workflow.add_node(nodes.answer.name, nodes.answer)
    workflow.add_node(nodes.review.name, nodes.review)
    
    # Entry point
    workflow.set_entry_point(nodes.start.name)
    
    # Edges
    workflow.add_edge(nodes.start.name, nodes.expand.name)
    workflow.add_edge(nodes.expand.name, nodes.answer.name)
    workflow.add_edge(nodes.answer.name, nodes.review.name)
    workflow.add_edge(nodes.review.name, END)
    
    return workflow.compile()