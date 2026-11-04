import random
from groq import Groq
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Linear Algebra Pre-Board LMS Portal",
    page_icon="📚",
    layout="centered",
)

# Initialize Groq client using Streamlit Secrets safely
try:
  groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
  groq_client = None

# Custom CSS for Professional UI, White Background, and NTS-style Question Palette Circles
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFFFFF;
        color: #111111;
    }
    .palette-container {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-bottom: 20px;
    }
    .palette-circle {
        width: 35px;
        height: 35px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 14px;
        border: 2px solid #ccc;
        cursor: pointer;
    }
    .circle-answered {
        background-color: #28a745;
        color: white;
        border-color: #28a745;
    }
    .circle-unanswered {
        background-color: #f8f9fa;
        color: #333;
        border-color: #ced4da;
    }
    .circle-current {
        border-color: #007bff;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 30 Mixed Difficult MCQs extracted from Linear Algebra PDF
MCQS_DATA = [
    {
        "question": "A square matrix that is both upper and lower triangular must be",
        "options": [
            "A matrix with no zeros",
            "A diagonal matrix",
            "A 1 x n matrix",
            "A non-square matrix",
        ],
        "answer": "A diagonal matrix",
        "reason": (
            "Upper aur lower triangular dono properties satisfy karne wali"
            " square matrix sirf diagonal matrix ho sakti hai[cite: 36]."
        ),
    },
    {
        "question": "The diagonal entries of a real skew-symmetric matrix are",
        "options": ["All equal to 1", "All zero", "All positive", "All equal to 2"],
        "answer": "All zero",
        "reason": (
            "Real skew-symmetric matrix ke main diagonal ke tamam entries zero"
            " hotay hain[cite: 36]."
        ),
    },
    {
        "question": "A square matrix A is involutory if",
        "options": ["A^2 = A", "A^2 = O", "A^2 = I", "A^T = -A"],
        "answer": "A^2 = I",
        "reason": (
            "Involutory matrix woh hoti hai jiska square identity matrix ke"
            " barabar ho[cite: 37]."
        ),
    },
    {
        "question": (
            "The product AB of matrices A (2x3) and B (3x4) has the order"
        ),
        "options": ["3 x 3", "4 x 2", "2 x 4", "2 x 3"],
        "answer": "2 x 4",
        "reason": (
            "Matrix multiplication mein (m x k) aur (k x n) ka product (m x n)"
            " order deta hai[cite: 38]."
        ),
    },
    {
        "question": "In general, matrix multiplication is",
        "options": [
            "Always commutative",
            "Defined for any two matrices",
            "Possible only for diagonal matrices",
            "Not commutative (AB != BA)",
        ],
        "answer": "Not commutative (AB != BA)",
        "reason": (
            "Matrix multiplication aam tor par commutative nahi hoti[cite: 38]."
        ),
    },
    {
        "question": "The determinant of [[2, 1], [4, 2]] is",
        "options": ["8", "4", "0", "2"],
        "answer": "0",
        "reason": "det = (2*2) - (1*4) = 4 - 4 = 0[cite: 40].",
    },
    {
        "question": (
            "If det(A) = 0, then the matrix A is classified as which of the"
            " following?"
        ),
        "options": [
            "Invertible",
            "The identity matrix",
            "Always symmetric",
            "Singular (no inverse)",
        ],
        "answer": "Singular (no inverse)",
        "reason": (
            "Agar determinant zero ho toh matrix singular hoti hai aur uska"
            " inverse exist nahi karta[cite: 40]."
        ),
    },
    {
        "question": "The cofactor of entry a_ij is given by the formula",
        "options": [
            "C_ij = (-1)^(i+j) * M_ij",
            "C_ij = M_ij + 1",
            "C_ij = (-1)^(i*j) * M_ij",
            "C_ij = i * j * M_ij",
        ],
        "answer": "C_ij = (-1)^(i+j) * M_ij",
        "reason": "Cofactor formula mein (-1 raise to power i+j) multiply hota hai minor ke sath[cite: 41].",
    },
    {
        "question": (
            "For A = [[3, 1, -4], [2, 5, 6], [1, 4, 8]], the minor M_11 is"
        ),
        "options": ["26", "-16", "16", "40"],
        "answer": "16",
        "reason": "det([[5, 6], [4, 8]]) = (5*8) - (6*4) = 40 - 24 = 16[cite: 41].",
    },
    {
        "question": "If any two rows of a square matrix are interchanged, the determinant",
        "options": [
            "Changes its sign",
            "Stays the same",
            "Becomes zero",
            "Doubles",
        ],
        "answer": "Changes its sign",
        "reason": "Do rows interchanging se determinant ka sign invert ho jata hai[cite: 42].",
    },
    {
        "question": "If two rows of a square matrix are identical, its determinant is",
        "options": ["1", "Equal to the trace", "0", "-1"],
        "answer": "0",
        "reason": "Identical rows hone par determinant hamesha zero hota hai[cite: 42].",
    },
    {
        "question": (
            "In machine learning, two features that are exact copies of each"
            " other cause"
        ),
        "options": [
            "A faster model",
            "A larger determinant",
            "Multicollinearity (det = 0)",
            "An identity matrix",
        ],
        "answer": "Multicollinearity (det = 0)",
        "reason": "Exact copy features ki wajah se rows dependent ho jati hain aur determinant zero ho jata hai[cite: 43].",
    },
    {
        "question": (
            "The matrix [[-1, 0], [0, 1]] has det -1, which indicates that the"
            " image transformation is"
        ),
        "options": [
            "Stretched 6 times",
            "Squashed into a line",
            "Destroyed",
            "Flipped (mirror image) with the same area",
        ],
        "answer": "Flipped (mirror image) with the same area",
        "reason": "Negative determinant reflection ya mirror image ko represent karta hai[cite: 44].",
    },
    {
        "question": (
            "A matrix like [[1, 2], [2, 4]] has det 0, meaning the image is"
        ),
        "options": [
            "Doubled in area",
            "Rotated only",
            "Flipped only",
            "Squashed flat into a line",
        ],
        "answer": "Squashed flat into a line",
        "reason": "Determinant zero hone par space squash ho kar lower dimension mein convert ho jati hai[cite: 44].",
    },
    {
        "question": (
            "To avoid overflow or underflow issues, AI libraries often use"
            " log-determinant via"
        ),
        "options": [
            "numpy.linalg.slogdet",
            "numpy.linalg.sumdet",
            "numpy.matrix.minor",
            "numpy.linalg.cofactor",
        ],
        "answer": "numpy.linalg.slogdet",
        "reason": "NumPy mein slogdet function sign aur log-determinant compute karne ke liye use hota hai[cite: 44].",
    },
    {
        "question": "Every homogeneous system of linear equations AX = 0 always has",
        "options": [
            "No solution",
            "Exactly two solutions",
            "At least the trivial solution",
            "Only nontrivial solutions",
        ],
        "answer": "At least the trivial solution",
        "reason": "Homogeneous system ka trivial solution (all zeros) hamesha exist karta hai[cite: 44].",
    },
    {
        "question": "If two lines in a plane are parallel and distinct, the linear system has",
        "options": [
            "One solution",
            "Two solutions",
            "Infinitely many solutions",
            "No solution",
        ],
        "answer": "No solution",
        "reason": "Parallel lines kabhi intersect nahi karti, isliye koi solution nahi hota[cite: 45].",
    },
    {
        "question": "A square matrix A is idempotent if it satisfies which condition?",
        "options": ["A^2 = I", "A^2 = A", "A^T = A", "A^2 = O"],
        "answer": "A^2 = A",
        "reason": "Idempotent matrix woh hoti hai jiska square khud matrix ke barabar ho[cite: 37].",
    },
    {
        "question": "The trace of the identity matrix I_4 is equal to",
        "options": ["4", "1", "0", "16"],
        "answer": "4",
        "reason": "Identity matrix ke diagonal elements ka sum uski dimension hoti hai[cite: 37].",
    },
    {
        "question": "The transpose of a product of two matrices (AB)^T is equal to",
        "options": ["A^T B^T", "B^T A^T", "AB", "BA"],
        "answer": "B^T A^T",
        "reason": "Product ka transpose reverse order mein individual transposes ka product hota hai[cite: 39].",
    },
    {
        "question": (
            "For a square matrix A, the inverse A^-1 exists if and only if"
        ),
        "options": ["det(A) = 0", "det(A) != 0", "Trace(A) = 1", "A is null"],
        "answer": "det(A) != 0",
        "reason": "Non-zero determinant wali matrix hi invertible hoti hai[cite: 43].",
    },
    {
        "question": "The minor M_32 for matrix A = [[3, 1, -4], [2, 5, 6], [1, 4, 8]] is",
        "options": ["10", "26", "26", "18"],
        "answer": "26",
        "reason": "det([[3, -4], [2, 6]]) = (3*6) - ((-4)*2) = 18 + 8 = 26[cite: 41].",
    },
    {
        "question": "If det(A) = 5 and two rows of A are interchanged, the new determinant is",
        "options": ["5", "0", "-5", "10"],
        "answer": "-5",
        "reason": "Row interchange karne se determinant ka sign change ho jata hai[cite: 42].",
    },
    {
        "question": (
            "If det(A) = 4 and one row of A is multiplied by 3, the new"
            " determinant is"
        ),
        "options": ["12", "7", "4", "64"],
        "answer": "12",
        "reason": "Kisi row ko scalar k se multiply karne par naya determinant k times ho jata hai (4*3 = 12)[cite: 42].",
    },
    {
        "question": "A square matrix A is Hermitian if it satisfies",
        "options": [
            "(A_bar)^T = -A",
            "(A_bar)^T = A",
            "A^T = A",
            "A^2 = I",
        ],
        "answer": "(A_bar)^T = A",
        "reason": "Hermitian matrix conjugate transpose ke equal hoti hai[cite: 37].",
    },
    {
        "question": "The trace of a square matrix is defined as the",
        "options": [
            "Product of the diagonal entries",
            "Sum of all entries",
            "Sum of the main diagonal entries",
            "Determinant value",
        ],
        "answer": "Sum of the main diagonal entries",
        "reason": "Trace main diagonal entries ka sum hota hai[cite: 36].",
    },
    {
        "question": "In artificial intelligence features representation, a dataset matrix stores each column as a",
        "options": ["Determinant", "Transpose", "Scalar", "Feature"],
        "answer": "Feature",
        "reason": "Dataset matrices mein columns features ko represent karte hain[cite: 39].",
    },
    {
        "question": (
            "A grayscale photo matrix stores numbers corresponding to which"
            " property?"
        ),
        "options": [
            "Name of picture",
            "File size",
            "Width of screen",
            "Brightness of one pixel",
        ],
        "answer": "Brightness of one pixel",
        "reason": "Grayscale image ka har entry ek pixel ki brightness represent karta hai[cite: 39].",
    },
    {
        "question": (
            "Neural networks store what they have learned inside matrices"
            " called"
        ),
        "options": ["Weights", "Minors", "Cofactors", "Diagonals"],
        "answer": "Weights",
        "reason": "Neural networks learning weights matrices mein store karte hain[cite: 39].",
    },
    {
        "question": "Every system of linear equations has how many possible solutions?",
        "options": [
            "Zero, one, or infinitely many solutions",
            "Exactly two solutions",
            "Exactly one solution always",
            "At most three solutions",
        ],
        "answer": "Zero, one, or infinitely many solutions",
        "reason": "Linear systems ke paas ya toh no solution, unique solution, ya infinite solutions hotay hain[cite: 45].",
    },
]

# Time duration for the quiz (30 minutes in seconds)
TOTAL_TIME_SECONDS = 30 * 60

# Session state initialization
if "submitted" not in st.session_state:
  st.session_state.submitted = False
if "current_index" not in st.session_state:
  st.session_state.current_index = 0
if "user_answers" not in st.session_state:
  st.session_state.user_answers = {}
if "start_time" not in st.session_state:
  import time

  st.session_state.start_time = time.time()
if "shuffled_mcqs" not in st.session_state:
  shuffled = list(MCQS_DATA)
  random.shuffle(shuffled)
  for q in shuffled:
    random.shuffle(q["options"])
  st.session_state.shuffled_mcqs = shuffled

# Title Header styled like Linear Algebra Pre-Board
st.title("📐 Linear Algebra Pre-Board LMS Portal")
st.markdown("NTS / ECAT style test portal with timer, review, and AI Tutor.")

# Timer logic calculation
import time

elapsed_time = int(time.time() - st.session_state.start_time)
remaining_time = TOTAL_TIME_SECONDS - elapsed_time

if remaining_time <= 0 and not st.session_state.submitted:
  st.session_state.submitted = True
  st.rerun()

# Main Quiz Interface
if not st.session_state.submitted:
  # Display Countdown Timer in a metric box
  mins, secs = divmod(max(0, remaining_time), 60)
  st.metric(
      label="⏳ Time Remaining", value=f"{mins:02d}:{secs:02d}", delta=None
  )

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

  # Navigation Buttons
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
    if st.button("✅ Submit Test", type="primary"):
      st.session_state.submitted = True
      st.rerun()

  st.markdown("---")
  st.markdown("### Question Palette (NTS Style)")

  # Render NTS style question palette circles
  palette_html = '<div class="palette-container">'
  for i in range(total):
    is_answered = i in st.session_state.user_answers and st.session_state.user_answers[i] is not None
    circle_class = "circle-answered" if is_answered else "circle-unanswered"
    if i == idx:
      circle_class += " circle-current"
    palette_html += f'<div class="palette-circle {circle_class}">{i+1}</div>'
  palette_html += "</div>"
  st.markdown(palette_html, unsafe_allow_html=True)

  # Auto refresh component to keep the countdown ticking smoothly
  time.sleep(1)
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
    st.session_state.start_time = time.time()
    random.shuffle(st.session_state.shuffled_mcqs)
    for q in st.session_state.shuffled_mcqs:
      random.shuffle(q["options"])
    st.rerun()
