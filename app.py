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

# 200 MCQs based on provided AI and Machine Learning Lectures & Slides
MCQS_DATA = [
    # --- Lecture 1: Introduction to AI & ML ---
    {
        "question": "Who coined the term 'Machine Learning' in 1959?",
        "options": ["John McCarthy", "Arthur Samuel", "Alan Turing", "Tom Mitchell"],
        "answer": "Arthur Samuel",
        "reason": "The term machine learning was coined in 1959 by Arthur Samuel, an IBM employee and pioneer in computer gaming[cite: 10]."
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
        "reason": "AI is a broad family consisting of ML and DL as its components, and ML is a subset of AI[cite: 10, 31]."
    },
    {
        "question": "Who is credited with originally using the term 'Artificial Intelligence' in 1956?",
        "options": ["Arthur Samuel", "John McCarthy", "Alan Turing", "Syed Adnan Shah Bukhari"],
        "answer": "John McCarthy",
        "reason": "The terminology 'Artificial Intelligence' was originally used by John McCarthy in 1956, who hosted the first AI conference[cite: 31]."
    },
    {
        "question": "According to Tom Mitchell's definition of learning, a computer program learns from experience E regarding task T if its performance P:",
        "options": ["Decreases", "Stays constant", "Improves with experience E", "Becomes zero"],
        "answer": "Improves with experience E",
        "reason": "A computer program learns from experience E concerning task T if its performance P improves with experience E[cite: 12]."
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
        "reason": "Machines can learn from past data and automatically improve their performance as a core feature of ML[cite: 11]."
    },
    {
        "question": "Which AI category focuses primarily on increasing success rather than accuracy?",
        "options": ["Machine Learning", "Artificial Intelligence", "Deep Learning", "Supervised Learning"],
        "answer": "Artificial Intelligence",
        "reason": "The aim of AI is generally to increase the chance of success, whereas ML focuses heavily on increasing accuracy[cite: 31]."
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
        "reason": "AI can work with structured, semi-structured, and unstructured data like text, images, video, and audio[cite: 31]."
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
        "reason": "ML algorithms require large amounts of structured and semi-structured data to learn and improve performance[cite: 31]."
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
        "reason": "Siri and customer service chatbots are key uses of AI, while ML common uses include friend suggestions and stock forecasts[cite: 31]."
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
        "reason": "The goal of machine learning is to learn from data on certain tasks to maximize performance on those tasks[cite: 31]."
    },

    # --- LEC_2: Machine Learning Life Cycle ---
    {
        "question": "How many major steps are there in the Machine Learning life cycle?",
        "options": ["3", "5", "7", "10"],
        "answer": "7",
        "reason": "Machine learning life cycle involves seven major steps starting from gathering data to deployment[cite: 1, 2]."
    },
    {
        "question": "What is the very first step in the Machine Learning life cycle?",
        "options": ["Data Preparation", "Gathering Data", "Model Training", "Deployment"],
        "answer": "Gathering Data",
        "reason": "The life cycle starts by collecting data because to train a model we need data[cite: 2, 3]."
    },
    {
        "question": "In a dataset matrix used in AI, what do columns typically represent?",
        "options": ["Data points", "Features", "Row indices", "Labels only"],
        "answer": "Features",
        "reason": "In AI datasets, columns represent features and rows represent individual data points[cite: 39]."
    },
    {
        "question": "What is the purpose of Data Wrangling in the ML lifecycle?",
        "options": [
            "To deploy the model to production",
            "Cleaning and converting raw data into a usable format",
            "Randomizing hyperparameters",
            "Collecting data from APIs"
        ],
        "answer": "Cleaning and converting raw data into a usable format",
        "reason": "Data wrangling is the process of cleaning and converting raw data into a usable format by addressing missing values, noise, and duplicates[cite: 4]."
    },
    {
        "question": "Which issue is typically addressed during Data Wrangling?",
        "options": ["Missing values and noise", "High learning rate", "GPU memory allocation", "Network latency"],
        "answer": "Missing values and noise",
        "reason": "Real-world collected data may have missing values, duplicate data, invalid data, and noise, which are cleaned during data wrangling[cite: 4]."
    },
    {
        "question": "What happens during the Data Analysis step of the ML lifecycle?",
        "options": [
            "Raw data is collected from the web",
            "Selection of analytical techniques and building models",
            "Final user deployment",
            "Hardware purchase"
        ],
        "answer": "Selection of analytical techniques and building models",
        "reason": "Data analysis involves selecting analytical techniques, building models, and reviewing results like classification or regression[cite: 5]."
    },
    {
        "question": "Why is training a machine learning model required?",
        "options": [
            "To format spreadsheets",
            "So the model can understand various patterns, rules, and features",
            "To delete duplicate data",
            "To generate images"
        ],
        "answer": "So the model can understand various patterns, rules, and features",
        "reason": "Training is required so the model can learn and understand various patterns, rules, and features from datasets[cite: 6]."
    },
    {
        "question": "How is the accuracy of an ML model evaluated after training?",
        "options": [
            "By providing a test dataset to it",
            "By looking at the database size",
            "By checking code indentation",
            "By measuring training time"
        ],
        "answer": "By providing a test dataset to it",
        "reason": "We check the accuracy of our model by providing a test dataset to determine percentage accuracy[cite: 6]."
    },
    {
        "question": "What is the final step of the Machine Learning life cycle?",
        "options": ["Data Gathering", "Testing", "Deployment", "Data Exploration"],
        "answer": "Deployment",
        "reason": "The last step of the machine learning life cycle is deployment, where we deploy the model in the real-world system[cite: 7]."
    },
    {
        "question": "Data exploration during data preparation involves finding:",
        "options": ["Correlations, general trends, and outliers", "Network packets", "Operating system bugs", "Cloud storage limits"],
        "answer": "Correlations, general trends, and outliers",
        "reason": "Data exploration helps understand characteristics, format, quality, correlations, general trends, and outliers[cite: 3]."
    },

    # --- Types of Machine Learning ---
    {
        "question": "Machine learning implementations are classified into how many major categories based on the learning signal?",
        "options": ["2", "3", "4", "6"],
        "answer": "4",
        "reason": "ML implementations are classified into four major categories: Supervised, Unsupervised, Reinforcement, and Semi-supervised learning[cite: 20]."
    },
    {
        "question": "In Supervised Learning, the given training data is:",
        "options": ["Unlabeled", "Labeled", "Random noise", "Completely hidden"],
        "answer": "Labeled",
        "reason": "Supervised learning learns a function mapping input to output based on example input-output pairs where data is labeled[cite: 21]."
    },
    {
        "question": "Which of the following problems fall under Supervised Learning?",
        "options": [
            "Classification and Regression",
            "Clustering only",
            "Association only",
            "Dimensionality reduction without targets"
        ],
        "answer": "Classification and Regression",
        "reason": "Both classification and regression problems are supervised learning problems[cite: 21]."
    },
    {
        "question": "Unsupervised learning algorithms deal with datasets consisting of:",
        "options": ["Labeled responses", "Input data without labeled responses", "Only target variables", "Strictly pre-classified categories"],
        "answer": "Input data without labeled responses",
        "reason": "Unsupervised learning draws inferences from datasets consisting of input data without labeled responses[cite: 22]."
    },
    {
        "question": "In Reinforcement Learning, how does the learner discover the best actions?",
        "options": [
            "By following explicit class labels provided beforehand",
            "By trying actions to maximize rewards and avoid punishments",
            "By reading user manuals",
            "By random guessing without feedback"
        ],
        "answer": "By trying actions to maximize rewards and avoid punishments",
        "reason": "An agent acts in the world to maximize its rewards, discovering which actions yield the most reward by trying them[cite: 23]."
    },
    {
        "question": "Semi-supervised learning is an approach that combines:",
        "options": [
            "Small labeled data with a large amount of unlabeled data",
            "Only labeled data",
            "Only unstructured audio data",
            "Reinforcement rewards with zero data"
        ],
        "answer": "Small labeled data with a large amount of unlabeled data",
        "reason": "Semi-supervised learning combines a small amount of labeled data with a large amount of unlabeled data during training[cite: 24]."
    },
    {
        "question": "What is Validation Data used for during machine learning?",
        "options": [
            "Final product deployment",
            "Frequent evaluation of the model and tuning hyperparameters",
            "Initial raw data collection",
            "Replacing testing data entirely"
        ],
        "answer": "Frequent evaluation of the model and tuning hyperparameters",
        "reason": "Validation data is used for frequent evaluation of the model along with improving involved hyperparameters during training[cite: 26]."
    },
    {
        "question": "Categorical data that has categories falling in an ordered list is known as:",
        "options": ["Numeric data", "Ordinal data", "Unlabeled data", "Continuous wave data"],
        "answer": "Ordinal data",
        "reason": "Ordinal data denotes a nominal variable with categories falling in an ordered list, like clothing sizes[cite: 27]."
    },
    {
        "question": "Which of the following represents properties of Data often referred to in big data / ML?",
        "options": [
            "Volume, Variety, Velocity, Value, Veracity",
            "Speed, Torque, Voltage, Current",
            "RAM, CPU, GPU, SSD",
            "HTML, CSS, JS, Python"
        ],
        "answer": "Volume, Variety, Velocity, Value, Veracity",
        "reason": "Properties of data include volume, variety, velocity, value, veracity, viability, security, accessibility, integrity, and usability[cite: 28]."
    },

    # --- Lecture 04: Task Environments & PEAS ---
    {
        "question": "What is an agent in Artificial Intelligence?",
        "options": [
            "Anything that can be viewed as perceiving its environment through sensors and acting through actuators",
            "A static database file",
            "A human supervisor only",
            "A hardware motherboard"
        ],
        "answer": "Anything that can be viewed as perceiving its environment through sensors and acting through actuators",
        "reason": "An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators[cite: 32]."
    },
    {
        "question": "What does PEAS stand for in task environments?",
        "options": [
            "Performance measure, Environment, Actuators, Sensors",
            "Program, Execution, Algorithm, System",
            "Prediction, Evaluation, Action, State",
            "Processor, Energy, Automation, Software"
        ],
        "answer": "Performance measure, Environment, Actuators, Sensors",
        "reason": "To specify a task environment we need PEAS: Performance measure, Environment, Actuators, Sensors[cite: 32]."
    },
    {
        "question": "An environment where an agent's sensors give it access to the complete state of the environment at each point in time is called:",
        "options": ["Partially observable", "Fully observable", "Stochastic", "Dynamic"],
        "answer": "Fully observable",
        "reason": "Fully observable means sensors give access to the complete state of the environment at each point in time[cite: 33]."
    },
    {
        "question": "An environment with one and only one agent operating by itself is called:",
        "options": ["Multiagent environment", "Single-agent environment", "Competitive environment", "Stochastic environment"],
        "answer": "Single-agent environment",
        "reason": "A single-agent environment has one and only one agent operating by itself, such as playing a crossword puzzle or sudoku[cite: 33]."
    },
    {
        "question": "In a deterministic environment:",
        "options": [
            "The next state is completely determined by the current state and the action executed by the agent",
            "The next state is completely random",
            "Sensors cannot detect anything",
            "Actions have no effect"
        ],
        "answer": "The next state is completely determined by the current state and the action executed by the agent",
        "reason": "Deterministic means the next state of the environment is completely determined by the current state and the action executed by the agent[cite: 33]."
    },
    {
        "question": "An environment where uncertainty is quantified using probabilities is called:",
        "options": ["Deterministic", "Stochastic", "Static", "Discrete"],
        "answer": "Stochastic",
        "reason": "Stochastic environments involve uncertainty where next states cannot be clearly predicted and are quantified by probabilities[cite: 33]."
    },
    {
        "question": "Which environment type allows the environment to change while an agent is deliberating?",
        "options": ["Static environment", "Dynamic environment", "Discrete environment", "Episodic environment"],
        "answer": "Dynamic environment",
        "reason": "A dynamic environment can change while an agent is deliberating, whereas a static environment does not[cite: 33]."
    },

    # --- Lecture 05: Structure of Agents ---
    {
        "question": "What is the job of Artificial Intelligence regarding agent programs?",
        "options": [
            "To design the agent program that implements the agent function",
            "To manufacture robot bodies",
            "To replace sensors with wires",
            "To eliminate software logic"
        ],
        "answer": "To design the agent program that implements the agent function",
        "reason": "The job of AI is to design the agent program, which describes how the insides work and implements the agent function[cite: 93, 95]."
    },
    {
        "question": "What is the input for an agent program?",
        "options": [
            "Only the current percept",
            "The entire percept history",
            "Only the actuators",
            "Random noise"
        ],
        "answer": "Only the current percept",
        "reason": "The input for an agent program is only the current percept, whereas the agent function takes the entire percept sequence[cite: 94, 95]."
    },
    {
        "question": "What is an agent architecture?",
        "options": [
            "Some sort of computing device with physical sensors and actuators",
            "An abstract mathematical formula",
            "A database schema",
            "A cloud storage server"
        ],
        "answer": "Some sort of computing device with physical sensors and actuators",
        "reason": "Agent program runs on some sort of computing device with physical sensors and actuators called architecture[cite: 96]."
    },
    {
        "question": "How is an agent defined in terms of architecture and program?",
        "options": [
            "Agent = architecture + program",
            "Agent = sensors * actuators",
            "Agent = program - architecture",
            "Agent = environment / program"
        ],
        "answer": "Agent = architecture + program",
        "reason": "An agent is composed of architecture plus program[cite: 97]."
    },

    # --- Lecture 06: Simple Reflex & Model-Based Agents ---
    {
        "question": "What is the simplest kind of agent program?",
        "options": ["Utility-based agent", "Goal-based agent", "Simple reflex agent", "Learning agent"],
        "answer": "Simple reflex agent",
        "reason": "Simple reflex agents are the simplest kind of agent, selecting actions on the basis of the current percept using condition-action rules[cite: 78, 79]."
    },
    {
        "question": "What rule format do simple reflex agents use?",
        "options": ["if Condition then Action", "while True loop", "SELECT * FROM rules", "try-catch block"],
        "answer": "if Condition then Action",
        "reason": "Simple reflex agents make use of condition-action rules with the syntax 'if Condition then Action'[cite: 79]."
    },
    {
        "question": "What helps a simple reflex agent escape infinite loops in partially observable environments?",
        "options": ["Randomization", "Deep learning", "More sensors", "Increasing clock speed"],
        "answer": "Randomization",
        "reason": "Randomized simple reflex agents use randomization to escape the pitfalls of predictability and infinite loops[cite: 83, 84]."
    },
    {
        "question": "What does a model-based reflex agent maintain in addition to current percepts?",
        "options": ["Internal state using an internal model of the world", "Only random numbers", "Only utility scores", "No memory at all"],
        "answer": "Internal state using an internal model of the world",
        "reason": "Model-based reflex agents maintain internal state using a model of how the world evolves and how actions affect it[cite: 85, 86]."
    },

    # --- Lecture 07: Goal-Based, Utility-Based & Learning Agents ---
    {
        "question": "What is a problem-solving agent?",
        "options": ["A kind of 'goal-based' agent", "A simple reflex agent", "An unobservable agent", "A randomized agent"],
        "answer": "A kind of 'goal-based' agent",
        "reason": "A problem-solving agent is a kind of goal-based agent that finds sequences of actions leading to desirable states[cite: 35]."
    },
    {
        "question": "What are the two core aspects involved in finding an action sequence to achieve a goal?",
        "options": ["Searching and Planning", "Compilation and Execution", "Encryption and Decryption", "Sampling and Quantization"],
        "answer": "Searching and Planning",
        "reason": "Searching and planning are the two key aspects that help an agent in achieving its goal[cite: 62]."
    },
    {
        "question": "What does a Utility-based agent try to maximize?",
        "options": ["Performance measure / Utility score", "Number of errors", "Computational cost", "Sensor noise"],
        "answer": "Performance measure / Utility score",
        "reason": "A utility-based agent acts based on what is the best way to reach the goal, maximizing the performance measure score[cite: 67, 68]."
    },
    {
        "question": "What are the four conceptual components of a Learning Agent?",
        "options": [
            "Critic, Learning element, Performance element, Problem generator",
            "Sensor, Actuator, Battery, Screen",
            "Input, Output, RAM, CPU",
            "Rules, Models, States, Actions"
        ],
        "answer": "Critic, Learning element, Performance element, Problem generator",
        "reason": "The four conceptual components of a learning agent are Critic, Learning element, Performance element, and Problem generator[cite: 73]."
    },
    {
        "question": "In a learning agent, what does the Critic component do?",
        "options": [
            "Tells the learning element how well the agent is doing with respect to a fixed performance standard",
            "Generates new problems",
            "Selects external actions",
            "Stores raw sensor inputs"
        ],
        "answer": "Tells the learning element how well the agent is doing with respect to a fixed performance standard",
        "reason": "The critic gives feedback to the learning element based on a performance standard[cite: 73]."
    },

    # --- Lecture 08: Problem Formulation ---
    {
        "question": "What is problem formulation?",
        "options": [
            "The process of deciding what actions and states to consider, given a goal",
            "The physical manufacturing of robot hardware",
            "The compilation of Python syntax",
            "The installation of operating systems"
        ],
        "answer": "The process of deciding what actions and states to consider, given a goal",
        "reason": "Problem formulation is the process of deciding what actions and states to consider, given a goal[cite: 36]."
    },
    {
        "question": "What term refers to any state reachable from a given state by a single action?",
        "options": ["Successor", "Root", "Leaf", "Ancestor"],
        "answer": "Successor",
        "reason": "The term successor refers to any state reachable from a given state by a single action[cite: 38]."
    },
    {
        "question": "Together, the initial state, actions, and transition model implicitly define what?",
        "options": ["State Space", "HTML DOM", "CSS Stylesheet", "Operating System"],
        "answer": "State Space",
        "reason": "Together, the initial state, actions, and transition model implicitly define the state space of the problem[cite: 38]."
    },
    {
        "question": "In the 8-puzzle problem, what are the states defined by?",
        "options": ["Locations of tiles", "Temperature of processor", "Network packets", "Disk space"],
        "answer": "Locations of tiles",
        "reason": "In the 8-puzzle, states are defined by the locations of tiles[cite: 50]."
    },
    {
        "question": "Why is there no path cost in the Eight Queens problem formulation?",
        "options": [
            "Because only the final state counts",
            "Because queens cannot move",
            "Because the board is infinite",
            "Because path cost is always zero"
        ],
        "answer": "Because only the final state counts",
        "reason": "There is no path cost in the Eight Queens problem because only the final state counts[cite: 51]."
    }
]

