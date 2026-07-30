from rag.rag_pipeline import ask_question

question = input("Ask a question: ")

answer = ask_question(question)

print("\n" + "=" * 80)
print("AI Answer:\n")
print(answer)