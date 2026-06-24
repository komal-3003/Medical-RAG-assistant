import streamlit as st

from utils.pdf_loader import extract_text_from_pdf
from utils.text_splitter import split_text
from utils.embeddings import load_embedding_model
from utils.vector_store import create_vector_store
from utils.retriever import get_retriever
from utils.llm import load_llm

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Medical Document Intelligence Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================
# Sidebar
# ==========================

with st.sidebar:

    st.title("🩺 Medical AI")

    st.markdown("---")

    st.subheader("Project")

    st.info("""
            Medical Document Intelligence Assistant

            Technology Stack

            • LangChain
            • FAISS
            • BGE Embeddings
            • Ollama
            • Gemma 3
            • Streamlit
            """)

    st.markdown("---")

    st.subheader("Pipeline")

    st.success("📄 PDF Upload")
    st.success("✂ Text Chunking")
    st.success("🧠 Embeddings")
    st.success("📚 Vector Search")
    st.success("🤖 LLM Answer")

st.title("🩺 Medical Document Intelligence Assistant")

st.write(
    "Upload a medical report and ask questions about it."
)


# --------------------------------------------------
# Upload PDF
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)


# --------------------------------------------------
# Process Uploaded PDF
# --------------------------------------------------

if uploaded_file is not None:

    st.success("✅ PDF uploaded successfully!")

    # ------------------------------------------
    # Extract text from PDF
    # ------------------------------------------

    extracted_text = extract_text_from_pdf(uploaded_file)

    st.success("✅ Text extracted successfully!")

    # ------------------------------------------
    # Split text into chunks
    # ------------------------------------------

    chunks = split_text(extracted_text)

    st.success(f"✅ Text split into {len(chunks)} chunks!")

     # ------------------------------------------
    # Stats card
    # ------------------------------------------


    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📄 Chunks", len(chunks))

    with col2:
        st.metric("🤖 LLM", "Gemma 3:4B")

    with col3:
        st.metric("🧠 Embeddings", "BGE")

    with col4:
        st.metric("📚 Vector DB", "FAISS")

    # ------------------------------------------
    # Load Embedding Model
    # ------------------------------------------

    embedding_model = load_embedding_model()

    st.success("✅ Embedding model loaded!")

    # ------------------------------------------
    # Create FAISS Vector Database
    # ------------------------------------------

    vector_db = create_vector_store(
        chunks,
        embedding_model
    )

    st.success("✅ FAISS Vector Database Created!")

    # ------------------------------------------
    # Create Retriever
    # ------------------------------------------

    retriever = get_retriever(vector_db)

    st.success("✅ Retriever Created!")

    # ------------------------------------------
    # Load Gemma 3
    # ------------------------------------------

    llm = load_llm()

    st.success("✅ Gemma 3 Loaded!")


    # --------------------------------------------------
# Ask Questions
# --------------------------------------------------

st.markdown("---")

st.markdown("""
## 💬 Medical AI Assistant

Ask questions about the uploaded medical report.
""")

question = st.text_input(
    "",
    placeholder="Example: What is the patient's hemoglobin level?"
)

if question:

    with st.spinner("🧠 Analyzing medical report and retrieving relevant information..."):

        # Retrieve top relevant chunks
        docs = retriever.invoke(question)

        st.markdown("### 📚 Sources Used")

        for i, doc in enumerate(docs):

            with st.expander(f"📄 Source {i+1}"):

                st.write(doc.page_content)

        # Combine retrieved chunks
        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
        You are an experienced medical report analysis assistant.

        You must answer ONLY from the provided medical report.

        Instructions:
        1. Read the report carefully.
        2. If the question asks for a lab value, return ONLY the patient's RESULT value.
        3. Do NOT return the biological reference range unless the user specifically asks for it.
        4. Mention the unit whenever available.
        5. If the value is outside the reference range, mention that.
        6. If the information is not present, reply:
        "I could not find this information in the uploaded medical report."

        Medical Report:
        {context}

        Question:
        {question}

        Answer:
        """
        
        # st.subheader("Context Sent to Gemma")
        # st.text_area("Context", context, height=300)

        # Generate answer
        response = llm.invoke(prompt)

    st.markdown("### 🤖 AI Analysis")

    st.info(response.content)