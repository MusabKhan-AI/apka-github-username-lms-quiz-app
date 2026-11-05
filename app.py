import random
from groq import Groq
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI & Machine Learning LMS Quiz Portal",
    page_icon="📚",
    layout="centered",
)

# Initialize Groq client using Streamlit Secrets safely
try:
    groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
    groq_client = None

# MCQs based on provided AI and Machine Learning Lectures & Slides
MCQS_DATA = [
    # Lecture 1: Introduction to AI & ML
    {
        "question": "Who coined the term 'Machine Learning' in 1959?",
        "options": ["John McCarthy", "Arthur Samuel", "Alan Turing", "Tom Mitchell"],
        "answer": "Arthur Samuel",
        "reason": "Arthur Samuel, an IBM employee and pioneer in computer gaming, coined the term machine learning in 1959."
    },
    {
        "question": "What is the relationship between AI, ML, and Deep Learning?",
        "options": [
            "ML is a subset of AI, and Deep Learning is a subset of ML",
            "AI is a subset of ML",
            "Deep Learning is broader than AI",
            "All three are completely independent fields"
        ],
        "answer": "ML is a subset of AI, and Deep Learning is a subset of ML",
        "reason": "Artificial Intelligence is the broad family, Machine Learning is its subset, and Deep Learning is a subset of Machine Learning."
    },
    {
        "question": "Who is credited with originally using the term 'Artificial Intelligence' in 1956?",
        "options": ["Arthur Samuel", "John McCarthy", "Alan Turing", "Syed Adnan Shah Bukhari"],
        "answer": "John McCarthy",
        "reason": "John McCarthy used the terminology 'Artificial Intelligence' in 1956 and hosted the first AI conference."
    },
    {
        "question": "According to Tom Mitchell's definition of learning, a computer program learns from experience E regarding task T if its performance P:",
        "options": ["Decreases", "Stays constant", "Improves with experience E", "Becomes zero"],
        "answer": "Improves with experience E",
        "reason": "Performance at task T, measured by P, improves with experience E."
    },
    {
        "question": "Which of the following data-driven features applies to Machine Learning?",
        "options": [
            "It cannot use past data",
            "It is completely rule-based without data",
            "It can learn from past data and automatically improve its performance",
            "It only works with text documents"
        ],
        "answer": "It can learn from past data and automatically improve its performance",
        "reason": "Machines can learn from past data and automatically improve their performance as a core feature of ML."
    },
    {
        "question": "Which AI category focuses primarily on increasing success rather than accuracy?",
        "options": ["Machine Learning", "Artificial Intelligence", "Deep Learning", "Supervised Learning"],
        "answer": "Artificial Intelligence",
        "reason": "The aim of AI is generally to increase the chance of success, whereas ML focuses heavily on increasing accuracy."
    },
    {
        "question": "What kind of data can Artificial Intelligence work with?",
        "options": [
            "Only structured data",
            "Only unstructured data",
            "Structured, semi-structured, and unstructured data",
            "Only numerical data"
        ],
        "answer": "Structured, semi-structured, and unstructured data",
        "reason": "AI can work with structured, semi-structured, and unstructured data like text, images, video, and audio."
    },
    {
        "question": "Machine Learning algorithms primarily require what type of data to learn and improve?",
        "options": [
            "Only unstructured audio",
            "Large amounts of structured and semi-structured data",
            "Random noise",
            "No data at all"
        ],
        "answer": "Large amounts of structured and semi-structured data",
        "reason": "ML algorithms require large amounts of structured data to learn and improve performance."
    },
    {
        "question": "Which of the following is a classic example of AI rather than standard machine learning?",
        "options": [
            "Facebook's friend suggestions",
            "Google's search algorithms",
            "Siri and customer service chatbots",
            "Stock price forecasting"
        ],
        "answer": "Siri and customer service chatbots",
        "reason": "Siri and chatbot customer service are key uses of AI, while ML common uses include friend suggestions and stock forecasts."
    },
    {
        "question": "What is the primary goal of Machine Learning?",
        "options": [
            "To simulate natural intelligence entirely",
            "To learn from data on certain tasks to maximize performance on that task",
            "To replace human consciousness",
            "To execute static rules"
        ],
        "answer": "To learn from data on certain tasks to maximize performance on that task",
        "reason": "The goal of machine learning is to learn from data on certain tasks to maximize performance on those tasks."
    },

    # Machine Learning Life Cycle
    {
        "question": "How many major steps are there in the Machine Learning life cycle?",
        "options": ["3", "5", "7", "
