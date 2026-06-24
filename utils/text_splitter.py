from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(text):
    """
    Splits extracted text into overlapping chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len
    )

    chunks = splitter.split_text(text)

    return chunks
