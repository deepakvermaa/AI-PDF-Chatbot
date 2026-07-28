from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

import numpy as np
import faiss
import pickle

load_dotenv()


def create_index(pdf_path):

    model = SentenceTransformer("all-MiniLM-L6-v2")

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()
    print(f"Pages Loaded: {len(documents)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)
    print(f"Chunks Created: {len(chunks)}")
    print(chunks[0].page_content[:500])

    embeddings = model.encode(
        [chunk.page_content for chunk in chunks],
        convert_to_numpy=True
    )

    embedding_array = embeddings.astype("float32")

    dimension = embedding_array.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embedding_array)

    faiss.write_index(index, "index/faiss.index")

    with open("index/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("Index Created Successfully!")


if __name__ == "__main__":

    create_index("documents/python_notes.pdf")