import streamlit as st
import speech_recognition as sr

def principal():
    st.title("Transcrição de audio: ")
    upload = st.file_uploader("Faça upload do arquivo de audio", type=["wav"])
    if upload is not None:
        transcrever(upload)

def transcrever (upload):
    recognizer = sr.Recognizer()
    with sr.AudioFile(upload) as source:
        st.write("processando...")
        audio = recognizer.record(source)
        texto = recognizer.recognize_google(audio,language="pt-BR")
        st.write("Texto: ",texto)
principal()
