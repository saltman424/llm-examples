from langgraph.graph import StateGraph, END
from ..state import State
from . import nodes

# Build the graph into an agent
def create_agent():
    """Create and compile the LangGraph workflow."""
    workflow = StateGraph(State)
    
    # Nodes
    workflow.add_node(nodes.length_selection.name, nodes.length_selection)
    workflow.add_node(nodes.story_selection.name, nodes.story_selection)
    workflow.add_node(nodes.narration_start.name, nodes.narration_start)
    workflow.add_node(nodes.user_choice.name, nodes.user_choice)
    workflow.add_node(nodes.narration_continued.name, nodes.narration_continued)
    
    # Entry point
    workflow.set_entry_point(nodes.length_selection.name)
    
    # Edges
    workflow.add_edge(nodes.length_selection.name, nodes.story_selection.name)
    workflow.add_edge(nodes.story_selection.name, nodes.narration_start.name)
    workflow.add_edge(nodes.narration_start.name, nodes.user_choice.name)
    workflow.add_edge(nodes.user_choice.name, nodes.narration_continued.name)
    workflow.add_conditional_edges(
      nodes.narration_continued.name,
      lambda state: state["finished"],
      {
        True: END,
        False: nodes.user_choice.name
      }
    )
    
    return workflow.compile()