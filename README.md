# PDF-Chat-Application
Overview

This repository contains the Chat with PDF Application, an interactive tool that allows users to upload PDF documents, extract their content, convert the text into embeddings using Sentence Transformers, and perform question-answering tasks using the extracted content. The app is built with Streamlit and employs efficient similarity search via FAISS.

Features

Upload single or multiple PDF files.

Extract and display text content from PDFs.

Generate embeddings for semantic understanding using Sentence Transformers.

Enable users to ask questions about the uploaded PDFs and receive accurate answers.

Retrieve relevant sections from the documents for better context.

Screenshots
<img width="1440" alt="Screenshot 2025-01-07 at 12 47 30 AM" src="https://github.com/user-attachments/assets/a693d4d0-e93b-46e2-9fb0-66313751b54d" />

Upload PDF Files
<img width="1440" alt="Screenshot 2025-01-07 at 12 48 18 AM" src="https://github.com/user-attachments/assets/0baf6106-8926-43e0-8adc-940459086e52" />

Question-Answering Interface

<img width="1440" alt="Screenshot 2025-01-07 at 12 49 52 AM" src="https://github.com/user-attachments/assets/f6276ad9-a432-448d-bdc6-abe7921e3a3c" />
<img width="1440" alt="Screenshot 2025-01-07 at 12 50 25 AM" src="https://github.com/user-attachments/assets/5a5bae56-5431-4662-bea2-229d65a40291" />

Setup Instructions

Prerequisites

Python (>= 3.8)

Recommended: A virtual environment for dependency management.

Installation

Create a Virtual Environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

Download Sentence Transformer Model (if not already cached):
The code automatically downloads the required model when first run.

Usage Instructions

Run the Application:

streamlit run app.py

Access the Interface:
Open your browser and navigate to http://localhost:8501.

Upload PDFs:

Use the sidebar to upload one or more PDF files.

Optionally, view the extracted text from the uploaded PDFs.

Ask Questions:

Enter your query in the provided text box.

The app will return a semantically accurate answer based on the document's content.

View Relevant Sections:

Enable the Show Relevant Sections checkbox to display document excerpts related to the answer.
