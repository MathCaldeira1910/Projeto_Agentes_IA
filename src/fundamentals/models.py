from langchain_groq import ChatGroq
import os

def get_llm():
    return ChatGroq(
        model="llama3-70b-8192",
        api_key=os.getenv("GROQ_API_KEY")
    )
