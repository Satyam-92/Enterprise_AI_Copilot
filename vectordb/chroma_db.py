import chromadb

from embeddings.embedder import generate_embeddings


client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="books"
)


def store_embeddings():

    df = generate_embeddings()

    collection.add(

        ids=[str(i) for i in range(len(df))],

        documents=df["text"].tolist(),

        embeddings=df["embedding"].tolist(),

        metadatas=[

            {
                "title": row["title"],
                "price": float(row["price"]),
                "rating": int(row["rating"]),
                "availability": row["availability"]

            }

            for _, row in df.iterrows()

        ]

    )

    return collection