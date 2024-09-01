import streamlit as st
from openai import OpenAI

# Sample SMS messages for testing
sms_messages = [
    {
        "sender": "+44 7700 900123",
        "date": "12 March 2023 at 10:15:00 GMT",
        "content": (
            "HSBC: You have successfully added a new payee. If this was not you, "
            "please click the link below to cancel this action immediately.\n"
            "http://hsbc-secure.com/cancel-payee\n"
            "New Tax Calculation: You are eligible to receive a tax refund of 209.27 GBP. "
            "Please submit the tax refund request."
        )
    },
    {
        "sender": "+1 310 555 9876",
        "date": "30 August 2024 at 08:45:00 PST",
        "content": (
            "Congratulations! You've won a $1000 gift card. To claim your prize, "
            "reply to this message with your full name and address. "
            "We have faced some problems with your account. Please update your information."
        )
    }
]

st.set_page_config(page_title="SMS Analyzer", layout="wide")

with st.sidebar:
    st.title("SMS Viewer")
    
    selected_sms_index = st.selectbox(
        "Select an SMS example", 
        options=["Example 1", "Example 2"], 
        index=0
    )
    
    sms_mapping = {"Example 1": 0, "Example 2": 1}
    selected_sms = sms_messages[sms_mapping[selected_sms_index]]
    
    st.subheader(f"From: {selected_sms['sender']}")
    st.write(f"**Date:** {selected_sms['date']}")
    st.write(f"**Content:**\n{selected_sms['content']}")

st.title("SMS Analyzer")

st.text("--Consistently monitoring SMS messages and scanning for potential scams...--")

if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = f"""
Please provide a concise analysis of the following SMS for potential phishing or scam characteristics. Limit your response to 3-5 sentences.

### SMS Details:
- From: {selected_sms['sender']}
- Date: {selected_sms['date']}
- Content: {selected_sms['content']}

### Questions:
1. Is this SMS a scam or legitimate?
2. What specific indicators led you to this conclusion? (List 2-3 key points)
3. What actions should the recipient take next? (e.g., report, delete)
4. What preventive measures can the recipient take against similar scams?
"""

if not st.session_state.messages or st.session_state.messages[0]["content"] != prompt:
    st.session_state.messages = [{"role": "user", "content": prompt}]

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

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

