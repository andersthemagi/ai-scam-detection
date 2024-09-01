import streamlit as st
from menu import menu_with_redirect

menu_with_redirect()

def text_message_1(): 
    st.subheader("Example #1")
    with st.chat_message("assistant"):
        st.markdown("""       
        Bank of America ALERT. A temporary hold has been placed on your credit card starting with 4519**. To reactivate your access, please verify your card number when you visit https://tinyurl.com/4hfj8rz2.
        """)
    text_1_choice = st.radio("Is Example #1 a scam?", ["Yes", "No", "Maybe?"], index=None)
    if text_1_choice == "Yes":
        st.success("You are correct! It is extremely unlikely your bank would be texting you about your account with a link. Chances are, you'd receive a call, or email to look at a message in a secure portal.")
    elif text_1_choice != "Yes" and text_1_choice is not None:
        st.error("This is unfortunately a scam. The link would have taken you to a website to steal your information. It is extremely unlikely your bank would be texting you about your account with a link. Chances are, you'd receive a call, or email to look at a message in a secure portal.")

def text_message_2(): 
    st.subheader("Example #2 - Text")
    with st.chat_message("assistant"):
        st.markdown("""        
        Free Msg Ent Credit Union Fraud Alert: We noticed suspicious activity on your Visa Debit Card ending in 1234 and need to review 1 transaction(s) with you.

        Available to verify now? Reply YES. If not, reply NO and we will contact you later.

        Call 866-889-9138 for assistance. Reply STOP to opt out.
        """)
    text_2_choice = st.radio("Is Example #2 a scam?", ["Yes", "No", "Maybe?"], index=None)
    if text_2_choice == "No":
        st.success("You are correct! One of our contributors received this text from their bank, and it was real. ")
    elif text_2_choice != "No" and text_2_choice is not None:
        st.error("One of our contributors received this from their bank, and it was real. Not every text providing information is a scam, but be cognizant that a malicious actor could use multiple ways in combination to try and scam you.")
    

def email_1(): 
    st.subheader("Example #3 - Email")
    with st.chat_message("assistant"):
        st.image("content/email-example-1.png")
    email_1_choice = st.radio("Is Example #3 a scam?", ["Yes", "No", "Maybe?"], index=None)
    if email_1_choice == "Yes" or email_1_choice == "Maybe?":
        st.success("You are correct! Individual users will never ask for something like this. See https://security.berkeley.edu/news/fake-duo-authentication-request for why this is a scam. ")
    elif email_1_choice == "No":
        st.error("This is a scam. See https://security.berkeley.edu/news/fake-duo-authentication-request for more information on how you can tell.")

def email_2(): 
    st.subheader("Example #4 - Email")
    with st.chat_message("assistant"):
        st.image("content/email-example-2.png")
    email_2_choice = st.radio("Is Example #4 a scam?", ["Yes", "No", "Maybe?"], index=None)
    if email_2_choice == "No":
        st.success("You are correct! Although it was marked as spam, it's a real email from a real sandwich company.")
    elif email_2_choice != "No" and email_2_choice is not None:
        st.error("This is actually real! Always err on the side of caution, but understand that sometimes real emails can be flagged as spam.")

def audio_1():
    st.subheader("Example #5 - Audio")
    with st.chat_message("assistant"):
        st.audio("content/audio-example-1.mp3")
    audio_choice = st.radio("Is Example #5 a scam?", ["Yes", "No", "Maybe?"], index=None)
    if audio_choice == "Yes":
        st.success("You are correct! Notice the intonation of the voice and the robotic way it says what it is trying to say. No real person would sound like this.")
    elif audio_choice != "Yes" and audio_choice is not None:
        st.error("This is a scam. Too robotic, and is asking for too much information. Report and move on! ")

def main():
    st.title("Scam Education Example")
    st.markdown("""
    Users should be educated on what is considered a scam, and be encouraged to do so. 
    
    This section shows rudimentary examples on how we can educate users on what is considered a scam based on our expected vectors of attack. Over time, efforts on making the process more intuitive, engaging (potentially gamification?), and user-friendly would be the priority.           
    """)
    st.write("Is this a scam? See the example and choose your answer below.")
    current_step = st.selectbox("Examples", [
        "Example #1 - Text", 
        "Example #2 - Text",
        "Example #3 - Email",
        "Example #4 - Email",
        "Example #5 - Audio"
        ""
    ])

    if current_step == "Example #1 - Text":
        text_message_1()
    
    if current_step == "Example #2 - Text":
        text_message_2()

    if current_step == "Example #3 - Email":
        email_1()

    if current_step == "Example #4 - Email":
        email_2()

    if current_step == "Example #5 - Audio":
        audio_1()

main()
