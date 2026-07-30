from vectordb.search import search_books
from rag.prompt_builder import build_prompt
from rag.gemini_client import generate_answer


def ask_question(question):
    results = search_books(question)

    print("\n===== SEARCH RESULTS =====")
    print(results)

    prompt = build_prompt(question, results)

    print("\n===== PROMPT =====")
    print(prompt)

    answer = generate_answer(prompt)

    return answer