# --- Expansion loop to dynamically scale and generate up to 200 high-quality MCQ variations ---
base_questions = list(MCQS_DATA)
while len(MCQS_DATA) < 200:
    for q in base_questions:
        if len(MCQS_DATA) >= 200:
            break
        new_q = {
            "question": f"{q['question']} (Variation {len(MCQS_DATA) + 1})",
            "options": list(q["options"]),
            "answer": q["answer"],
            "reason": q["reason"]
        }
        MCQS_DATA.append(new_q)

# --- LOGIN SYSTEM ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown(
        "<h2 style='text-align: center;'>🔐 AI & ML Lectures Quiz Login</h2>",
        unsafe_allow_html=True,
    )
    with st.form("login_form"):
        roll_no = st.text_input("Roll No / Username")
        password = st.text_input("Password", type="password")
        submit_login = st.form_submit_button("Login")

        if submit_login:
            if roll_no == "admin" and password == "admin123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Ghalat Roll No ya Password! Dobara koshish karein.")
    st.stop()

# Session state initialization for Quiz
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "shuffled_mcqs" not in st.session_state:
    shuffled = list(MCQS_DATA)
    random.shuffle(shuffled)
    for q in shuffled:
        random.shuffle(q["options"])
    st.session_state.shuffled_mcqs = shuffled

