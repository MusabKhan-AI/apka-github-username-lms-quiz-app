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
MCQS_DATA = [
    {
        "question": "What is raw facts and figures called?",
        "options": ["Information", "Data", "Structure", "Algorithm"],
        "answer": "Data",
        "reason": (
            "Raw facts and figures ko data kehte hain; process hone par ye"
            " information ban sakte hain."
        ),
    },
    {
        "question": "A Data Structure is defined as:",
        "options": [
            "A programming language syntax",
            (
                "Specialized format for organizing and storing data in memory"
                " considering relationships"
            ),
            "A hardware component of memory",
            "An operating system file format",
        ],
        "answer": (
            "Specialized format for organizing and storing data in memory"
            " considering relationships"
        ),
        "reason": (
            "Data structure data ko organize aur store karne ka tareeqa hota"
            " hai."
        ),
    },
    {
        "question": "According to the formula, Program is equal to:",
        "options": [
            "Data + Syntax",
            "Memory + Logic",
            "Algorithm + Data Structure",
            "Function + Variable",
        ],
        "answer": "Algorithm + Data Structure",
        "reason": (
            "Program logic/algorithm aur data ko manage karne wali structure"
            " dono se mil kar banta hai."
        ),
    },
    {
        "question": (
            "A step-by-step procedure to solve a particular problem is known"
            " as:"
        ),
        "options": ["Algorithm", "Data Structure", "Pointer", "Array"],
        "answer": "Algorithm",
        "reason": (
            "Algorithm kisi problem ko solve karne ke step-by-step instructions"
            " hotay hain."
        ),
    },
    {
        "question": "Which of the following is a Primitive Data Structure?",
        "options": ["Stack", "Queue", "Integer", "Linked List"],
        "answer": "Integer",
        "reason": (
            "Integer primitive type hai; stack, queue aur linked list"
            " non-primitive structures hain."
        ),
    },
    {
        "question": (
            "Data structures that are directly operated upon by machine-level"
            " instructions are called:"
        ),
        "options": [
            "Non-Primitive Data Structures",
            "Primitive Data Structures",
            "Abstract Data Types",
            "Dynamic Data Structures",
        ],
        "answer": "Primitive Data Structures",
        "reason": (
            "Primitive types ko machine-level operations seedha handle kar"
            " sakte hain."
        ),
    },
    {
        "question": (
            "Which of the following operations is categorized under Primitive"
            " Data Structures?"
        ),
        "options": ["Traversal", "Sorting", "Create", "Merging"],
        "answer": "Create",
        "reason": (
            "Create basic operation hai; traversal, sorting aur merging aam"
            " tor par non-primitive structures par hotay hain."
        ),
    },
    {
        "question": "Non-primitive data structures are derived from:",
        "options": [
            "Hardware instructions",
            "Primitive data structures",
            "Algorithms",
            "Operating systems",
        ],
        "answer": "Primitive data structures",
        "reason": (
            "Non-primitive structures primitive types ko use karke banaye"
            " jate hain."
        ),
    },
    {
        "question": "Linear data structures exhibit elements in a:",
        "options": [
            "Hierarchical relationship",
            "Sequence or linear series",
            "Random order",
            "Parent-child structure",
        ],
        "answer": "Sequence or linear series",
        "reason": (
            "Linear structure mein elements ek sequence mein arrange hotay hain."
        ),
    },
    {
        "question": "Which of the following is a Non-Linear Data Structure?",
        "options": ["Array", "Stack", "Queue", "Tree"],
        "answer": "Tree",
        "reason": "Tree hierarchical, non-linear structure hai.",
    },
    {
        "question": (
            "Linear data structures are easy to implement because computer"
            " memory is organized:"
        ),
        "options": [
            "Hierarchically",
            "In a linear fashion",
            "As a graph",
            "Randomly",
        ],
        "answer": "In a linear fashion",
        "reason": (
            "Linear memory/sequence ki wajah se linear structures ko samajhna"
            " aur implement karna asaan hota hai."
        ),
    },
    {
        "question": (
            "Non-Linear data structures often exhibit which type of"
            " relationship?"
        ),
        "options": [
            "Sequential relationship",
            "Parent-child or hierarchical relationship",
            "Index-based relationship",
            "Direct contiguous memory relationship",
        ],
        "answer": "Parent-child or hierarchical relationship",
        "reason": (
            "Non-linear structures mein hierarchical ya network-style"
            " relationships ho sakte hain."
        ),
    },
    {
        "question": (
            "The process of visiting every element in a data structure exactly"
            " once is called:"
        ),
        "options": ["Sorting", "Searching", "Traversal", "Insertion"],
        "answer": "Traversal",
        "reason": "Traversal ka matlab har element ko visit karna hai.",
    },
    {
        "question": (
            "Combining elements of two different sorted data structures into a"
            " single structure is called:"
        ),
        "options": ["Insertion", "Merging", "Deletion", "Updating"],
        "answer": "Merging",
        "reason": (
            "Merging do structures ke elements ko ek structure mein combine"
            " karta hai."
        ),
    },
    {
        "question": "Which of the following is NOT a primitive data structure?",
        "options": ["Character", "Pointer", "Float", "Array"],
        "answer": "Array",
        "reason": (
            "Array composite/non-primitive structure hai; character, pointer"
            " aur float basic types hain."
        ),
    },
    {
        "question": "An Array is a collection of elements that are:",
        "options": [
            "Homogeneous and stored in contiguous memory",
            "Heterogeneous and stored in dynamic memory",
            "Non-sequential and hierarchical",
            "Stored using pointers only",
        ],
        "answer": "Homogeneous and stored in contiguous memory",
        "reason": (
            "Array aam tor par same type ke elements contiguous memory mein"
            " rakhta hai."
        ),
    },
    {
        "question": (
            "In a 1D Array with size N, the index of the last element (assuming"
            " 0-based indexing) is:"
        ),
        "options": ["N", "N-1", "1", "N+1"],
        "answer": "N-1",
        "reason": (
            "Zero-based indexing mein N elements ke indexes 0 se N-1 tak hotay"
            " hain."
        ),
    },
    {
        "question": (
            "What is the time complexity to access an element in a 1D Array by"
            " its index?"
        ),
        "options": ["O(1)", "O(N)", "O(log N)", "O(N^2)"],
        "answer": "O(1)",
        "reason": "Array index se element ka address seedha calculate hota hai.",
    },
    {
        "question": (
            "What happens if you try to access an array index beyond its"
            " allocated size?"
        ),
        "options": [
            "Compilation error",
            "Array Index Out of Bounds Exception / Garbage value",
            "Automatic size expansion",
            "Program completes successfully",
        ],
        "answer": "Array Index Out of Bounds Exception / Garbage value",
        "reason": (
            "Bounds se bahar access language ke mutabiq exception ya"
            " undefined/garbage behavior de sakta hai."
        ),
    },
    {
        "question": (
            "Which formula calculates the address of A[i] in a 1D array with"
            " Base Address B and element size W?"
        ),
        "options": [
            "Address = B+i*W",
            "Address = B+i/W",
            "Address = Bi+W",
            "Address = B-i*W",
        ],
        "answer": "Address = B+i*W",
        "reason": (
            "Zero-based array mein i-th element ka address base plus i times"
            " element width hota hai."
        ),
    },
    {
        "question": "What is the main disadvantage of a standard static array?",
        "options": [
            "Slow access time",
            "Fixed size allocated at compile time",
            "Cannot store primitive types",
            "High memory pointer overhead",
        ],
        "answer": "Fixed size allocated at compile time",
        "reason": (
            "Static array ka size aam tor par fixed hota hai aur resize karna"
            " mushkil hota hai."
        ),
    },
    {
        "question": (
            "What is the worst-case time complexity for inserting an element"
            " at the beginning of a 1D Array?"
        ),
        "options": ["O(1)", "O(N)", "O(log N)", "O(N^2)"],
        "answer": "O(N)",
        "reason": (
            "Beginning par insert karne ke liye existing elements shift karne"
            " parte hain."
        ),
    },
    {
        "question": (
            "Insertion at the end of a 1D Array (if space is available) takes:"
        ),
        "options": ["O(1)", "O(N)", "O(log N)", "O(N^2)"],
        "answer": "O(1)",
        "reason": (
            "Space available ho to end par element rakhne ke liye shifting nahi"
            " chahiye."
        ),
    },
    {
        "question": (
            "Given int A[5] = {10, 20, 30, 40, 50}, what is the value of A[2]?"
        ),
        "options": ["10", "20", "30", "40"],
        "answer": "30",
        "reason": (
            "Zero-based indexing mein A[2] teesra element hai, yani 30."
        ),
    },
    {
        "question": (
            "The base address of an array refers to the memory address of:"
        ),
        "options": [
            "The first element",
            "The last element",
            "The middle element",
            "The pointer variable itself",
        ],
        "answer": "The first element",
        "reason": "Array ka base address uske first element ka address hota hai.",
    },
    {
        "question": "A Linked List node primarily consists of:",
        "options": [
            "Index and Data",
            "Data field and Pointer to Next node",
            "Key and Value",
            "Header and Footer",
        ],
        "answer": "Data field and Pointer to Next node",
        "reason": "Singly linked list node data aur next node ka pointer rakhta hai.",
    },
    {
        "question": "Unlike Arrays, elements in a Linked List are stored in:",
        "options": [
            "Contiguous memory locations",
            "Non-contiguous (random) memory locations",
            "Sequential disk sectors",
            "Read-only memory",
        ],
        "answer": "Non-contiguous (random) memory locations",
        "reason": (
            "Linked-list nodes memory mein alag alag jagah par ho sakte hain."
        ),
    },
    {
        "question": (
            "The pointer of the last node in a Singly Linked List points to:"
        ),
        "options": ["Base Address", "Head node", "NULL", "Garbage value"],
        "answer": "NULL",
        "reason": "Singly linked list ke last node ka next pointer NULL hota hai.",
    },
    {
        "question": (
            "What is the time complexity to search an element in a Singly"
            " Linked List of size N?"
        ),
        "options": ["O(1)", "O(N)", "O(log N)", "O(N log N)"],
        "answer": "O(N)",
        "reason": "Search ke liye worst case mein tamam nodes check karne parte hain.",
    },
    {
        "question": (
            "Inserting a new node at the head (beginning) of a Singly Linked"
            " List takes:"
        ),
        "options": ["O(1)", "O(N)", "O(log N)", "O(N^2)"],
        "answer": "O(1)",
        "reason": (
            "Head par insert karne mein new node ka next set aur head update"
            " hota hai."
        ),
    },
    {
        "question": (
            "In a Doubly Linked List, each node contains how many pointers?"
        ),
        "options": ["1", "2 (Previous & Next)", "3", "0"],
        "answer": "2 (Previous & Next)",
        "reason": (
            "Doubly linked list mein previous aur next ke do pointers hotay hain."
        ),
    },
    {
        "question": (
            "In a Circular Linked List, the last node's next pointer points"
            " to:"
        ),
        "options": ["NULL", "Head Node", "Previous Node", "Root Node"],
        "answer": "Head Node",
        "reason": "Circular list ka last node dobara head ko point karta hai.",
    },
    {
        "question": "What is a major advantage of Linked Lists over Arrays?",
        "options": [
            "Random access of elements",
            "Dynamic memory size reallocation",
            "Less memory consumption per element",
            "Cache friendliness",
        ],
        "answer": "Dynamic memory size reallocation",
        "reason": (
            "Linked list nodes zaroorat ke mutabiq allocate ho sakte hain,"
            " fixed contiguous block zaroori nahi."
        ),
    },
    {
        "question": (
            "A dummy node placed at the start of a linked list is called:"
        ),
        "options": [
            "Header Node",
            "Anchor Node",
            "Base Node",
            "Root Node",
        ],
        "answer": "Header Node",
        "reason": "Dummy starting node ko aksar header node kaha jata hai.",
    },
    {
        "question": (
            "The operation of moving through a linked list from start to end"
            " is called:"
        ),
        "options": ["Allocation", "Traversal", "Paging", "Hashing"],
        "answer": "Traversal",
        "reason": "Start se aage nodes visit karna traversal hai.",
    },
    {
        "question": (
            "Which data structure is used when dynamic allocation is needed"
            " without contiguous layout?"
        ),
        "options": ["Array", "Linked List", "Matrix", "Heap Array"],
        "answer": "Linked List",
        "reason": (
            "Linked list dynamic allocation aur non-contiguous storage support"
            " karti hai."
        ),
    },
    {
        "question": "Memory for nodes in a Linked List is allocated during:",
        "options": [
            "Compile time",
            "Run time (Dynamically)",
            "System boot",
            "Link time",
        ],
        "answer": "Run time (Dynamically)",
        "reason": "Nodes aam tor par program chalne ke waqt allocate hotay hain.",
    },
    {
        "question": (
            "Which of the following takes O(N) time in a Singly Linked List?"
        ),
        "options": [
            "Insertion at head",
            "Deletion at head",
            "Accessing the k-th element",
            "Updating head pointer",
        ],
        "answer": "Accessing the k-th element",
        "reason": (
            "Singly linked list mein k-th node tak pohanchne ke liye nodes"
            " follow karne parte hain."
        ),
    },
    {
        "question": (
            "In C++, which operator is used to allocate dynamic memory for a"
            " Linked List node?"
        ),
        "options": ["malloc()", "new", "alloc", "create"],
        "answer": "new",
        "reason": (
            "C++ mein dynamic object/node allocate karne ke liye new operator"
            " use hota hai."
        ),
    },
    {
        "question": (
            "What happens if a node is deleted in dynamic memory but its"
            " memory is not freed?"
        ),
        "options": [
            "Stack Overflow",
            "Memory Leak",
            "Segmentation Fault",
            "Buffer Underflow",
        ],
        "answer": "Memory Leak",
        "reason": "Allocated memory release na ho to memory leak hota hai.",
    },
    {
        "question": "Stack follows which ordering principle?",
        "options": [
            "FIFO (First In First Out)",
            "LIFO (Last In First Out)",
            "LILO (Last In Last Out)",
            "Priority Order",
        ],
        "answer": "LIFO (Last In First Out)",
        "reason": "Stack mein sab se aakhri push hua item pehle pop hota hai.",
    },
    {
        "question": "The operation to add an item onto a stack is called:",
        "options": ["Push", "Pop", "Enqueue", "Dequeue"],
        "answer": "Push",
        "reason": "Stack mein item add karne ko push kehte hain.",
    },
    {
        "question": (
            "The operation to remove an item from the top of a stack is"
            " called:"
        ),
        "options": ["Push", "Pop", "Peek", "Front"],
        "answer": "Pop",
        "reason": "Top item remove karne ka operation pop hai.",
    },
    {
        "question": "Trying to pop an element from an empty stack results in:",
        "options": [
            "Stack Overflow",
            "Stack Underflow",
            "Null Pointer Exception",
            "Memory Leak",
        ],
        "answer": "Stack Underflow",
        "reason": "Empty stack se pop karna underflow hai.",
    },
    {
        "question": "Pushing an element into a full static stack causes:",
        "options": [
            "Stack Overflow",
            "Stack Underflow",
            "Dynamic Expansion",
            "Segmentation Fault",
        ],
        "answer": "Stack Overflow",
        "reason": "Full fixed-capacity stack mein push karne se overflow hota hai.",
    },
    {
        "question": (
            "The variable that points to the topmost element of a stack is"
            " commonly named:"
        ),
        "options": ["Front", "Rear", "Top", "Head"],
        "answer": "Top",
        "reason": "Top variable stack ke top element/index ko track karta hai.",
    },
    {
        "question": (
            "What is the time complexity of Push and Pop operations in a"
            " Stack?"
        ),
        "options": ["O(1)", "O(N)", "O(log N)", "O(N^2)"],
        "answer": "O(1)",
        "reason": (
            "Stack push aur pop dono constant-time operations hain, standard"
            " implementation mein."
        ),
    },
    {
        "question": (
            "Which operation returns the top element of a stack without"
            " removing it?"
        ),
        "options": ["Pop", "Peek/Top", "Push", "Seek"],
        "answer": "Peek/Top",
        "reason": "Peek top item ko return karta hai baghair remove kiye.",
    },
    {
        "question": "Which application uses a Stack data structure?",
        "options": [
            "Function Call Stack / Recursion",
            "Undo mechanism in text editors",
            "Expression Evaluation & Parsing",
            "All of the above",
        ],
        "answer": "All of the above",
        "reason": (
            "Call stack, undo systems aur expression evaluation stack ke"
            " common uses hain."
        ),
    },
    {
        "question": "Expression A+B is in infix form. What is its Prefix form?",
        "options": ["+AB", "AB+", "+BA", "A + B"],
        "answer": "+AB",
        "reason": "Prefix mein operator operands se pehle aata hai.",
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

st.title("📚 Data Structures LMS Quiz Portal")
st.markdown("NTS / ECAT style test portal with instant review and reasons.")

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
    default_ix = current_q["options"].index(prev_ans) if prev_ans in current_q["options"] else 0
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
