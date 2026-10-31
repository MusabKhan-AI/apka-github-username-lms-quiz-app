import random
from groq import Groq
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Data Structures LMS Quiz Portal", page_icon="📚", layout="centered"
)

# Initialize Groq client using Streamlit Secrets safely
try:
  groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
  groq_client = None

# 50 Data Structures MCQs extracted from your PDF (Numbering removed from questions)
# 60 mixed MCQs from Lectures 03, 04, and 05
MCQS_DATA = [
    {
            "question": "What is a strategic environment in the lecture's description?",
            "options": ['Deterministic except for the actions of other agents', 'Always fully observable', 'A static environment with no actions', 'An environment with only continuous values'],
            "answer": 'A',
            "reason": 'Deterministic except for the actions of other agents',
        },
    {
            "question": 'What is a performance measure?',
            "options": ['A device that moves the agent', "An objective criterion for success of an agent's behavior", 'A record of source code length', 'The complete percept history'],
            "answer": 'B',
            "reason": "An objective criterion for success of an agent's behavior",
        },
    {
            "question": 'Which is an example of an artificial but potentially complex environment?',
            "options": ['Flight simulator', 'Video game', 'Internet', 'All of the above'],
            "answer": 'D',
            "reason": 'All of the above',
        },
    {
            "question": 'Which is an example of a vacuum-cleaner percept shown in the lecture?',
            "options": ['[A, Dirty]', '[Motor, Fast]', '[Sensor, Off]', '[B, Left]'],
            "answer": 'A',
            "reason": '[A, Dirty]',
        },
    {
            "question": 'Which PEAS element enables the agent to detect information?',
            "options": ['Actuators', 'Sensors', 'Environment', 'Utility'],
            "answer": 'B',
            "reason": 'Sensors',
        },
    {
            "question": 'What must an agent do to use the entire percept sequence?',
            "options": ['Remember all percepts in the sequence', 'Ignore previous percepts in every case', 'Remove its architecture', 'Use no program'],
            "answer": 'A',
            "reason": 'Remember all percepts in the sequence',
        },
    {
            "question": 'Which can cause partial observability according to the lecture?',
            "options": ['Noisy sensors', 'Missing parts of information', 'Both noisy sensors and missing parts', 'A title page'],
            "answer": 'C',
            "reason": 'Both noisy sensors and missing parts',
        },
    {
            "question": 'Which statement best captures the distinction between agent function and agent program?',
            "options": ['Function specifies the percept-to-action mapping; program implements it', 'Function is hardware and program is the environment', 'They are both actuators', 'The function only stores page numbers'],
            "answer": 'A',
            "reason": 'Function specifies the percept-to-action mapping; program implements it',
        },
    {
            "question": 'Which notation is used for the agent function in the slides?',
            "options": ['f: A → P*', 'f: P* → A', 'f: S → E', 'f: E → P'],
            "answer": 'B',
            "reason": 'f: P* → A',
        },
    {
            "question": 'Which of the following is NOT listed as one of the Lecture 05 structure components?',
            "options": ['Agent behavior', 'Agent program', 'Agent function', 'Weather forecast'],
            "answer": 'D',
            "reason": 'Weather forecast',
        },
    {
            "question": 'Which condition makes an environment discrete according to the slides?',
            "options": ['Limited distinct states with clearly defined percepts and actions', 'Continuous values at every moment', 'No defined states or actions', 'Unpredictable outcomes only'],
            "answer": 'A',
            "reason": 'Limited distinct states with clearly defined percepts and actions',
        },
    {
            "question": 'According to the lecture, omniscience in reality is:',
            "options": ['Always guaranteed', 'Impossible in reality', 'The same as autonomy', 'Required for every agent'],
            "answer": 'B',
            "reason": 'Impossible in reality',
        },
    {
            "question": 'A cooperative multiagent environment relies on:',
            "options": ['Cooperation between multiple AI agents', 'Only one agent', 'No communication or coordination ever', 'Infinite knowledge'],
            "answer": 'A',
            "reason": 'Cooperation between multiple AI agents',
        },
    {
            "question": 'In a competitive multiagent environment, agents are set against each other to:',
            "options": ['Optimize a specific outcome', 'Share one identical action', 'Avoid all decisions', 'Remove the environment'],
            "answer": 'A',
            "reason": 'Optimize a specific outcome',
        },
    {
            "question": 'What does the agent program implement?',
            "options": ['Agent function', 'Physical environment', 'Performance measure only', "The user's assignment"],
            "answer": 'A',
            "reason": 'Agent function',
        },
    {
            "question": 'According to the lecture, an agent perceives its environment through which components?',
            "options": ['Actuators', 'Sensors', 'Programs only', 'Performance measures'],
            "answer": 'B',
            "reason": 'Sensors',
        },
    {
            "question": 'How does the lecture describe inference in deep learning?',
            "options": ['Inference in layers', 'Inference without computation', 'Inference only by hand', 'Inference by page numbering'],
            "answer": 'A',
            "reason": 'Inference in layers',
        },
    {
            "question": 'What is a percept history or percept sequence?',
            "options": ['Only the next action', 'The complete history of what has been perceived', "Only the agent's hardware", 'A list of actuators'],
            "answer": 'B',
            "reason": 'The complete history of what has been perceived',
        },
    {
            "question": 'In the formula for an agent, architecture refers to:',