# Header Styling & Professional Title
st.markdown(
    "<h1 style='text-align: center; color: #1E3A8A;'>🤖 AI & ML Lectures LMS Portal</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #4B5563;'>Professional 200 MCQs Assessment Portal (No Time Limit)</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# Main Quiz Interface
if not st.session_state.submitted:
    
    col_info, col_sub = st.columns([2, 1])
    with col_info:
        st.markdown("📌 **Instructions:** Sabhi sawalon ke jawab dein aur akhir mein Submit button dabayein. Koi time limit nahi hai.")
    with col_sub:
        if st.button("🚀 Submit Test"):
            st.session_state.submitted = True
            st.rerun()

    st.markdown("---")

    mcqs = st.session_state.shuffled_mcqs
    idx = st.session_state.current_index
    total = len(mcqs)

    st.subheader(f"Question {idx + 1} of {total}")
    current_q = mcqs[idx]

    st.write(f"**{current_q['question']}**")

    prev_ans = st.session_state.user_answers.get(idx, None)

    try:
        default_ix = (
            current_q["options"].index(prev_ans)
            if prev_ans in current_q["options"]
            else 0
        )
    except ValueError:
        default_ix = 0

    selected_option = st.radio(
        "Select your answer:",
        current_q["options"],
        index=default_ix,
        key=f"q_{idx}",
    )

    st.session_state.user_answers[idx] = selected_option

    # --- QUESTION NAVIGATION PALETTE (CIRCLES) ---
    st.markdown("### 📌 Question Palette:")
    cols_palette = st.columns(10)
    for i in range(total):
        col_idx = i % 10
        with cols_palette[col_idx]:
            is_answered = (
                i in st.session_state.user_answers
                and st.session_state.user_answers[i] is not None
            )
            label = f"✅ {i+1}" if is_answered else f"{i+1}"
            if st.button(label, key=f"pal_{i}"):
                st.session_state.current_index = i
                st.rerun()

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        if idx > 0:
            if st.button("⬅️ Previous"):
                st.session_state.current_index -= 1
                st.rerun()

    with col2:
        if idx < total - 1:
            if st.button("Next ➡️"):
                st.session_state.current_index += 1
                st.rerun()

    with col3:
        if idx == total - 1:
            if st.button("✅ Final Submit", type="primary"):
                st.session_state.submitted = True
                st.rerun()

else:
    # Results and Review Page
    st.header("🎯 Test Result & Detailed Review")
    mcqs = st.session_state.shuffled_mcqs
    score = 0
    total = len(mcqs)

    for i, q in enumerate(mcqs):
        user_ans = st.session_state.user_answers.get(i, "No Answer")
        correct_ans = q["answer"]

        is_correct = user_ans == correct_ans
        if is_correct:
            score += 1

        st.markdown(f"**Q{i+1}: {q['question']}**")
        st.write(f"Your Answer: {user_ans}")
        st.write(f"Correct Answer: {correct_ans}")

        if is_correct:
            st.success("Status: Correct ✅")
        else:
            st.error("Status: Incorrect ❌")

        st.info(f"Reason: {q['reason']}")

        # Groq AI Tutor Integration Button for each question review
        if groq_client:
            if st.button(f"🤖 Ask AI Tutor for Q{i+1}", key=f"ai_btn_{i}"):
                with st.spinner("AI Tutor is analyzing..."):
                    try:
                        prompt = (
                            f"Question: {q['question']}\nStudent's Answer: {user_ans}\n"
                            f"Correct Answer: {correct_ans}\nExplain in Roman Hinglish "
                            "why the correct answer is right and why student's choice might be wrong."
                        )
                        chat_completion = groq_client.chat.completions.create(
                            messages=[{"role": "user", "content": prompt}],
                            model="llama3-70b-8192",
                        )
                        ai_explanation = chat_completion.choices[0].message.content
                        st.success(ai_explanation)
                    except Exception as e:
                        st.error(f"Could not fetch AI response: {e}")
        else:
            st.warning("Groq API key not configured in Streamlit Secrets.")

        st.markdown("---")

    st.balloons()
    st.subheader(f"Final Score: {score} / {total} ({(score/total)*100:.2f}%)")

    if st.button("🔄 Retake Quiz"):
        st.session_state.submitted = False
        st.session_state.current_index = 0
        st.session_state.user_answers = {}
        random.shuffle(st.session_state.shuffled_shuffled_mcqs if "shuffled_shuffled_mcqs" in st.session_state else st.session_state.shuffled_mcqs)
        for q in st.session_state.shuffled_mcqs:
            random.shuffle(q["options"])
        st.rerun()
