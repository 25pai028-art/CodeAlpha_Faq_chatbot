import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page Configuration
st.set_page_config(
    page_title="Pet Food FAQ Assistant",
    page_icon="🐶",
    layout="centered"
)

# FAQ Dataset
faq = pd.DataFrame({
    "question": [
        "What ingredients are used in the pet food?",
        "Is this food suitable for puppies?",
        "How should I store the pet food?",
        "Do you offer grain free options?",
        "How much food should I feed my dog?",
        "Is the food suitable for cats?",
        "What is the shelf life of the product?",
        "Do you provide home delivery?"
    ],
    "answer": [
        "Our pet food contains chicken, rice, vegetables, and essential vitamins.",
        "Yes, we have special formulas designed specifically for puppies.",
        "Store the food in a cool, dry place and keep the package sealed.",
        "Yes, we offer grain-free pet food options.",
        "Please follow the feeding guide on the package according to your dog's weight.",
        "We offer separate formulas specially designed for cats.",
        "The shelf life is typically 12 months from the manufacturing date.",
        "Yes, we provide home delivery services."
    ]
})

# Title
st.title("🐶 Pet Food FAQ Assistant")
st.write("Ask any question about our pet food products.")

# TF-IDF Model
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(faq["question"])

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat Function
def get_answer(user_question):
    user_vector = vectorizer.transform([user_question])

    similarity_scores = cosine_similarity(
        user_vector,
        faq_vectors
    )

    best_index = similarity_scores.argmax()
    best_score = similarity_scores[0][best_index]

    if best_score < 0.2:
        return "Sorry, I couldn't find a relevant answer."

    return faq.iloc[best_index]["answer"]

# User Input
user_input = st.text_input(
    "Enter your question:",
    placeholder="Example: Is this food suitable for puppies?"
)

if st.button("Send") and user_input:
    answer = get_answer(user_input)

    st.session_state.messages.append(
        {"role": "user", "text": user_input}
    )

    st.session_state.messages.append(
        {"role": "bot", "text": answer}
    )

# Display Chat
for msg in st.session_state.messages:

    if msg["role"] == "user":
        st.markdown(
            f"""
            <div style="
                background:#E3F2FD;
                padding:10px;
                border-radius:10px;
                margin:5px 0;">
                <b>👤 You:</b> {msg["text"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f"""
            <div style="
                background:#E8F5E9;
                padding:10px;
                border-radius:10px;
                margin:5px 0;">
                <b>🤖 Assistant:</b> {msg["text"]}
            </div>
            """,
            unsafe_allow_html=True
        )

# Sidebar
st.sidebar.title("🐾 Pet Food Support")
st.sidebar.markdown("""
### Sample Questions
- What ingredients are used?
- Is this food suitable for puppies?
- Do you offer grain free options?
- How should I store the food?
- Do you provide home delivery?
""")