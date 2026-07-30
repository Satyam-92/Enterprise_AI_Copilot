from vectordb.search import search_books

query = input("Enter your query: ")

results = search_books(query)

print("=" * 70)
print("Semantic Search Results")
print("=" * 70)

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

for i in range(len(documents)):
    print(f"\nResult {i+1}")
    print("-" * 40)
    print("Title :", metadatas[i]["title"])
    print("Price :", metadatas[i]["price"])
    print("Rating :", metadatas[i]["rating"])
    print("Availability :", metadatas[i]["availability"])
    print("Distance :", round(distances[i], 4))