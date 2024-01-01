import streamlit as st
import langchain_helper
import evaluation

st.title("Text Translator")

from_language = st.selectbox("Translate from", ("English", "French"))
to_language = st.selectbox("Translate to", ("English", "French"))

if from_language == to_language:
    st.warning("Please select different languages for translation.")
    st.stop()

text = st.text_input("Enter Text to be Translated")

if from_language and to_language and text:
    translated = langchain_helper.generate_translation(to_language, text)
    st.write(translated['translatedText'].strip())

    similarity = evaluation.similarity(translated['translatedText'].strip())
    st.write("Accuracy:", similarity)
