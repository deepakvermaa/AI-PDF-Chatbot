import os
import pickle
import faiss

from pathlib import Path
from dotenv import load_dotenv
from google import genai
from sentence_transformers import SentenceTransformer
from config import (  EMBEDDING_MODEL,INDEX_FOLDER,FAISS_FILE,CHUNKS_FILE,)


def load_gemini_client():
    load_dotenv()
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    return client

def load_embedding_model():
    model = SentenceTransformer(EMBEDDING_MODEL)
    return model

def load_faiss_index(index_path):
    index = faiss.read_index(str(index_path))
    return index

def load_chunks(chunks_path):
    with open(chunks_path, "rb") as file:
        chunks = pickle.load(file)
    return chunks


def load_resources():
    project_folder = Path(__file__).parent

    index_folder = project_folder / INDEX_FOLDER
    faiss_index_path = index_folder / FAISS_FILE
    chunks_path = index_folder / CHUNKS_FILE

    client = load_gemini_client()
    model = load_embedding_model()
    index = load_faiss_index(faiss_index_path)
    chunks = load_chunks(chunks_path)

    return client, model, index, chunks