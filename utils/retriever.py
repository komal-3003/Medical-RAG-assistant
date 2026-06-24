def get_retriever(vector_db):
    """
    Creates a retriever from the FAISS vector database.
    """
    retriever = vector_db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)

    return retriever