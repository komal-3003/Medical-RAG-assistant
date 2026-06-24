from langchain_huggingface import HuggingFaceEmbeddings

def load_embedding_model():
    """
    Loads the BGE embedding model.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )

    return embeddings