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

# MCQs Data Bank (Combined from all lectures with questions, options, answers, and reasons)
MCQS_DATA = [
    # --- Lectures 03, 04 & 05 MCQs ---
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
        "reason": (
            "Sensors environment se information receive karte hain; actuators"
            " actions perform karte hain."
        ),
    },
    {
        "question": "An agent acts upon its environment through which components?",
        "options": [
            "Sensors",
            "Percepts",
            "Actuators",
            "Knowledge bases only",
        ],
        "answer": "Actuators",
        "reason": (
            "Actuators woh parts hain jin ke zariye agent environment par"
            " action karta hai."
        ),
    },
    {
        "question": (
            "Which statement best describes an intelligent agent in the"
            " lecture?"
        ),
        "options": [
            "It only stores data",
            (
                "It perceives, acts autonomously toward goals, and may"
                " learn"
            ),
            "It only follows a fixed timetable",
            "It must always be a human",
        ],
        "answer": (
            "It perceives, acts autonomously toward goals, and may learn"
        ),
        "reason": (
            "Intelligent agent environment ko perceive karta, goals ke liye"
            " actions leta aur learning bhi kar sakta hai."
        ),
    },
    {
        "question": "Which are examples of sensors of a human agent?",
        "options": [
            "Hands and legs",
            "Eyes and ears",
            "Motors and wheels",
            "Mouth and feet only",
        ],
        "answer": "Eyes and ears",
        "reason": "Lecture mein human sensors ki examples eyes, ears aur doosre organs di gayi hain.",
    },
    {
        "question": "Which are examples of actuators of a human agent?",
        "options": [
            "Eyes and ears",
            "Cameras and infrared range finders",
            "Hands, legs, mouth, and other body parts",
            "Knowledge base and inference engine",
        ],
        "answer": "Hands, legs, mouth, and other body parts",
        "reason": "Hands, legs, mouth aur body parts insaan ko actions perform karne mein madad dete hain.",
    },
    {
        "question": "Which pair is listed as sensors of a robotic agent?",
        "options": [
            "Cameras and infrared range finders",
            "Hands and legs",
            "Motors and wheels",
            "Mouth and ears",
        ],
        "answer": "Cameras and infrared range finders",
        "reason": "Slides mein robotic agent ke sensors cameras aur infrared range finders bataye gaye hain.",
    },
    {
        "question": "Which component is listed as an actuator of a robotic agent?",
        "options": [
            "Camera",
            "Infrared range finder",
            "Various motors",
            "Percept sequence",
        ],
        "answer": "Various motors",
        "reason": "Robotic agent ke actuators mein various motors shamil hain.",
    },
    {
        "question": "What does the agent function map?",
        "options": [
            "Actions to sensors",
            "Percept histories to actions",
            "Programs to environments",
            "Actuators to knowledge",
        ],
        "answer": "Percept histories to actions",
        "reason": "Agent function percept history ya sequence ko input bana kar action select karta hai.",
    },
    {
        "question": "Which notation is used for the agent function in the slides?",
        "options": ["f: A → P*", "f: P* → A", "f: S → E", "f: E → P"],
        "answer": "f: P* → A",
        "reason": "Slides mein agent function ki notation f: P* → A hai: P* percept sequences aur A actions ko show karta hai.",
    },
    {
        "question": "What is a percept?",
        "options": [
            "The agent's input that forms the basis for its actions",
            "The physical device running a program",
            "The agent's final score only",
            "An actuator movement",
        ],
        "answer": "The agent's input that forms the basis for its actions",
        "reason": "Percept agent ko milne wali input information hai jo action lene ki bunyaad banti hai.",
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
        "reason": "Percept sequence se murad agent ne ab tah jo kuch perceive kiya us ki complete history hai.",
    },
    {
        "question": "What is an agent program?",
        "options": [
            "A physical sensor",
            "An implementation of the agent function",
            "The environment itself",
            "A performance measure",
        ],
        "answer": "An implementation of the agent function",
        "reason": "Agent program programming language mein agent function ko implement ya execute karta hai.",
    },
    {
        "question": "Where does the agent program run?",
        "options": [
            "Only inside a sensor",
            "On the physical architecture",
            "Inside the performance measure",
            "Only in the environment",
        ],
        "answer": "On the physical architecture",
        "reason": "Agent program physical architecture par run karta hai aur agent function ko produce/implement karta hai.",
    },
    {
        "question": "Which formula is given for an agent?",
        "options": [
            "Agent = sensors - actuators",
            "Agent = architecture + program",
            "Agent = percepts + environment",
            "Agent = program - architecture",
        ],
        "answer": "Agent = architecture + program",
        "reason": "Lecture ke mutabiq agent banane ke liye architecture aur program dono chahiye.",
    },
    {
        "question": "In the vacuum-cleaner world, how many named squares are specified?",
        "options": [
            "One: A",
            "Two: A and B",
            "Three: A, B, and C",
            "Four: A, B, C, and D",
        ],
        "answer": "Two: A and B",
        "reason": "Vacuum-cleaner environment mein do squares, A aur B, diye gaye hain.",
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
        "question": "Which set contains the vacuum agent's listed actions?",
        "options": [
            "Up, Down, Open, Close",
            "Left, Right, Suck, NoOp",
            "Run, Stop, Learn, Forget",
            "Sense, Think, Store, Print",
        ],
        "answer": "Left, Right, Suck, NoOp",
        "reason": "Vacuum agent ke actions Left, Right, Suck aur NoOp hain.",
    },
    {
        "question": "What should an agent strive to do, according to the rational-agent slide?",
        "options": [
            "Do the right thing based on what it can perceive and do",
            "Always perform the same action",
            "Know every future outcome",
            "Avoid using sensors",
        ],
        "answer": "Do the right thing based on what it can perceive and do",
        "reason": "Rational agent available percepts aur possible actions ko dekh kar munasib action choose karta hai.",
    },
    {
        "question": "What is a performance measure?",
        "options": [
            "A device that moves the agent",
            "An objective criterion for success of an agent's behavior",
            "A record of source code length",
            "The complete percept history",
        ],
        "answer": "An objective criterion for success of an agent's behavior",
        "reason": "Performance measure agent ke behavior ki success ko objectively assess karta hai.",
    },
    {
        "question": "A rational agent selects actions that maximize its expected what?",
        "options": [
            "File size",
            "Utility",
            "Number of sensors",
            "Program length",
        ],
        "answer": "Utility",
        "reason": "Rational agent expected utility ya performance ko maximize karne ki koshish karta hai.",
    },
    {
        "question": "What does omniscience mean in the lecture?",
        "options": [
            "Learning from experience",
            "All-knowing with infinite knowledge",
            "Using multiple agents",
            "Acting without sensors",
        ],
        "answer": "All-knowing with infinite knowledge",
        "reason": "Omniscience ka matlab har cheez ka ilm ya infinite knowledge hona hai.",
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
        "reason": "Slides wazeh karti hain ke real world mein omniscience mumkin nahi.",
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
        "reason": "Lecture flight simulators, video games aur Internet ko artificial complex environments ki examples ke taur par deti hai.",
    },
    {
        "question": "What are software agents also called in the lecture?",
        "options": [
            "Softbots or software robots",
            "Physical actuators",
            "Percept sensors",
            "Inference measures",
        ],
        "answer": "Softbots or software robots",
        "reason": "Software agents ko software robots ya softbots bhi kaha gaya hai.",
    },
    {
        "question": "In PEAS, what does P stand for?",
        "options": [
            "Program",
            "Performance measure",
            "Percept sequence",
            "Probability",
        ],
        "answer": "Performance measure",
        "reason": "PEAS mein P ka matlab Performance measure hai.",
    },
    {
        "question": "In PEAS, what does E stand for?",
        "options": ["Environment", "Evaluation", "Episode", "Engine"],
        "answer": "Environment",
        "reason": "PEAS ka E environment hai.",
    },
    {
        "question": "In PEAS, what does A stand for?",
        "options": ["Autonomy", "Architecture", "Actuators", "Actions history"],
        "answer": "Actuators",
        "reason": "PEAS mein A actuators ko represent karta hai.",
    },
    {
        "question": "In PEAS, what does S stand for?",
        "options": ["Sensors", "Software", "Sequence", "State"],
        "answer": "Sensors",
        "reason": "PEAS ka S sensors hain.",
    },

    # --- Machine Learning Lectures 01 & 02 MCQs ---
    {
        "question": "What is the relationship between AI and ML in the lecture?",
        "options": [
            "AI and ML mean exactly the same",
            "AI is a subset of ML",
            "ML is a subset of AI",
            "They are unrelated",
        ],
        "answer": "ML is a subset of AI",
        "reason": "AI broader field hai; ML us ka subset hai.",
    },
    {
        "question": (
            "Who coined the term Machine Learning in 1959, according to the"
            " slides?"
        ),
        "options": [
            "Arthur Samuel",
            "Geoffrey Hinton",
            "Alan Turing",
            "John McCarthy",
        ],
        "answer": "Arthur Samuel",
        "reason": "Lecture history section 1959 mein Arthur Samuel ka naam deti hai.",
    },
    {
        "question": "What did Arthur Samuel's early checkers program calculate?",
        "options": [
            "Number of players",
            "Computer speed",
            "Board size",
            "Winning chance for each side",
        ],
        "answer": "Winning chance for each side",
        "reason": "Early program checkers mein dono sides ke winning chances calculate karta tha.",
    },
    {
        "question": "Which description best defines machine learning?",
        "options": [
            "Building computer hardware",
            (
                "Learning patterns from data to perform tasks without explicit"
                " task-by-task rules"
            ),
            "Only following fixed instructions",
            "Only storing records",
        ],
        "answer": (
            "Learning patterns from data to perform tasks without explicit"
            " task-by-task rules"
        ),
        "reason": "ML data se patterns seekhta aur unseen data par generalize karta hai.",
    },
    {
        "question": "In the T/E/P definition, what does E represent?",
        "options": ["Evaluation score", "Error rate", "Environment only", "Experience"],
        "answer": "Experience",
        "reason": "E experience/training examples ko represent karta hai.",
    },
    {
        "question": "In handwriting recognition, what is task T?",
        "options": [
            "Recognizing and classifying handwritten words in images",
            "Collecting computer parts",
            "Counting files",
            "Measuring image size",
        ],
        "answer": "Recognizing and classifying handwritten words in images",
        "reason": "Slides mein T handwritten words ki recognition aur classification hai.",
    },
    {
        "question": "For handwriting recognition, what is performance measure P?",
        "options": [
            "Percentage of words correctly classified",
            "Internet speed",
            "Number of users",
            "Number of stored images",
        ],
        "answer": "Percentage of words correctly classified",
        "reason": "P correct classified words ka percentage hai.",
    },
    {
        "question": (
            "Which learning type uses labelled input-output examples?"
        ),
        "options": [
            "Semi-supervised only",
            "Reinforcement",
            "Supervised",
            "Unsupervised",
        ],
        "answer": "Supervised",
        "reason": "Supervised learning mein input ke sath correct label/output hota hai.",
    },
    {
        "question": (
            "An agent tries actions and learns which actions produce the most"
            " reward. This is:"
        ),
        "options": [
            "Supervised learning",
            "Reinforcement learning",
            "Unsupervised learning",
            "Data preparation",
        ],
        "answer": "Reinforcement learning",
        "reason": "Agent trial and reward se useful actions seekhta hai.",
    },
    {
        "question": "What is the main role of training data?",
        "options": [
            "It replaces the model",
            "The model learns patterns from it",
            "It contains only final scores",
            "It is used only after deployment",
        ],
        "answer": "The model learns patterns from it",
        "reason": "Training data woh examples hain jin se model learn karta hai.",
    },
    {
        "question": "Why keep test data separate from training data?",
        "options": [
            "To let model memorize test answers",
            "To evaluate on data not used for learning",
            "To avoid evaluation",
            "To replace all features",
        ],
        "answer": "To evaluate on data not used for learning",
        "reason": "Separate test set unseen data par performance evaluate karta hai.",
    },
    {
        "question": "How many major steps are listed in the ML life cycle?",
        "options": ["Five", "Ten", "Seven", "Six"],
        "answer": "Seven",
        "reason": "Slides seven steps list karti hain.",
    },

    # --- Lectures 06, 07 & 08 MCQs ---
    {
        "question": "Which statement best describes a simple reflex agent?",
        "options": [
            "It chooses actions using only the current percept",
            "It stores every past percept permanently",
            "It always searches several future action sequences",
            "It learns a new model after every action",
        ],
        "answer": "It chooses actions using only the current percept",
        "reason": "Simple reflex agent current percept par react karta hai; percept history ko use nahi karta.",
    },
    {
        "question": (
            "A room-cleaning agent follows: 'If room is dirty, then clean.' What"
            " is this an example of?"
        ),
        "options": [
            "A goal test",
            "A condition-action rule",
            "A path-cost function",
            "A learning element",
        ],
        "answer": "A condition-action rule",
        "reason": "Rule mein condition (room dirty) true hoti hai to action (clean) trigger hota hai.",
    },
    {
        "question": (
            "Which additional capability distinguishes a model-based reflex"
            " agent from a simple reflex agent?"
        ),
        "options": [
            "It maintains an internal state",
            "It never uses current percepts",
            "It always maximizes a numerical utility",
            "It must know the final goal",
        ],
        "answer": "It maintains an internal state",
        "reason": "Model-based agent percept history ko internal state mein maintain karta hai.",
    },
    {
        "question": "What information is essential for a goal-based agent to choose actions?",
        "options": [
            "A description of desirable situations",
            "Only a fixed condition-action table",
            "Only the number of sensors",
            "A list of past rewards without a goal",
        ],
        "answer": "A description of desirable situations",
        "reason": "Goal agent ko pata hona chahiye ke desired situation/goal kya hai.",
    },
    {
        "question": "What does a utility-based agent try to maximize?",
        "options": [
            "The performance measure or utility",
            "The number of percepts forgotten",
            "The number of condition rules",
            "The size of the state space only",
        ],
        "answer": "The performance measure or utility",
        "reason": "Utility agent performance measure ko maximize karne wali solution choose karta hai.",
    },
    {
        "question": "In a state-space graph, what do nodes and links represent?",
        "options": [
            "Nodes are states; links represent actions",
            "Nodes are actions; links are goals",
            "Nodes are costs; links are percepts",
            "Nodes are agents; links are sensors",
        ],
        "answer": "Nodes are states; links represent actions",
        "reason": "Lecture graph mein nodes states aur links/actions ke darmiyan connections hotay hain.",
    },
    {
        "question": "What is path cost in the Romania travel problem?",
        "options": [
            "The sum of distances travelled",
            "The number of cities in the country",
            "The agent's memory size",
            "The number of goals",
        ],
        "answer": "The sum of distances travelled",
        "reason": "Lecture path cost ko travelled distances ke sum se explain karti hai.",
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
  # Shuffle questions order
  random.shuffle(shuffled)
  # Shuffle option/answer sequence for each question so answers are mixed up ("uper nichy")
  for q in shuffled:
    random.shuffle(q["options"])
  st.session_state.shuffled_mcqs = shuffled

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
    for q in st.session_state.shuffled_mcqs:
      random.shuffle(q["options"])
    st.rerun()
