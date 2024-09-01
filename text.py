import streamlit as st
from openai import OpenAI

# Sample SMS messages
sms_messages = [
    {
        "sender": "HMRC",
        "date": "18 October 2016 at 13:34:36 BST",
        "recipient": "yourphonenumber",
        "content": (
            "HMRC: H0928753\n\n"
            "Hello\n\n"
            "New Tax Calculation\n"
            "You are eligible for a tax refund of 209.27 GBP.\n"
            "Submit the tax refund request.\n\n"
            "Note: A refund can be delayed for various reasons."
        )
    },
    {
        "sender": "PayPal",
        "date": "1 September 2024 at 09:00:00 UTC",
        "recipient": "yourphonenumber",
        "content": (
            "Dear Member,\n\n"
            "Problems with your account. Update now or it will be closed.\n\n"
            "Confirm your information. It only takes a minute.\n\n"
            "1. Click the link below.\n"
            "2. Confirm your account ownership."
        )
    }
]

st.set_page_config(page_title="SMS Analyzer", layout="wide")

with st.sidebar:
    st.title("SMS Viewer")
    
    selected_sms_index = st.selectbox(
        "Select an example", 
        options=["Example 1", "Example 2"], 
        index=0
    )
    
    sms_mapping = {"Example 1": 0, "Example 2": 1}
    selected_sms = sms_messages[sms_mapping[selected_sms_index]]
    
    st.subheader(f"From: {selected_sms['sender']}")
    st.write(f"**Date:** {selected_sms['date']}")
    st.write(f"**To:** {selected_sms['recipient']}")
    st.write(selected_sms['content'])

st.title("SMS Analyzer")

st.text("--Consistently monitoring SMS messages and scanning possible scams...--")

if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = f"""
Please provide a concise analysis of the following SMS for potential phishing or scam characteristics. Limit your response to 3-5 sentences.

### SMS Details:
- From: {selected_sms['sender']}
- Date: {selected_sms['date']}
- To: {selected_sms['recipient']}
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

