import streamlit as st
from langdetect import detect
from PyPDF2 import PdfReader
import docx
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer  # or LexRankSummarizer, LuhnSummarizer

# ---------------------------
# Helper functions
# ---------------------------
import nltk
nltk.download('punkt_tab')

def extract_text(file):
    if file.type == "application/pdf":
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
        return text
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        return " ".join([para.text for para in doc.paragraphs])
    elif file.type == "text/plain":
        return file.read().decode("utf-8")
    else:
        return None

def detect_language(text):
    try:
        return detect(text)
    except:
        return "Unknown"

def count_words(text):
    return len(text.split())

def summarize_text(text, sentence_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("📝 Offline Text & Document Summarizer (No OpenAI)")

input_option = st.radio("Choose input type:", ["Upload Document", "Enter Text"])

summary_length = st.slider("Number of summary sentences", min_value=1, max_value=15, value=5)

# ---------------------------
# Upload Document
# ---------------------------
if input_option == "Upload Document":
    uploaded_file = st.file_uploader("Upload a document (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
    if uploaded_file:
        text = extract_text(uploaded_file)
        if text:
            st.subheader("Detected Language")
            st.write(detect_language(text))

            st.subheader("Original Text Preview")
            st.write(text[:1000] + "...")
            st.write(f"**Word Count:** {count_words(text)}")

            if st.button("Generate Summary"):
                summary = summarize_text(text, summary_length)
                st.subheader("📄 Summary")
                st.write(summary)
                st.write(f"**Summary Word Count:** {count_words(summary)}")
        else:
            st.error("Unsupported or unreadable file format.")

# ---------------------------
# Enter Text
# ---------------------------
elif input_option == "Enter Text":
    user_text = st.text_area("Enter text here", height=300)
    if user_text.strip():
        st.subheader("Detected Language")
        st.write(detect_language(user_text))
        st.write(f"**Word Count:** {count_words(user_text)}")

        if st.button("Generate Text Summary"):
            summary = summarize_text(user_text, summary_length)
            st.subheader("📄 Summary")
            st.write(summary)
            st.write(f"**Summary Word Count:** {count_words(summary)}")
