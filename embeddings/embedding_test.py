from embeddings.embedder import generate_embeddings

df = generate_embeddings()

print("=" * 80)
print("EMBEDDINGS GENERATED")
print("=" * 80)

print(df[["title", "embedding"]].head())

print("\nEmbedding Dimension:")
print(len(df["embedding"][0]))