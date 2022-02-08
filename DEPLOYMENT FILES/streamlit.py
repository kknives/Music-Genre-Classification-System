#!/usr/bin/env python3

from genre_rec_service import Genre_Recognition_Service
import streamlit as st

st.title("Genrify")
st.caption("Hear it. Genrify it. ")
grs = Genre_Recognition_Service()
uploaded_audio_file = st.file_uploader(
    "Choose an audio file", type=[".ogg", ".wav", ".flac"]
)
if uploaded_audio_file is not None:
    st.audio(uploaded_audio_file, format="audio/wav", start_time=0)
    prediction = ""
    with st.spinner("🎧 giving it a listen..."):
        prediction = grs.predict(uploaded_audio_file)
    prediction_message = f"""
    The song is predicted to be in the {prediction} genre.
    """
    st.success(prediction_message)
