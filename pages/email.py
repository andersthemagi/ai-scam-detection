import streamlit as st
from openai import OpenAI
from menu import menu_with_redirect

emails = [
    {
        "subject": "Support Center: Tax refund",
        "sender": "Hugo Enrique osorio <hugo23_5@hotmail.com>",
        "date": "18 October 2016 at 13:34:36 BST",
        "recipient": "youremailaddress@hotmail.co.uk",
        "content": (
            "HM Revenue & Customs\n"
            "HMRC : H0928753\n\n"
            "Hello\n\n"
            "New Tax Calculation\n"
            "We have determined that you are eligible to receive a tax refund of 209.27 GBP.\n"
            "Please submit the tax refund request\n"
            "Please Click Refund and submit the tax refund request.\n\n"
            "Note: A refund can be delayed for a variety of reasons, for example submitting invalid records or applying after the deadline."
        )
    },
    {
        "subject": "Attention! Your PayPal account will close soon!",
        "sender": "support@paypal.com",
        "date": "1 September 2024 at 09:00:00 UTC",
        "recipient": "youremailaddress@example.com",
        "content": (
            "Dear Member,\n\n"
            "We have faced some problems with your account. Please update the account. If you do not update, it will be closed.\n\n"
            "To Update your account, just confirm your information. (It only takes a minute.)\n\n"
            "It's easy:\n"
            "1. Click the link below to open a secure browser window.\n"
            "2. Confirm that you're the owner of the account, and then follow the instructions.\n"
            "Relog in to your account now."
        )
    }
]

with st.sidebar:
    st.title("Email Viewer")
    
    selected_email_index = st.selectbox(
        "Select an example", 
        options=["Example 1", "Example 2"], 
        index=0
    )
    
    email_mapping = {"Example 1": 0, "Example 2": 1}
    selected_email = emails[email_mapping[selected_email_index]]
    
    st.subheader(f"Subject: {selected_email['subject']}")
    st.write(f"**From:** {selected_email['sender']}")
    st.write(f"**Date:** {selected_email['date']}")
    st.write(f"**To:** {selected_email['recipient']}")
    st.write(selected_email['content'])

st.title("Email Example")

st.text("--Consistently monitoring emails and scanning possible scams...--")

if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = (
    "You are a helpful assistant trained in identifying scams. "
    "Utilize https://scamsearch.io/ as a resource for determining whether or not something is a scam.\n\n"
    f"Here is the email I received:\n"
    f"From: {selected_email['sender']}\n"
    f"Date: {selected_email['date']}\n"
    f"To: {selected_email['recipient']}\n"
    f"Subject: {selected_email['subject']}\n\n"
    f"{selected_email['content']}\n\n"
    "Is it a scam or not? Explain how you draw the conclusion."
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

if prompt := st.chat_input("Type 're' to test or enter your first email"):
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
