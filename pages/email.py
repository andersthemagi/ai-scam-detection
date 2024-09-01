import streamlit as st
from openai import OpenAI

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

st.set_page_config(page_title="Email Analyzer", layout="wide")

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

st.title("Email Analyzer")

st.text("--Consistently monitoring emails and scanning possible scams...--")

if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = f"""
Please provide a concise analysis of the following email for potential phishing or scam characteristics. Limit your response to 3-5 sentences.

### Email Details:
- From: {selected_email['sender']}
- Date: {selected_email['date']}
- To: {selected_email['recipient']}
- Subject: {selected_email['subject']}
- Content: {selected_email['content']}

### Questions:
1. Is this email a scam or legitimate?
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

if prompt := st.chat_input("Type 're' to reanalyze or enter your own email content"):
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

