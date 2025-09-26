import nltk
from nltk.tokenize import sent_tokenize

def clean_text(text):
    # Add more sophisticated cleaning as needed
    return " ".join(sent_tokenize(text))