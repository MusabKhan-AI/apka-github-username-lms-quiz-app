import random
from groq import Groq
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI & Data Structures LMS Quiz Portal",
    page_icon="📚",
    layout="centered",
)

# Initialize Groq client using Streamlit Secrets safely
try:
  groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
  groq_client = None

# MCQs Data Bank
MCQS_DATA = [
    {
        "question": "What is a strategic environment in the lecture's description?",
        "options": [
            "Deterministic except for the actions of other agents",
            "Always fully observable",
            "A static environment with no actions",
            "An environment with only continuous values",
        ],
        "answer": "Deterministic except for the actions of other agents",
        "reason": (
            "Strategic environment mein doosre agents ki actions ke ilawa"
            " environment deterministic hota hai."
        ),
    },
    {
        "question": "What is a performance measure?",
        "options": [
            "A device that moves the agent",
            "An objective criterion for success of an agent's behavior",
            "A record of source code length",
            "The complete percept history",
        ],
        "answer": (
            "An objective criterion for success of an agent's behavior"
        ),
        "reason": (
            "Performance measure agent ke behavior ki success ka objective"
            " criterion hota hai."
        ),
    },
    {
        "question": (
            "Which is an example of an artificial but potentially complex"
            " environment?"
        ),
        "options": [
            "Flight simulator",
            "Video game",
            "Internet",
            "All of the above",
        ],
        "answer": "All of the above",
        "reason": (
            "Flight simulator, video game aur internet sab artificial aur"
            " complex environments ki misalein hain."
        ),
    },
    {
        "question": (
            "Which is an example of a vacuum-cleaner percept shown in the"
            " lecture?"
        ),
        "options": ["[A, Dirty]", "[Motor, Fast]", "[Sensor, Off]", "[B, Left]"],
        "answer": "[A, Dirty]",
        "reason": "[A, Dirty] vacuum cleaner ki percept ki ek misaal hai.",
    },
    {
        "question": "Which PEAS element enables the agent to detect information?",
        "options": ["Actuators", "Sensors", "Environment", "Utility"],
        "answer": "Sensors",
        "reason": "Sensors ki madad se agent environment se information detect karta hai.",
    },
    {
        "question": "What must an agent do to use the entire percept sequence?",
        "options": [
            "Remember all percepts in the sequence",
            "Ignore previous percepts in every case",
            "Remove its architecture",
            "Use no program",
        ],
        "answer": "Remember all percepts in the sequence",
        "reason": (
            "Poori percept sequence ko use karne ke liye agent ko tamam percepts"
            " yaad rakhne parte hain."
        ),
    },
    {
        "question": (
            "Which can cause partial observability according to the lecture?"
        ),
        "options": [
            "Noisy sensors",
            "Missing parts of information",
            "Both noisy sensors and missing parts",
            "A title page",
        ],
        "answer": "Both noisy sensors and missing parts",
        "reason": (
            "Noisy sensors aur missing information dono ki wajah se partial"
            " observability ho sakti hai."
        ),
    },
    {
        "question": (
            "Which statement best captures the distinction between agent"
            " function and agent program?"
        ),
        "options": [
            (
                "Function specifies the percept-to-action mapping; program"
                " implements it"
            ),
            "Function is hardware and program is the environment",
            "They are both actuators",
            "The function only stores page numbers",
        ],
        "answer": (
            "Function specifies the percept-to-action mapping; program"
            " implements it"
        ),
        "reason": (
            "Agent function mapping define karti hai jabke agent program usay"
            " implement karta hai."
        ),
    },
    {
        "question": "Which notation is used for the agent function in the slides?",
        "options": ["f: A → P*", "f: P* → A", "f: S → E", "f: E → P"],
        "answer": "f: P* → A",
        "reason": "Agent function ko f: P* → A se represent kiya jata hai.",
    },
    {
        "question": (
            "Which of the following is NOT listed as one of the Lecture 05"
            " structure components?"
        ),
        "options": [
            "Agent behavior",
            "Agent program",
            "Agent function",
            "Weather forecast",
        ],
        "answer": "Weather forecast",
        "reason": (
            "Weather forecast lecture structure components mein shamil nahi"
            " hai."
        ),
    },
    {
        "question": (
            "Which condition makes an environment discrete according to the"
            " slides?"
        ),
        "options": [
            (
                "Limited distinct states with clearly defined percepts and"
                " actions"
            ),
            "Continuous values at every moment",
            "No defined states or actions",
            "Unpredictable outcomes only",
        ],
        "answer": (
            "Limited distinct states with clearly defined percepts and actions"
        ),
        "reason": (
            "Limited distinct states aur defined actions hone par environment"
            " discrete hota hai."
        ),
    },
    {
        "question": "According to the lecture, omniscience in reality is:",
        "options": [
            "Always guaranteed",
            "Impossible in reality",
            "The same as autonomy",
            "Required for every agent",
        ],
        "answer": "Impossible in reality",
        "reason": "Asal zindagi mein omniscience (sab kuch janna) namumkin hai.",
    },
    {
        "question": "A cooperative multiagent environment relies on:",
        "options": [
            "Cooperation between multiple AI agents",
            "Only one agent",
            "No communication or coordination ever",
            "Infinite knowledge",
        ],
        "answer": "Cooperation between multiple AI agents",
        "reason": (
            "Cooperative environment multiple agents ke darmiyan ta'awun par"
            " base karta hai."
        ),
    },
    {
        "question": (
            "In a competitive multiagent environment, agents are set against"
            " each other to:"
        ),
        "options": [
            "Optimize a specific outcome",
            "Share one identical action",
            "Avoid all decisions",
            "Remove the environment",
        ],
        "answer": "Optimize a specific outcome",
        "reason": (
            "Competitive environment mein agents mukabala karke apne outcome ko"
            " optimize karte hain."
        ),
    },
    {
        "question": "What does the agent program implement?",
        "options": [
            "Agent function",
            "Physical environment",
            "Performance measure only",
            "The user's assignment",
        ],
        "answer": "Agent function",
        "reason": "Agent program asal mein agent function ko implement karta hai.",
    },
    {
        "question": (
            "According to the lecture, an agent perceives its environment"
            " through which components?"
        ),
        "options": [
            "Actuators",
            "Sensors",
            "Programs only",
            "Performance measures",
        ],
        "answer": "Sensors",
        "reason": "Agent sensors ke zariye environment ko perceive karta hai.",
    },
    {
        "question": "How does the lecture describe inference in deep learning?",
        "options": [
            "Inference in layers",
            "Inference without computation",
            "Inference only by hand",
            "Inference by page numbering",
        ],
        "answer": "Inference in layers",
        "reason": "Deep learning mein inference layers ke zariye hoti hai.",
    },
    {
        "question": "What is a percept history or percept sequence?",
        "options": [
            "Only the next action",
            "The complete history of what has been perceived",
            "Only the agent's hardware",
            "A list of actuators",
        ],
        "answer": "The complete history of what has been perceived",
        "reason": "Percept history ab tak perceive ki gayi tamam cheezon ka record hai.",
    },
    {
        "question": "In the formula for an agent, architecture refers to:",
        "options": [
            "The computing device/hardware the agent runs on",
            "Only the software code",
            "The performance measure",
            "The action sequence",
        ],
        "answer": "The computing device/hardware the agent runs on",
        "reason": "Architecture us hardware ya computing device ko kehte hain jis par agent chalta hai.",
    },
    {
        "question": "What is autonomy in the context of intelligent agents?",
        "options": [
            "Relying solely on prior built-in knowledge without learning",
            (
                "The extent to which an agent's behavior depends on its own"
                " experience"
            ),
            "Having no sensors at all",
            "Executing random actions forever",
        ],
        "answer": (
            "The extent to which an agent's behavior depends on its own"
            " experience"
        ),
        "reason": (
            "Autonomy ka matlab hai ke agent ka behavior uske apne tajurbe"
            " par kitna depend karta hai."
        ),
    },
]

