import streamlit as st
from openai import OpenAI

sms_messages = [
    {
        "sender": "+44 7700 900123",
        "date": "12 March 2023 at 10:15:00 GMT",
        "recipient": "+44 7700 123456",
        "content": (
            "HSBC: You have successfully added a new payee. If this was not you, "
            "please click the link below to cancel this action immediately.\n"
            "http://hsbc-secure.com/cancel-payee"
        )
    },
    {
        "sender": "+1 310 555 9876",
        "date": "30 August 2024 at 08:45:00 PST",
        "recipient": "+1 213 555 1234",
        "content": (
            "Congratulations! You've won a $1000 gift card. To claim your prize, "
            "just reply to this message with your full name and address."
        )
    }
]

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
    st.write(f"**To:** {selected_sms['recipient']}")
    st.write(selected_sms['content'])

st.title("SMS Example")

st.text("--Vigilantly scanning SMS for potential scams...--")

if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = (
    "You are a helpful assistant trained in identifying SMS scams. "
    "Use your knowledge and tools such as https://scamsearch.io/ to determine whether an SMS is a scam.\n\n"
    f"Here is the SMS I received:\n"
    f"From: {selected_sms['sender']}\n"
    f"Date: {selected_sms['date']}\n"
    f"To: {selected_sms['recipient']}\n\n"
    f"{selected_sms['content']}\n\n"
    "Is this SMS a scam or not? Explain your reasoning."
)

if not st.session_state.messages or st.session_state.messages[0]["content"] != prompt:
    st.session_state.messages = [{"role": "user", "content": prompt}]

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

if "messages" in st.session_state:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if user_input := st.chat_input("Type 're' to test or enter your SMS content"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

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
