# Offline AI Summarizer

An AI-powered document summarization application that works completely offline. Upload documents or paste text and generate concise summaries without sending your data to external servers.

## Features

* 📄 Support for PDF, DOCX, and TXT files
* ✍️ Direct text input summarization
* 🔒 Fully offline processing
* 🎯 Custom summary word limit
* ⚡ Fast and lightweight Streamlit interface
* 📚 Extracts key points from large documents
* 🖥️ Simple and user-friendly UI
* 🔐 Privacy-focused (no cloud dependency)

---

## Supported Input Formats

* PDF (.pdf)
* Word Documents (.docx)
* Text Files (.txt)
* Raw Text Input

---

## Tech Stack

* Python
* Streamlit
* PyPDF2
* python-docx
* NLTK
* NumPy
* Pandas

---

## Project Structure

```text
offline_ai_summarizer/
│
├── app.py
├── summarizer.py
├── requirements.txt
├── README.md
│
├── uploads/
├── utils/
└── assets/
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/satya66123/offline_ai_summarizer.git
cd offline_ai_summarizer
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

Application will open automatically in your browser.

---

## How It Works

1. Upload a document or enter text.
2. The application extracts the content.
3. Important sentences are identified using NLP techniques.
4. A concise summary is generated based on the specified word limit.
5. The summary is displayed instantly.

---

## Use Cases

### Students

* Summarize study materials
* Quickly review notes

### Researchers

* Extract key findings from papers
* Save reading time

### Professionals

* Summarize reports
* Review meeting notes

### Content Creators

* Generate condensed versions of long articles
* Extract important information quickly

---

## Screenshots

Add screenshots here:

```text
screenshots/
├── home.png
├── upload.png
└── summary.png
```

---

## Future Enhancements

* Multi-language summarization
* Bullet-point summaries
* Summary export to PDF
* AI-powered abstractive summarization
* Document comparison
* Chat with documents

---

## Privacy

All processing happens locally on your machine.

No data is uploaded to external servers.

---

## Author

### Satya Srinath Nekkanti

GitHub: [satya66123/offline_ai_summarizer](https://github.com/satya66123/offline_ai_summarizer)

LinkedIn: [Satya Srinath Nekkanti LinkedIn](https://www.linkedin.com/in/satya-srinath-nekkanti-08b012a3)

---

## License

This project is licensed under the MIT License.

"Offline AI Summarizer: A Tool for Quick Document ..."
