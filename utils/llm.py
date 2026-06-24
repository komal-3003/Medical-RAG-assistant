from langchain_ollama import ChatOllama

def load_llm():
    """
    Loads the local Gemma 3 model using Ollama.
    """

    llm = ChatOllama(
    model="gemma3:4b",
    temperature=0
    )

    return llm
