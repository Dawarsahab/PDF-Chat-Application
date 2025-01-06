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

Upload PDF Files


Extracted Text Display


Question-Answering Interface


Relevant Sections Highlighted


Setup Instructions

Prerequisites

Python (>= 3.8)

Recommended: A virtual environment for dependency management.

Installation

Clone the Repository:

git clone https://github.com/your_username/chat-with-pdf.git
cd chat-with-pdf

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
