import streamlit as st

from frontend.api import ask_ai


st.set_page_config(
    page_title="Enterprise AI Copilot",
    page_icon="🤖",
    layout="centered"
)


st.title("🤖 Enterprise AI Copilot")

st.write(
    "Ask questions about the books available in the knowledge base."
)


question = st.text_input(
    "Enter your question:",
    placeholder="Which books have a 5-star rating?"
)


if st.button("Ask AI"):

    if question.strip():

        with st.spinner("Searching knowledge base..."):

            answer = ask_ai(question)

        st.subheader("🤖 AI Answer")

        st.write(answer)

    else:

        st.warning("Please enter a question.")