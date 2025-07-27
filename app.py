import streamlit as st
import requests

# Set title
st.set_page_config(page_title="Youssef Hazem Chatbot", layout="centered")
st.title(" Youssef Hazem Chatbot")

# Sidebar content
with st.sidebar:
    st.header("About")
    st.write("Chatbot using FastAPI + Together AI")
    if st.button("🧹 Clear Chat"):
        st.session_state.chat_history = []

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# API URL
url = "http://127.0.0.1:8000/llm/"

# User input
query = st.text_input("Enter your question:")

# If query submitted
if query:
    payload = {"query": query}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        bot_response = response.json().get("answer", "⚠️ No response from model.")
    except Exception as e:
        bot_response = f"❌ Error: {e}"

    # Store in history
    st.session_state.chat_history.append(("User", query))
    st.session_state.chat_history.append(("Bot", bot_response))

# Show chat history
for role, message in st.session_state.chat_history:
    if role == "User":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")
