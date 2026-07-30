from vectordb.search import search_books
from rag.prompt_builder import build_prompt
from rag.gemini_client import generate_answer


def ask_question(question: str):
    search_results = search_books(question)

    prompt = build_prompt(question, search_results)

    answer = generate_answer(prompt)

    return answer