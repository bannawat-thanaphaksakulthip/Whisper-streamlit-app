import whisper
import streamlit as st
import tempfile

model = whisper.load_model("tiny")
st.markdown("# Speech To Text.")
uploaded_file = st.file_uploader("Upload your file", type=["m4a"])
st.audio(uploaded_file)

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".m4a") as tmp:
        tmp.write(uploaded_file.read())
        result = model.transcribe(tmp.name)
    st.write("Detected language:",result["language"])
    st.text_area("Result", result["text"], height=200)