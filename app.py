import random
import time
from groq import Groq
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Linear Algebra Pre-Board LMS Quiz Portal",
    page_icon="📚",
    layout="centered",
)

# Initialize Groq client using Streamlit Secrets safely
try:
  groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
  groq_client = None

# 30 Mixed MCQs selected from the Linear Algebra PDF (Part 1 to Part 6)
MCQS_DATA = [
    {
        "question": "A matrix with 3 rows and 2 columns has size",
        "options": ["2 x 3", "3 x 3", "3 x 2", "6 x 1"],
        "answer": "3 x 2",
        "reason": (
            "Matrix ka size rows x columns hota hai, is liye 3 rows aur 2"
            " columns ke liye size 3 x 2 hai[cite: 33]."
        ),
    },
    {
        "question": (
            "A square matrix that is both upper and lower triangular must be"
        ),
        "options": [
            "A matrix with no zeros",
            "A diagonal matrix",
            "A 1 x n matrix",
            "A non-square matrix",
        ],
        "answer": "A diagonal matrix",
        "reason": (
            "Jab matrix upper aur lower triangular dono ho toh main diagonal ke"
            " ilawa baqi sab entries zero hoti hain, jo ke diagonal matrix ki"
            " definition hai[cite: 36]."
        ),
    },
    {
        "question": "The transpose of a matrix is obtained by",
        "options": [
            "Interchanging its rows and columns",
            "Adding 1 to every entry",
            "Multiplying every entry by -1",
            "Deleting its diagonal",
        ],
        "answer": "Interchanging its rows and columns",
        "reason": (
            "Transpose nikalne ke liye matrix ki rows aur columns ko aapas mein"
            " interchange kiya jata hai[cite: 36]."
        ),
    },
    {
        "question": "A matrix A is symmetric if",
        "options": ["A^T = -A", "A^2 = I", "A^2 = A", "A^T = A"],
        "answer": "A^T = A",
        "reason": (
            "Symmetric matrix woh hoti hai jiska transpose uske apne barabar"
            " ho (A^T = A)[cite: 36]."
        ),
    },
    {
        "question": "The trace of a square matrix is the",
        "options": [
            "Product of the diagonal entries",
            "Sum of all the entries",
            "Difference of the two rows",
            "Sum of the main diagonal entries",
        ],
        "answer": "Sum of the main diagonal entries",
        "reason": (
            "Trace main diagonal ki tamam entries ke sum ke barabar hota hai"
            "[cite: 36]."
        ),
    },
    {
        "question": "A square matrix A is involutory if",
        "options": ["A^2 = A", "A^2 = O", "A^2 = I", "A^T = -A"],
        "answer": "A^2 = I",
        "reason": (
            "Involutory matrix woh hoti hai jiska square identity matrix (I)"
            " ke barabar ho[cite: 37]."
        ),
    },
    {
        "question": "The product AB is defined only when",
        "options": [
            "Rows of A = rows of B",
            "Columns of A = columns of B",
            "Columns of A = rows of B",
            "A and B are both square",
        ],
        "answer": "Columns of A = rows of B",
        "reason": (
            "Matrix multiplication ke liye pehli matrix ke columns doosri matrix"
            " ki rows ke equal honay chahiye[cite: 38]."
        ),
    },
    {
        "question": (
            "In AI, a dataset is usually stored as a matrix in which each"
            " column represents a"
        ),
        "options": ["Determinant", "Transpose", "Scalar", "Feature"],
        "answer": "Feature",
        "reason": (
            "AI datasets mein columns features ko aur rows data points ko"
            " represent karte hain[cite: 39]."
        ),
    },
    {
        "question": (
            "A grayscale photo can be represented as a matrix in which each"
            " number is the"
        ),
        "options": [
            "Name of the picture",
            "Size of the file",
            "Width of the screen",
            "Brightness of one pixel",
        ],
        "answer": "Brightness of one pixel",
        "reason": (
            "Grayscale image matrix mein har number ek pixel ki brightness ya"
            " intensity ko zahir karta hai[cite: 39]."
        ),
    },
    {
        "question": "The transpose of a product (AB)^T equals",
        "options": ["A^T B^T", "B^T A^T", "AB", "BA"],
        "answer": "B^T A^T",
        "reason": (
            "Product ka transpose reverse order mein hota hai, yani (AB)^T ="
            " B^T A^T[cite: 39]."
        ),
    },
    {
        "question": "The determinant of a square matrix is",
        "options": [
            "Another matrix",
            "A row vector",
            "A single number",
            "A column vector",
        ],
        "answer": "A single number",
        "reason": (
            "Square matrix ka determinant hamesha ek single scalar value (number)"
            " hota hai[cite: 39]."
        ),
    },
    {
        "question": "If det(A) = 0, then the matrix A is",
        "options": [
            "Invertible",
            "The identity matrix",
            "Always symmetric",
            "Singular (no inverse)",
        ],
        "answer": "Singular (no inverse)",
        "reason": (
            "Agar determinant zero ho toh matrix ko singular kehte hain aur uska"
            " inverse exist nahi karta[cite: 40]."
        ),
    },
    {
        "question": "The cofactor of entry a_ij is given by",
        "options": [
            "C_ij = (-1)^(i+j) M_ij",
            "C_ij = M_ij + 1",
            "C_ij = (-1)^(ij) M_ij",
            "C_ij = i * j * M_ij",
        ],
        "answer": "C_ij = (-1)^(i+j) M_ij",
        "reason": (
            "Cofactor ka formula (-1^(i+j)) multiplied by minor (M_ij) hota hai"
            "[cite: 41]."
        ),
    },
    {
        "question": (
            "If every entry of a row of a square matrix is zero, then its"
            " determinant is"
        ),
        "options": ["0", "1", "-1", "Undefined"],
        "answer": "0",
        "reason": (
            "Agar kisi matrix ki koi poori row zero ho toh uska determinant zero"
            " hota hai[cite: 42]."
        ),
    },
    {
        "question": (
            "If any two rows of a square matrix are interchanged, the"
            " determinant"
        ),
        "options": [
            "Changes its sign",
            "Stays the same",
            "Becomes zero",
            "Doubles",
        ],
        "answer": "Changes its sign",
        "reason": (
            "Do rows aapas mein interchange karne se determinant ka sign change"
            " ho jata hai[cite: 42]."
        ),
    },
    {
        "question": "If two rows of a square matrix are identical, its determinant is",
        "options": ["1", "Equal to the trace", "0", "-1"],
        "answer": "0",
        "reason": (
            "Identical rows honay par determinant hamesha zero hota hai [cite:"
            " 42]."
        ),
    },
    {
        "question": "An inverse of a 2x2 matrix exists only if",
        "options": ["det = 0", "det = 1 only", "det != 0", "The matrix is symmetric"],
        "answer": "det != 0",
        "reason": (
            "Inverse tabhi mumkin hai jab determinant non-zero ho[cite: 43]."
        ),
    },
    {
        "question": "The matrix [[3, 6], [1, 2]] has no inverse because",
        "options": [
            "Its determinant is 1",
            "Its determinant is 0",
            "It is not square",
            "It has a negative entry",
        ],
        "answer": "Its determinant is 0",
        "reason": (
            "Is matrix ka determinant (3*2 - 6*1 = 0) hai, is liye inverse"
            " exist nahi karta[cite: 43]."
        ),
    },
    {
        "question": "A simple fix for duplicate (repeated) features is to",
        "options": [
            "Remove one of the repeated features",
            "Multiply the data by zero",
            "Add more duplicates",
            "Take the transpose",
        ],
        "answer": "Remove one of the repeated features",
        "reason": (
            "Multicollinearity se bachne ke liye duplicate feature ko remove kar"
            " diya jata hai[cite: 44]."
        ),
    },
    {
        "question": (
            "The matrix [[-1, 0], [0, 1]] has det -1, which means the image is"
        ),
        "options": [
            "Stretched 6 times",
            "Squashed into a line",
            "Destroyed",
            "Flipped (mirror image) with the same area",
        ],
        "answer": "Flipped (mirror image) with the same area",
        "reason": (
            "Negative determinant reflection (mirror image) ko zahir karta hai"
            "[cite: 44]."
        ),
    },
    {
        "question": (
            "A matrix like [[1, 2], [2, 4]] has det 0, so the image is"
        ),
        "options": [
            "Doubled in area",
            "Rotated only",
            "Flipped only",
            "Squashed flat into a line",
        ],
        "answer": "Squashed flat into a line",
        "reason": (
            "Determinant zero honay ka matlab hai ke 2D space flat ho kar line"
            " ban gayi hai[cite: 44]."
        ),
    },
    {
        "question": (
            "A system of linear equations written as AX = 0 is called a"
        ),
        "options": [
            "Non-homogeneous system",
            "Homogeneous system",
            "Quadratic system",
            "Singular matrix",
        ],
        "answer": "Homogeneous system",
        "reason": (
            "Jab right side zero vector ho toh usay homogeneous system kehte"
            " hain[cite: 44]."
        ),
    },
    {
        "question": "Every homogeneous system of linear equations always has",
        "options": [
            "No solution",
            "Exactly two solutions",
            "At least the trivial solution",
            "Only nontrivial solutions",
        ],
        "answer": "At least the trivial solution",
        "reason": (
            "Homogeneous system ka zero solution (trivial solution) hamesha exist"
            " karta hai[cite: 44]."
        ),
    },
    {
        "question": "The solution x_1 = x_2 = ... = x_n = 0 is called the",
        "options": [
            "Nontrivial solution",
            "Unique minor",
            "Trivial solution",
            "Augmented solution",
        ],
        "answer": "Trivial solution",
        "reason": "Tamam variables ki zero value ko trivial solution kehte hain[cite: 45].",
    },
    {
        "question": "Every system of linear equations has",
        "options": [
            "Zero, one, or infinitely many solutions",
            "Exactly two solutions",
            "Exactly one solution always",
            "At most three solutions",
        ],
        "answer": "Zero, one, or infinitely many solutions",
        "reason": (
            "Linear systems ke ya toh no solution, unique solution, ya infinite"
            " solutions hotay hain[cite: 45]."
        ),
    },
    {
        "question": (
            "If two lines in a plane are parallel (and distinct), the system has"
        ),
        "options": [
            "One solution",
            "Two solutions",
            "Infinitely many solutions",
            "No solution",
        ],
        "answer": "No solution",
        "reason": (
            "Parallel lines aapas mein kahin intersect nahi karti, is liye koi"
            " solution nahi hota[cite: 45]."
        ),
    },
    {
        "question": "The determinant of [[1, 2], [3, 4]] is",
        "options": ["2", "10", "-10", "-2"],
        "answer": "-2",
        "reason": "(1*4) - (2*3) = 4 - 6 = -2[cite: 40].",
    },
    {
        "question": "The determinant of the identity matrix I_2 is",
        "options": ["0", "1", "2", "-1"],
        "answer": "1",
        "reason": "Identity matrix ka determinant hamesha 1 hota hai[cite: 40].",
    },
    {
        "question": "If A is a 2x4 matrix, then A^T has order",
        "options": ["2 x 4", "4 x 4", "2 x 2", "4 x 2"],
        "answer": "4 x 2",
        "reason": (
            "Transpose lene se rows aur columns ki tadad ulat jati hai, is liye"
            " 4 x 2 ban jayega[cite: 36]."
        ),
    },
    {
        "question": "Every identity matrix is also a",
        "options": [
            "Null matrix",
            "Scalar matrix",
            "Skew-symmetric matrix",
            "Row matrix",
        ],
        "answer": "Scalar matrix",
        "reason": (
            "Identity matrix ek aisi scalar matrix hoti hai jismein diagonal"
            " elements 1 hotay hain[cite: 35]."
        ),
    },
]

