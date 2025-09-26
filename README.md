# Transformer-based Text Summarizer

This project uses state-of-the-art transformer models (BART, T5) to generate concise summaries from long-form text.

## Features
- Easy-to-use web interface (Streamlit)
- Abstractive summarization with pre-trained models
- Customizable summary length

## Getting Started

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Run the app:
    ```
    streamlit run app.py
    ```

3. Paste your text and get an instant summary!

## Customization

- Change model in `src/summarizer.py` (`facebook/bart-large-cnn`, `t5-base`, etc.)
- Adjust summary length in the web interface.

## License
MIT
