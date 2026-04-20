from langgraph_core.graph_builder import build_graph

def run_pipeline(topic: str):
    graph = build_graph()

    result = graph.invoke({
        "topic": topic,
        "research": "",
        "analysis": "",
        "report": ""
    })

    return result["report"]
