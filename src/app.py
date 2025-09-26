import streamlit as st
from summarizer import TextSummarizer
from preprocessing import clean_text

st.title("Transformer-based Text Summarizer")

text_input = st.text_area("Paste your text here:")

if st.button("Summarize"):
    if text_input.strip():
        cleaned = clean_text(text_input)
        summarizer = TextSummarizer()
        summary = summarizer.summarize(cleaned)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.write("Please enter some text to summarize.")