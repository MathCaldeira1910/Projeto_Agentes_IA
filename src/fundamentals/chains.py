from .models import get_llm
from .prompts import get_basic_prompt

def run_basic_chain(tema: str):
    llm = get_llm()
    prompt = get_basic_prompt().format(tema=tema)
    response = llm.invoke(prompt)
    return response.content
