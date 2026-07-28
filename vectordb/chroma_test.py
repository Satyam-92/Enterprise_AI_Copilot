from vectordb.chroma_db import store_embeddings

collection = store_embeddings()

print("=" * 60)
print("CHROMADB CREATED SUCCESSFULLY")
print("=" * 60)

print("Total Documents :", collection.count())