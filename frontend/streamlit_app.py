import streamlit as st
import requests
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

API_URL = os.environ.get("FRONTEND_API_URL", "http://localhost:8000")
API_KEY = os.environ.get("HACKATHON_API_KEY", "")

st.set_page_config(page_title="RAG Chat", page_icon="🤖")
st.title("Insurance DocAI: Your Insurance Policy Expert")

# --- Only Public URL mode ---
url = st.text_input("Document URL (publicly accessible)")

questions_text = st.text_area(
    "Questions (one per line)",
    placeholder="What is the policy effective date?\nWhat does Section 5 say about exclusions?"
)

if st.button("Get Answers", use_container_width=True, type="primary"):
    if not url.strip():
        st.error("Please enter a document URL.")
    elif not questions_text.strip():
        st.error("Please enter at least one question.")
    elif not API_KEY:
        st.error("HACKATHON_API_KEY not set in frontend/.env")
    else:
        questions = [q.strip() for q in questions_text.splitlines() if q.strip()]
        headers = {"Authorization": f"Bearer {API_KEY}"}
        payload = {"documents": url, "questions": questions}

        try:
            with st.spinner("Contacting backend..."):
                resp = requests.post(f"{API_URL}/hackrx/run", json=payload, headers=headers, timeout=300)
            if resp.ok:
                answers = resp.json().get("answers", [])
                for question, answer in zip(questions, answers):
                    st.markdown(f"**❓ Question:** {question}")
                    st.markdown(f"**💡 Answer:** {answer}")
            else:
                st.error(f"Backend error: {resp.status_code} {resp.text}")
        except Exception as e:
            st.error(f"Request error: {e}")
