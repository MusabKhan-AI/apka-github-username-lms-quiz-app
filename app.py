import random
from groq import Groq
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI & ML LMS Quiz Portal",
    page_icon="📚",
    layout="centered",
)

# Initialize Groq client using Streamlit Secrets safely
try:
  groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
  groq_client = None

# MCQs Data based on provided AI and ML Lectures / Slides
MCQS_DATA = [
    {
        "question": "Who coined the term 'Machine Learning' in 1959?",
        "options": ["John McCarthy", "Arthur Samuel", "Alan Turing", "Tom Mitchell"],
        "answer": "Arthur Samuel",
        "reason": (
            "Arthur Samuel ne 1959 ma 'Machine Learning' term coin kari hati"
            "[cite: 10]."
        ),
    },
    {
        "question": (
            "What is the first step of the Machine Learning life cycle?"
        ),
        "options": [
            "Data Preparation",
            "Gathering Data",
            "Data Wrangling",
            "Train Model",
        ],
        "answer": "Gathering Data",
        "reason": (
            "ML life cycle no pehlo step data gather karvo chhe[cite: 2]."
        ),
    },
    {
        "question": (
            "Which step involves cleaning and converting raw data into a"
            " usable format?"
        ),
        "options": [
            "Data Wrangling",
            "Deployment",
            "Testing",
            "Model Training",
        ],
        "answer": "Data Wrangling",
        "reason": (
            "Data wrangling ma raw data ne clean ane usable format ma convert"
            " karva ma aave chhe[cite: 4]."
        ),
    },
    {
        "question": (
            "In PEAS description for an automated taxi, what do the sensors"
            " include?"
        ),
        "options": [
            "Steering & brakes",
            "Accelerators",
            "Camera, GPS, IR sensors",
            "Display screen",
        ],
        "answer": "Camera, GPS, IR sensors",
        "reason": (
            "Automated taxi ma camera, GPS ane IR sensors sensors ma aave chhe"
            "[cite: 32]."
        ),
    },
    {
        "question": (
            "Which type of agent selects actions that maximize expected"
            " utility?"
        ),
        "options": [
            "Simple Reflex Agent",
            "Utility-based Agent",
            "Goal-based Agent",
            "Learning Agent",
        ],
        "answer": "Utility-based Agent",
        "reason": (
            "Utility-based agent performance measure ne maximize karva mate"
            " utility use kare chhe[cite: 68]."
        ),
    },
    {
        "question": (
            "How many major steps are involved in the Machine Learning life"
            " cycle?"
        ),
        "options": ["5", "6", "7", "8"],
        "answer": "7",
        "reason": (
            "Machine learning life cycle ma 7 major steps hoy chhe[cite: 2]."
        ),
    },
    {
        "question": "Machine Learning is a subset of which broader field?",
        "options": [
            "Data Science",
            "Artificial Intelligence",
            "Computer Vision",
            "Robotics",
        ],
        "answer": "Artificial Intelligence",
        "reason": (
            "Machine learning e Artificial Intelligence (AI) no subset chhe"
            "[cite: 10, 31]."
        ),
    },
    {
        "question": (
            "Which data type consists of input data without labeled"
            " responses?"
        ),
        "options": [
            "Supervised data",
            "Unlabeled data",
            "Labeled data",
            "Test data",
        ],
        "answer": "Unlabeled data",
        "reason": (
            "Unlabeled data ma target responses ya labels hotah nathi[cite: 22]."
        ),
    },
    {
        "question": (
            "What does PEAS stand for in task environment specification?"
        ),
        "options": [
            "Performance, Environment, Actuators, Sensors",
            "Program, Execution, Action, State",
            "Prediction, Evaluation, Analysis, System",
            "Processing, Environment, Algorithm, Search",
        ],
        "answer": "Performance, Environment, Actuators, Sensors",
        "reason": (
            "PEAS stands for Performance measure, Environment, Actuators,"
            " Sensors[cite: 32]."
        ),
    },
    {
        "question": (
            "Which environment type has an agent's sensors give complete"
            " state access at each point in time?"
        ),
        "options": [
            "Partially Observable",
            "Fully Observable",
            "Stochastic",
            "Dynamic",
        ],
        "answer": "Fully Observable",
        "reason": (
            "Fully observable environment ma sensors complete state access"
            " aape chhe[cite: 33]."
        ),
    },
    {
        "question": (
            "In a decision tree or classification task, each episode is"
            " independent of previous actions in a(n)..."
        ),
        "options": [
            "Sequential environment",
            "Episodic environment",
            "Static environment",
            "Continuous environment",
        ],
        "answer": "Episodic environment",
        "reason": (
            "Episodic environment ma next episode paila na actions par depend"
            " nathi kartu[cite: 33]."
        ),
    },
    {
        "question": (
            "Which agent component tells the learning element how well the"
            " agent is doing?"
        ),
        "options": ["Critic", "Problem Generator", "Actuator", "Sensor"],
        "answer": "Critic",
        "reason": (
            "Learning agent ma Critic performance standard mujab feedback aape"
            " chhe[cite: 74]."
        ),
    },
    {
        "question": "The 8-puzzle is a classic example of a problem solved in:",
        "options": [
            "Problem Formulation and Search",
            "Unsupervised Learning",
            "Reinforcement Learning",
            "Neural Networks",
        ],
        "answer": "Problem Formulation and Search",
        "reason": (
            "8-puzzle e problem formulation and search agents no example chhe"
            "[cite: 34, 50]."
        ),
    },
    {
        "question": (
            "What type of learning involves an agent discovering actions that"
            " yield the most reward?"
        ),
        "options": [
            "Supervised Learning",
            "Unsupervised Learning",
            "Reinforcement Learning",
            "Semi-Supervised Learning",
        ],
        "answer": "Reinforcement Learning",
        "reason": (
            "Reinforcement learning ma agent rewards and punishments thi"
            " learn kare chhe[cite: 23]."
        ),
    },
    {
        "question": (
            "Which properties of data refer to the scale and rate of data"
            " streaming respectively?"
        ),
        "options": [
            "Volume and Velocity",
            "Variety and Veracity",
            "Value and Viability",
            "Integrity and Security",
        ],
        "answer": "Volume and Velocity",
        "reason": (
            "Volume scale of data chhe ane Velocity rate of data streaming"
            " chhe[cite: 28]."
        ),
    },
]

# --- LOGIN SYSTEM ---
if "logged_in" not in st.session_state:
  st.session_state.logged_in = False

if not st.session_state.logged_in:
  st.markdown(
      "<h2 style='text-align: center;'>🔐 AI & ML Portal Login</h2>",
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
    "<h1 style='text-align: center; color: #1E3A8A;'>🤖 AI & Machine Learning"
    " LMS Portal</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #4B5563;'>Professional Assessment"
    " Portal</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# Main Quiz Interface (Timer removed)
if not st.session_state.submitted:
  col_title, col_sub = st.columns([2, 1])
  with col_title:
    st.markdown("📝 **Quiz in Progress (No Time Limit)**")
  with col_sub:
    if st.button("🚀 Early Submit Test"):
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
                f"Correct Answer: {correct_ans}\nExplain why the correct"
                " answer is right and why student's choice might be wrong."
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
    random.shuffle(st.session_state.shuffled_mcqs)
    for q in st.session_state.shuffled_mcqs:
      random.shuffle(q["options"])
    st.rerun()
