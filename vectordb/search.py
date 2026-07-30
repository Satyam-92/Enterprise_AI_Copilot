import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load persistent ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection("books")


def search_books(query, top_k=5):
    """
    Search similar books using semantic search.
    """

    # Convert query into embedding
    query_embedding = model.encode(query).tolist()

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results