from sentence_transformers import SentenceTransformer
from ml.feature_engineering import create_features

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings():
    """
    Generate sentence embeddings for book descriptions.
    """

    df = create_features()

    embeddings = model.encode(
        df["text"].tolist(),
        convert_to_numpy=True,
        show_progress_bar=True
    )

    df["embedding"] = embeddings.tolist()

    return df