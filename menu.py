import streamlit as st 

def menu():
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/audio.py", label="Audio Example")
    st.sidebar.page_link("pages/text.py", label="Text Example")
    st.sidebar.page_link("pages/email.py", label="Email Example")

def menu_with_redirect():
    # Once we have criteria on what information we need to run this, 
    # we may either remove this function or add client variables
    # that need to be filled before a page can be ran. 
    menu()
        