# --- LOGIN SYSTEM ---
if "logged_in" not in st.session_state:
  st.session_state.logged_in = False

if not st.session_state.logged_in:
  st.markdown(
      "<h2 style='text-align: center;'>🔐 Linear Algebra Pre-Board Login</h2>",
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

# Timer initialization (30 minutes = 1800 seconds)
if "start_time" not in st.session_state:
  st.session_state.start_time = time.time()

# Header Styling & Professional Title
st.markdown(
    "<h1 style='text-align: center; color: #1E3A8A;'>📐 Linear Algebra Pre-Board"
    " LMS Portal</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #4B5563;'>Professional NTS / ECAT"
    " Style Assessment</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# Main Quiz Interface
if not st.session_state.submitted:
  elapsed_time = int(time.time() - st.session_state.start_time)
  remaining_time = 1800 - elapsed_time

  if remaining_time <= 0:
    st.session_state.submitted = True
    st.rerun()

  mins, secs = divmod(remaining_time, 60)

  # Timer and Submit option row
  col_timer, col_sub = st.columns([2, 1])
  with col_timer:
    st.markdown(
        f"⏳ **Waqt Baki (Time Remaining):** <span"
        f" style='color:red; font-size:20px; font-weight:bold;'>{mins:02d}:{secs:02d}</span>",
        unsafe_allow_html=True,
    )
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

  # --- NTS STYLE QUESTION NAVIGATION PALETTE (CIRCLES) ---
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

  time.sleep(
