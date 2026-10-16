# pip install streamlit SpeechRecognition
# Requires Streamlit >= 1.39 for st.audio_input

import streamlit as st
import speech_recognition as sr

st.set_page_config(page_title="Speech to Text", page_icon="🎙️")
st.title("🎙️ Speech to Text")

languages = {
    "English": "en-IN",
    "Hindi": "hi-IN",
    "Malayalam": "ml-IN",
    "Kannada": "kn-IN",
}
lang_name = st.selectbox("Language:", list(languages.keys()))

recorded = st.audio_input("Click the mic and speak")

if st.button("Convert to Text"):
    if recorded is None:
        st.warning("Please record some audio first.")
    else:
        with st.spinner("Transcribing..."):
            try:
                recognizer = sr.Recognizer()
                recorded.seek(0)
                with sr.AudioFile(recorded) as source:
                    audio_data = recognizer.record(source)
                text = recognizer.recognize_google(
                    audio_data, language=languages[lang_name]
                )

                st.success("Done!")
                st.text_area("Transcription:", value=text, height=150)
                st.download_button(
                    label="Download Text",
                    data=text,
                    file_name="transcription.txt",
                    mime="text/plain",
                )
            except sr.UnknownValueError:
                st.error("Couldn't understand the audio. Try speaking more clearly, and make sure the selected language matches what you said.")
            except sr.RequestError as e:
                st.error(f"Could not reach Google's speech service: {e}")
            except Exception as e:
                st.error(f"Something went wrong: {e}")