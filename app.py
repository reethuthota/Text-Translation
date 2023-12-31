import streamlit as st
import langchain_helper

st.title("Text Translator")

language = st.selectbox("Pick a Language to translate into", ("English", "French"))

text = st.text_input("Enter Text to be Translated")

if language and text:
    response = langchain_helper.generate_translation(language, text)
    translated = response['translatedText'].strip()
    st.write(translated)
        
# run using "streamlit run app.py"