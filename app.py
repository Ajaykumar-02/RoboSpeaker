import streamlit as st
from gtts import gTTS
import tempfile

st.set_page_config(
    page_title="RoboSpeaker",
    page_icon="🎤",
    layout="centered"
)

st.title("🎤 RoboSpeaker")
st.write("Convert Text into Speech and Download Audio")

text = st.text_area(
    "Enter Text",
    height=150,
    placeholder="Type something here..."
)

language = st.selectbox(
    "🌍 Select Language",
    [
        "English",
        "Hindi",
        "French",
        "Spanish",
        "German"
    ]
)

language_map = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

if st.button("🔊 Generate Speech"):

    if text.strip():

        tts = gTTS(
            text=text,
            lang=language_map[language]
        )

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        )

        tts.save(temp_file.name)

        st.success("✅ Audio Generated Successfully!")

        st.audio(temp_file.name)

        with open(temp_file.name, "rb") as audio_file:

            st.download_button(
                label="📥 Download Audio",
                data=audio_file.read(),
                file_name="speech.mp3",
                mime="audio/mp3"
            )

    else:

        st.warning("⚠️ Please enter some text.")





'''
from gtts import gTTS

text = "Hello Ajay, welcome to Python."

tts = gTTS(
    text=text,
    lang="en"
)

tts.save("speech.mp3")

'''        