import requests


API_URL = "http://127.0.0.1:8000/ask"


def ask_ai(question: str):
    """
    Send a question to the FastAPI backend
    and return the AI-generated answer.
    """

    try:
        response = requests.post(
            API_URL,
            json={"question": question},
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        return data["answer"]

    except requests.exceptions.RequestException as error:
        return f"Backend connection error: {error}"