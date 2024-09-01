import streamlit as st
from openai import OpenAI
from textblob import TextBlob
import re

# Function to analyze SMS text and highlight issues
def analyze_text(text):
    blob = TextBlob(text)
    
    # Identify potential grammatical errors (basic approach using TextBlob's part of speech tagging)
    grammar_errors = [word for word, pos in blob.tags if pos not in ['NN', 'VB', 'JJ', 'RB']]
    
    # Identify suspicious elements
    suspicious_elements = re.findall(r'http[s]?://\S+|www\.\S+', text)  # URLs
    suspicious_elements.extend(re.findall(r'\b\d{1,3}(?:,\d{3})*(?:\.\d{2})?\b', text))  # Money amounts
    
    # Identify urgent language
    urgent_phrases = []
    urgent_words = ['urgent', 'immediately', 'now', 'hurry', 'quick', 'important', 'action required', 'act now', 'limited time']
    for word in urgent_words:
        if re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE):
            urgent_phrases.append(word)
    
    return grammar_errors, suspicious_elements, urgent_phrases, blob.sentiment.polarity

# Example SMS messages
messages = [
    {
        "sender": "+447123456789",
        "date": "1 September 2024 at 09:00:00 UTC",
        "content": (
            "URGENT: Your account has been compromised. Please visit http://fakebank.com to secure your account now!"
        )
    },
    {
        "sender": "+1234567890",
        "date": "18 October 2024 at 13:34:36 BST",
        "content": (
            "Congratulations! You've won a prize of $1000. Claim it now by visiting www.prizeclaim.com!"
        )
    }
]

st.set_page_config(page_title="SMS Analyzer", layout="wide")

with st.sidebar:
    st.title("SMS Viewer")
    
    selected_message_index = st.selectbox(
        "Select an example", 
        options=["Message 1", "Message 2"], 
        index=0
    )
    
    message_mapping = {"Message 1": 0, "Message 2": 1}
    selected_message = messages[message_mapping[selected_message_index]]
    
    st.subheader(f"From: {selected_message['sender']}")
    st.write(f"**Date:** {selected_message['date']}")
    st.write(selected_message['content'])

st.title("SMS Analyzer")

st.text("--Consistently monitoring SMS messages and scanning possible scams...--")

# Analyze the SMS content
grammar_errors, suspicious_elements, urgent_phrases, sentiment = analyze_text(selected_message['content'])

# Display the analysis results
st.subheader("SMS Content Analysis")

# Display the SMS content with highlighted elements
content = selected_message['content']
for error in grammar_errors:
    content = content.replace(error, f"<span style='background-color: yellow'>{error}</span>")
for element in suspicious_elements:
    content = content.replace(element, f"<span style='background-color: #ff9999'>{element}</span>")
for phrase in urgent_phrases:
    content = content.replace(phrase, f"<span style='background-color: #ffcc99'>{phrase}</span>")

st.markdown(f"<div style='border: 1px solid #ddd; padding: 10px;'>{content}</div>", unsafe_allow_html=True)

st.write("**Legend:**")
st.markdown("- <span style='background-color: yellow'>Yellow</span>: Potential grammatical errors", unsafe_allow_html=True)
st.markdown("- <span style='background-color: #ff9999'>Red</span>: Suspicious elements (URLs, money amounts)", unsafe_allow_html=True)
st.markdown("- <span style='background-color: #ffcc99'>Orange</span>: Urgent language", unsafe_allow_html=True)

st.write(f"**Sentiment Analysis:** {'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'} (Score: {sentiment:.2f})")

if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = f"""
Please provide a concise analysis of the following SMS for potential phishing or scam characteristics. Limit your response to 3-5 sentences.

### SMS Details:
- From: {selected_message['sender']}
- Date: {selected_message['date']}
- Content: {selected_message['content']}

### Questions:
1. Is this SMS a scam or legitimate?
2. What specific indicators led you to this conclusion? (List 2-3 key points)
3. What actions should the recipient take next? (e.g., report, delete)
4. What preventive measures can the recipient take against similar scams?
"""

if not st.session_state.messages or st.session_state.messages[0]["content"] != prompt:
    st.session_state.messages = [{"role": "user", "content": prompt}]


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type 're' to reanalyze or enter your own SMS content"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

if st.button("Return to Home", type="primary"):
    st.switch_page("app.py")

