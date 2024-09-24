import os
import PyPDF2
import google.generativeai as genai
import streamlit as st
import time

# Set your Google API Key
GOOGLE_API_KEY = "API"  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

# Function to read PDF content
def read_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to get response from Gemini API
def get_gemini_response(question, context):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    response = model.generate_content(prompt)
    return response.text.strip()

# Load your PDF document
pdf_path = r"C:\Users\Khuzaima Ayaz\Desktop\EurosHub ChatBot\eurosHub.pdf"  # Ensure this path is correct
pdf_content = read_pdf(pdf_path)

# Streamlit UI setup
st.set_page_config(page_title="PDF Q&A with Google Gemini", layout="wide")

# Custom CSS for a ChatGPT-like look
st.markdown("""
    <style>
    body {
        background-color: #f0f2f5;
    }
    .chat-container {
        max-width: 600px;
        margin: auto;
        background: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    .user-message {
        background-color: #007BFF;
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
        text-align: left;
    }
    .bot-message {
        background-color: #e9ecef;
        color: black;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
        text-align: left;
    }
    .logo {
        width: 100%;  /* Adjust to your desired size */
        max-width: 300px;  /* Maximum width for the logo */
        opacity: 0.1;  /* Makes the logo faint behind the title */
        position: absolute;
        top: 50px;  /* Adjust based on title height */
        left: 50%;
        transform: translateX(-50%);
        z-index: -1;  /* Ensures the logo is behind other content */
    }
    </style>
""", unsafe_allow_html=True)

# Add your custom logo
st.markdown('<img src="C:\\Users\\Khuzaima Ayaz\\Desktop\\EurosHub ChatBot\\Logo - Cyan.png" class="logo">', unsafe_allow_html=True)  # Replace with your logo path

# Title
st.title("📚 EurosHub Chat Bot")
st.markdown("Ask questions about the content of the PDF document.")

# Chat interface
user_input = st.text_input("Type your question:", "")

if st.button("Ask"):
    if user_input:
        # Show loading spinner
        with st.spinner("Loading response..."):
            time.sleep(1)  # Simulate loading time
            response = get_gemini_response(user_input, pdf_content)
        st.success("Response received!")  # Notify user response is ready
        
        # Display messages without bold formatting
        st.markdown(f'<div class="chat-container"><div class="user-message">You: {user_input}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-message">Bot: {response}</div></div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a question.")
