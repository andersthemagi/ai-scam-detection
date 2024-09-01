import streamlit as st
from openai import OpenAI
from menu import menu_with_redirect

menu_with_redirect()

st.title("Audio Example")

st.markdown("""
This example will showcase a potential method of ingesting, processing, and determining whether or not an audio message is a scam.

Using OpenAI, we process the audio into a transcript, then process the transcript to determine "scamminess".     

For a full solution, we would look to use a deepfake detection API like Hive.io to provide more detailed analysis. The current solution does not account for any cadence, tone, etc. which would be indicative of an ai-generated voice as well.  
""")

if st.button("Run Demo", type="primary"):
    # Create client
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    st.session_state["openai_model"] = "gpt4o"

    audio_file = open("content/audio-example-1.mp3", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )

    with st.chat_message("user"):
        st.markdown("""
        Please turn this audio file into a transcription.         
        """)
        st.audio("content/audio-example-1.mp3")

    with st.chat_message("assistant"):
        st.write(transcription)

    with st.chat_message("user"):
        st.markdown("""
        I received this audio message from a strange caller. Is this a scam?
        """)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages=[
                {"role": "user", "content": f"""
                I received this audio message from a strange caller. Is this a scam?
                 
                {transcription}
                """}
            ],
            stream=True,
        )
        response = st.write_stream(stream)
