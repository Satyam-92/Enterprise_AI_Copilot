def build_prompt(question, search_results):
    """
    Build a prompt for the LLM using retrieved documents.
    """

    documents = search_results["documents"][0]
    metadatas = search_results["metadatas"][0]

    context = ""

    for i, doc in enumerate(documents):
        context += f"""
Book {i+1}
Title: {metadatas[i]['title']}
Price: {metadatas[i]['price']}
Rating: {metadatas[i]['rating']}
Availability: {metadatas[i]['availability']}

Content:
{doc}

------------------------
"""

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the context below.

If the answer is not found in the context,
reply with:

"I don't have enough information."

==========================
CONTEXT
==========================

{context}

==========================
QUESTION
==========================

{question}

==========================
ANSWER
==========================
"""

    return prompt