# Session state initialization
if "submitted" not in st.session_state:
  st.session_state.submitted = False
if "current_index" not in st.session_state:
  st.session_state.current_index = 0
if "user_answers" not in st.session_state:
  st.session_state.user_answers = {}
if "shuffled_mcqs" not in st.session_state:
  shuffled = list(MCQS_DATA)
  random.shuffle(shuffled)
  st.session_state.shuffled_mcqs = shuffled[:50]

st.title("📚 AI & Data Structures LMS Quiz Portal")
st.markdown("NTS / ECAT style test portal with instant review and AI Tutor.")

# Main Quiz Interface
if not st.session_state.submitted:
  mcqs = st.session_state.shuffled_mcqs
  idx = st.session_state.current_index
  total = len(mcqs)

  st.subheader(f"Question {idx + 1} of {total}")
  current_q = mcqs[idx]

  st.write(f"**{current_q['question']}**")

  prev_ans = st.session_state.user_answers.get(idx, None)

  # Safe index calculation for radio button
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
      if st.button("✅ Submit Test", type="primary"):
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
                f"Correct Answer: {correct_ans}\nExplain in Roman Hinglish"
                " why the correct answer is right and why student's choice"
                " might be wrong."
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
      st.warning(
          "Groq API key not configured in Streamlit Secrets. Add"
          " GROQ_API_KEY to enable AI Tutor."
      )

    st.markdown("---")

  st.balloons()
  st.subheader(f"Final Score: {score} / {total} ({(score/total)*100:.2f}%)")

  if st.button("🔄 Retake Quiz"):
    st.session_state.submitted = False
    st.session_state.current_index = 0
    st.session_state.user_answers = {}
    random.shuffle(st.session_state.shuffled_mcqs)
    st.rerun()
