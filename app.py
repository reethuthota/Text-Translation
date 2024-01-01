import streamlit as st
import langchain_helper
import evaluation

st.title("Text Translator")

language = st.selectbox("Pick a Language to translate into", ("English", "French"))

text = st.text_input("Enter Text to be Translated")

if language and text:
    translation = langchain_helper.generate_translation(language, text)
    translated = translation['translatedText'].strip()
    st.write(translated)
    
    similarity = evaluation.similarity(translated)
    st.write("Accuracy :",similarity)
        
# run using "streamlit run app.py"