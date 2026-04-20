def research_node(state):
    topic = state["topic"]
    return {"research": f"Pesquisa sobre {topic}"}

def analysis_node(state):
    research = state["research"]
    return {"analysis": f"Análise baseada em: {research}"}

def writer_node(state):
    analysis = state["analysis"]
    return {"report": f"Relatório final:\n{analysis}"}
