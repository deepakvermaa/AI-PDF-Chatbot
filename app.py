import streamlit as st
import os

from create_index import create_index
from loader import load_resources
from retrieval import retrieve_context
from generator import generate_answer


@st.cache_resource
def initialize():
    return load_resources()


client, model, index, chunks = initialize()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False

st.title("📄 AI PDF Chatbot")

with st.sidebar:
    st.title("📄 AI PDF Chatbot")

    uploaded_file = st.file_uploader(
        "Upload your PDF",
        type="pdf"
    )

    debug = st.checkbox("Show Retrieved Context")   # for showing the retrive chunks

    if uploaded_file:

        st.success("PDF uploaded successfully!")
        st.write(f"📄 {uploaded_file.name}")

        if st.button("Process PDF"):

            try:
                os.makedirs("documents", exist_ok=True)

                # for delete old files
                for file in os.listdir("documents"):
                    file_path = os.path.join("documents", file)

                    if os.path.isfile(file_path):
                        os.remove(file_path)

                with st.spinner("Creating embeddings..."):

                    pdf_path = os.path.join(
                        "documents",
                        uploaded_file.name
                    )

                    with open(pdf_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                    create_index(pdf_path)
                    initialize.clear()

                    client, model, index, chunks = initialize()
                    
                    st.session_state.messages = []  # start a new conversation if i upload new pdf
                    st.session_state.pdf_processed = True

                    st.success("PDF processed successfully!")

            
            except Exception as e:
                st.error(f"Something went wrong: {e}")

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


question = st.chat_input(
    "Ask anything from your PDF...",
    disabled=not st.session_state.pdf_processed
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            context = retrieve_context(
                question,
                model,
                index,
                chunks
            )

            # for showing the retrive chunks
            if debug:
                with st.expander("Retrieved Context"):
                    st.write(context)

            chat_history = ""

            for msg in st.session_state.messages:
                chat_history += f"{msg['role']}: {msg['content']}\n"

            try:

                answer = generate_answer(
                    client,
                    context,
                    question,
                    chat_history
                )

                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as e:
                st.error(f"Failed to generate response: {e}")

