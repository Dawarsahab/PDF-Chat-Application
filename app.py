import streamlit as st
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import PyPDF2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class PDFChatApp:
    def __init__(self):
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.qa_model = pipeline('question-answering', model='deepset/roberta-base-squad2')
        self.chunk_size = 500
        self.documents = []
        self.embeddings = []

    def extract_text_from_pdf(self, pdf_file):
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    def chunk_text(self, text):
        words = text.split()
        chunks = []
        current_chunk = []
        current_size = 0
        
        for word in words:
            current_chunk.append(word)
            current_size += len(word) + 1
            
            if current_size >= self.chunk_size:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_size = 0
                
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        return chunks

    def process_pdf(self, pdf_file):
        text = self.extract_text_from_pdf(pdf_file)
        chunks = self.chunk_text(text)
        self.documents.extend(chunks)
        new_embeddings = self.embedder.encode(chunks)
        self.embeddings.extend(new_embeddings)

    def find_relevant_chunks(self, question, top_k=3):
        question_embedding = self.embedder.encode([question])[0]
        similarities = cosine_similarity([question_embedding], self.embeddings)[0]
        top_indices = np.argsort(similarities)[-top_k:]
        return [self.documents[i] for i in top_indices]

    def answer_question(self, question):
        if not self.documents:
            return "Please upload a PDF first."
        
        relevant_chunks = self.find_relevant_chunks(question)
        context = " ".join(relevant_chunks)
        
        answer = self.qa_model(question=question, context=context)
        return answer['answer']

def main():
    st.title("PDF Chat Application")
    
    pdf_chat = PDFChatApp()
    
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")
    if uploaded_file:
        with st.spinner("Processing PDF..."):
            pdf_chat.process_pdf(uploaded_file)
        st.success("PDF processed successfully!")
        
        st.subheader("Ask Questions")
        question = st.text_input("Enter your question:")
        if question:
            with st.spinner("Finding answer..."):
                answer = pdf_chat.answer_question(question)
            st.write("Answer:", answer)

if __name__ == "__main__":
    main()



