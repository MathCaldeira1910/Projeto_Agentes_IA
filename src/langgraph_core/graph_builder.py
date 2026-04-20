from langgraph.graph import StateGraph
from .state import GraphState
from .nodes import research_node, analysis_node, writer_node

def build_graph():
    builder = StateGraph(GraphState)

    builder.add_node("research", research_node)
    builder.add_node("analysis", analysis_node)
    builder.add_node("writer", writer_node)

    builder.set_entry_point("research")

    builder.add_edge("research", "analysis")
    builder.add_edge("analysis", "writer")

    return builder.compile()
