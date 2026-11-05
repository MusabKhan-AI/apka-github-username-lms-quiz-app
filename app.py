from groq import Groq
import streamlit as st
import random

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

# 200 MCQs based on provided AI and Machine Learning Lectures
MCQS_DATA = [
    # Lecture 1: Introduction to AI & ML
    {
        "question": "Who coined the term 'Machine Learning' in 1959?",
        "options": ["John McCarthy", "Arthur Samuel", "Alan Turing", "Tom Mitchell"],
        "answer": "Arthur Samuel",
        "reason": "Arthur Samuel, an IBM employee and pioneer in computer gaming, coined the term machine learning in 1959[cite: 10]."
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
        "reason": "Artificial Intelligence is the broad family, Machine Learning is its subset, and Deep Learning is a subset of Machine Learning[cite: 10]."
    },
    {
        "question": "Who is credited with originally using the term 'Artificial Intelligence' in 1956?",
        "options": ["Arthur Samuel", "John McCarthy", "Alan Turing", "Syed Adnan Shah Bukhari"],
        "answer": "John McCarthy",
        "reason": "John McCarthy used the terminology 'Artificial Intelligence' in 1956 and hosted the first AI conference[cite: 31]."
    },
    {
        "question": "According to Tom Mitchell's definition of learning, a computer program learns from experience E regarding task T if its performance P:",
        "options": ["Decreases", "Stays constant", "Improves with experience E", "Becomes zero"],
        "answer": "Improves with experience E",
        "reason": "Performance at task T, measured by P, improves with experience E[cite: 12]."
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
        "reason": "ML algorithms require large amounts of structured data to learn and improve performance[cite: 31]."
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
        "reason": "Siri and chatbot customer service are key uses of AI, while ML common uses include friend suggestions and stock forecasts[cite: 31]."
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

    # Machine Learning Life Cycle (LEC_2)
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
        "reason": "Life cycle starts by collecting data because to train a model we need data[cite: 2, 3]."
    },
    {
        "question": "In a dataset matrix used in AI, what does each column typically represent?",
        "options": ["Data point", "Label", "Feature", "Row index"],
        "answer": "Feature",
        "reason": "In AI datasets, columns represent features and rows represent data points[cite: 39]."
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

    # Types of Machine Learning (Supervised, Unsupervised, Reinforcement, Semi-Supervised)
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
        "reason": "Ordinal data denotes a nominal variable with categories falling in an ordered list, like clothing sizes (small, medium, large)[cite: 27]."
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
    {
        "question": "In the context of logistic regression code example from the slides, what library was used?",
        "options": ["sklearn", "tensorflow", "keras", "pytorch"],
        "answer": "sklearn",
        "reason": "The code example used `from sklearn.linear_model import LogisticRegression`[cite: 30]."
    },

    # AI Agents & PEAS (Lecture 3 & 4)
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
        "question": "What does an agent function map from?",
        "options": [
            "Percept histories to actions [f: P* -> A]",
            "Actuators to sensors",
            "Database tables to UI elements",
            "Random numbers to weights"
        ],
        "answer": "Percept histories to actions [f: P* -> A]",
        "answer_full": "f: P* -> A",
        "reason": "Agent function maps from percept histories to actions[cite: 32]."
    },
    {
        "question": "What is the difference between an agent architecture and an agent program?",
        "options": [
            "Architecture is the computing device/hardware, while program implements the agent function",
            "Program is hardware and architecture is software",
            "They are identical terms",
            "Architecture runs on human brain only"
        ],
        "answer": "Architecture is the computing device/hardware, while program implements the agent function",
        "reason": "Agent = architecture + program, where architecture is the computing device with sensors/actuators and program implements the agent function[cite: 32, 98]."
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
        "question": "What are the actuators of a human agent?",
        "options": [
            "Eyes and ears",
            "Hands, legs, mouth, and other body parts",
            "Sensors and infrared range finders",
            "CPUs and RAM"
        ],
        "answer": "Hands, legs, mouth, and other body parts",
        "reason": "Human agent sensors are eyes/ears, and actuators are hands, legs, mouth, and other body parts[cite: 32]."
    },
    {
        "question": "What does a rational agent select?",
        "options": [
            "Actions that minimize its performance score",
            "Actions that maximize its (expected) utility",
            "Random actions always",
            "Actions with highest cost"
        ],
        "answer": "Actions that maximize its (expected) utility",
        "reason": "A rational agent selects actions that maximize its expected utility based on percepts and built-in knowledge[cite: 32]."
    },
    {
        "question": "Is rationality the same as omniscience (all-knowing with infinite knowledge)?",
        "options": [
            "Yes, they are identical",
            "No, omniscience knows actual outcomes of actions, but omniscience is impossible in reality",
            "Omniscience applies only to software robots",
            "Rationality requires infinite knowledge"
        ],
        "answer": "No, omniscience knows actual outcomes of actions, but omniscience is impossible in reality",
        "reason": "Rationality is distinct from omniscience; an omniscient agent knows actual outcomes, but omniscience is impossible[cite: 32]."
    },
    {
        "question": "What makes an agent autonomous?",
        "options": [
            "If its behavior is determined entirely by its designer's prior rules",
            "If its behavior is determined by its own experience with the ability to learn and adapt",
            "If it operates without sensors",
            "If it never updates its configuration"
        ],
        "answer": "If its behavior is determined by its own experience with the ability to learn and adapt",
        "reason": "An agent is autonomous if its behavior is determined by its own experience with the ability to learn and adapt[cite: 32]."
    },
    {
        "question": "What are software agents (softbots) working in artificial environments like video games or internet called?",
        "options": ["Robotic hardware agents", "Software agents", "Mechanical actuators", "Physical sensors"],
        "answer": "Software agents",
        "reason": "Agents working in artificial environments like flight simulators, video games, or internet are called software agents or softbots[cite: 32]."
    },
    {
        "question": "What is the first step in designing any agent?",
        "options": [
            "Writing Python code",
            "Specifying the task environment (PEAS) as fully as possible",
            "Purchasing high-end GPUs",
            "Testing model deployment"
        ],
        "answer": "Specifying the task environment (PEAS) as fully as possible",
        "reason": "In designing an agent, the first step must always be to specify the task environment as fully as possible using PEAS[cite: 32]."
    },

    # Environment Types / Properties (Lecture 4)
    {
        "question": "An environment where an agent's sensors give it access to the complete state of the environment at each point in time is called:",
        "options": ["Partially observable", "Fully observable", "Stochastic", "Dynamic"],
        "answer": "Fully observable",
        "reason": "Fully observable means sensors give access to the complete state of the environment at each point in time[cite: 33]."
    },
    {
        "question": "Why might an environment be partially observable?",
        "options": [
            "Because of noisy sensors or missing parts",
            "Because there is only one agent",
            "Because the time is discrete",
            "Because the state space is completely known"
        ],
        "answer": "Because of noisy sensors or missing parts",
        "reason": "An environment might be partially observable because of noisy sensors or missing parts[cite: 33]."
    },
    {
        "question": "An environment with one and only one agent operating by itself is called:",
        "options": ["Multiagent environment", "Single-agent environment", "Competitive environment", "Stochastic environment"],
        "answer": "Single-agent environment",
        "reason": "A single-agent environment has one and only one agent operating by itself (e.g., crossword puzzle, sudoku)[cite: 33]."
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
        "reason": "Deterministic means the next state of the environment is completely determined by current state and action[cite: 33]."
    },
    {
        "question": "An environment where you cannot clearly predict the next state and uncertainty is quantified using probabilities is:",
        "options": ["Deterministic", "Stochastic", "Static", "Discrete"],
        "answer": "Stochastic",
        "reason": "Stochastic environments involve uncertainty where next states cannot be clearly predicted and are quantified by probabilities[cite: 33]."
    },
    {
        "question": "In an episodic environment:",
        "options": [
            "The current decision affects all future decisions",
            "The agent's experience is divided into atomic episodes where next episode does not depend on previous actions",
            "The environment changes while the agent deliberates",
            "There are continuous time values"
        ],
        "answer": "The agent's experience is divided into atomic episodes where next episode does not depend on previous actions",
        "reason": "In episodic environments, each episode consists of percept and single action, and next episodes do not depend on previous actions[cite: 33]."
    },
    {
        "question": "Which environment type allows the environment to change while an agent is deliberating?",
        "options": ["Static environment", "Dynamic environment", "Discrete environment", "Episodic environment"],
        "answer": "Dynamic environment",
        "reason": "A dynamic environment can change while an agent is deliberating, whereas a static environment does not[cite: 33]."
    },
    {
        "question": "What is a semi-dynamic environment?",
        "options": [
            "The environment changes constantly with time",
            "The environment itself does not change with time, but the agent's performance score does",
            "There are no actions allowed",
            "It is fully observable and deterministic"
        ],
        "answer": "The environment itself does not change with time, but the agent's performance score does",
        "reason": "In a semi-dynamic environment, the environment itself does not change with the passage of time, but the agent's performance score does[cite: 33]."
    },
    {
        "question": "An environment with a limited number of distinct states, clearly defined percepts and actions is:",
        "options": ["Continuous", "Discrete", "Stochastic", "Dynamic"],
        "answer": "Discrete",
        "reason": "A discrete environment has a limited number of distinct states, clearly defined percepts and actions (e.g., chess, sudoku)[cite: 33]."
    },
    {
        "question": "According to the task environment properties table, what are the characteristics of Chess with a clock?",
        "options": [
            "Fully Observable, Multiagent, Deterministic, Sequential, Semi-dynamic, Discrete",
            "Partially Observable, Single-agent, Stochastic, Episodic, Dynamic, Continuous",
            "Fully Observable, Single-agent, Deterministic, Static, Discrete",
            "Partially Observable, Multiagent, Stochastic, Dynamic, Continuous"
        ],
        "answer": "Fully Observable, Multiagent, Deterministic, Sequential, Semi-dynamic, Discrete",
        "reason": "Chess with a clock is fully observable, multiagent, deterministic, sequential, semi-dynamic, and discrete[cite: 33]."
    },

    # Agent Programs & Reflex / Goal / Utility Agents (Lecture 5, 6, 7)
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
        "reason": "Simple reflex agents make use of condition-action rules with the syntax 'if Condition then Action'[cite: 79, 80]."
    },
    {
        "question": "What is a major limitation of simple reflex agents?",
        "options": [
            "They have unlimited intelligence",
            "Even a little bit of un-observability can cause serious trouble and infinite loops",
            "They always use deep neural networks",
            "They cannot use rules"
        ],
        "answer": "Even a little bit of un-observability can cause serious trouble and infinite loops",
        "reason": "Simple reflex agents have limited intelligence and un-observability causes serious trouble and unavoidable infinite loops[cite: 83]."
    },
    {
        "question": "How can a simple reflex agent escape infinite loops in partially observable environments?",
        "options": ["Randomization", "Deep learning", "More sensors", "Increasing clock speed"],
        "answer": "Randomization",
        "reason": "Randomized simple reflex agents use randomization to escape the pitfalls of predictability and infinite loops[cite: 83, 84]."
    },
    {
        "question": "What does a model-based reflex agent maintain in addition to current percepts?",
        "options": ["Internal state using an internal model of the world", "Only random numbers", "Only utility scores", "No memory at all"],
        "answer": "Internal state using an internal model of the world",
        "reason": "Model-based reflex agents maintain internal state to track the world using a model of how the world evolves and how actions affect it[cite: 86]."
    },
    {
        "question": "What is the key difference between Goal-based agents and Reflex agents?",
        "options": [
            "Goal-based agents consider future actions and choose actions to achieve specific goals rather than just automated reflex responses",
            "Reflex agents are more flexible than goal-based agents",
            "Goal-based agents do not use states",
            "Reflex agents use search and planning"
        ],
        "answer": "Goal-based agents consider future actions and choose actions to achieve specific goals rather than just automated reflex responses",
        "reason": "Goal-based agents review many actions to achieve goals and have flexibility, whereas reflex agents just have automated responses[cite: 64]."
    },
    {
        "question": "What two core aspects are involved in finding an action sequence to achieve a goal?",
        "options": [
            "Searching and Planning",
            "Compilation and Execution",
            "Encryption and Decryption",
            "Sampling and Quantization"
        ],
        "answer": "Searching and Planning",
        "reason": "Searching and planning are the two key aspects that help an agent in achieving its goal[cite: 63]."
    },
    {
        "question": "Why are goal-based agents more computationally expensive than simple reflex agents?",
        "options": [
            "Because they consider future action sequences, searching, and planning",
            "Because they have fewer rules",
            "Because they lack internal states",
            "Because they never evaluate outcomes"
        ],
        "answer": "Because they consider future action sequences, searching, and planning",
        "reason": "Goal-based agents review many actions and plan, making them computationally more expensive but much more flexible than reflex agents[cite: 64]."
    },
    {
        "question": "What limitation do goals alone have in generating high-quality behavior?",
        "options": [
            "Goals provide a crude binary distinction between 'happy' and 'unhappy' states without rating quality nuances",
            "Goals are too complex to define",
            "Goals cannot be achieved by AI",
            "Goals require zero computation"
        ],
        "answer": "Goals provide a crude binary distinction between 'happy' and 'unhappy' states without rating quality nuances",
        "reason": "Goals provide just a crude binary distinction, whereas utility-based agents score different ways to reach the goal (quicker, safer, cheaper)[cite: 66]."
    },
    {
        "question": "What does a Utility-based agent try to maximize?",
        "options": ["Performance measure / Utility score", "Number of errors", "Computational cost", "Sensor noise"],
        "answer": "Performance measure / Utility score",
        "reason": "A utility-based agent acts based on what is the best way to reach the goal, maximizing the performance measure score[cite: 68, 69]."
    },

    # Learning Agents & Problem Formulation (Lecture 7 & 8)
    {
        "question": "What are the four conceptual components of a Learning Agent?",
        "options": [
            "Critic, Learning element, Performance element, Problem generator",
            "Sensor, Actuator, Battery, Screen",
            "Input, Output, RAM, CPU",
            "Rules, Models, States, Actions"
        ],
        "answer": "Critic, Learning element, Performance element, Problem generator",
        "reason": "The four conceptual components of a learning agent are Critic, Learning element, Performance element, and Problem generator[cite: 74]."
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
        "reason": "The critic gives feedback to the learning element based on a performance standard[cite: 74]."
    },
    {
        "question": "What is the function of the Problem Generator in a learning agent?",
        "options": [
            "Suggests actions that will lead to new and informative experiences (exploration)",
            "Deletes all previous states",
            "Executes actuator commands",
            "Measures electrical consumption"
        ],
        "answer": "Suggests actions that will lead to new and informative experiences (exploration)",
        "reason": "The problem generator suggests actions that will lead to new and informative experiences[cite: 74]."
    },
    {
        "question": "What kind of agent is a problem-solving agent?",
        "options": ["A kind of 'goal-based' agent", "A simple reflex agent", "An unobservable agent", "A randomized agent"],
        "answer": "A kind of 'goal-based' agent",
        "reason": "A problem-solving agent is a kind of goal-based agent that finds sequences of actions leading to desirable states[cite: 36]."
    },
    {
        "question": "What is problem formulation?",
        "options": [
            "The process of deciding what actions and states to consider, given a goal",
            "The physical manufacturing of robot hardware",
            "The compilation of Python syntax",
            "The installation of operating systems"
        ],
        "answer": "The process of deciding what actions and states to consider, given a goal",
        "reason": "Problem formulation is the process of deciding what actions and states to consider given a goal, preceded by goal formulation[cite: 37]."
    },
    {
        "question": "What term refers to any state reachable from a given state by a single action?",
        "options": ["Successor", "Root", "Leaf", "Ancestor"],
        "answer": "Successor",
        "reason": "The term successor refers to any state reachable from a given state by a single actionTamari demand mujab, code man thi 30 minutes walo timer remove kari didho che, purana Linear Algebra na MCQs remove karine aapela slides (Machine Learning ane AI lectures) na mutabiq nawa MCQs add karvā ma aaya che. 

Neeche complete updated Python code aapelo che:

```python
import random
from groq import Groq
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI & ML Lectures LMS Quiz Portal",
    page_icon="📚",
    layout="centered",
)

# Initialize Groq client using Streamlit Secrets safely
try:
    groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
    groq_client = None

# MCQs generated from the provided AI & ML lecture slides
MCQS_DATA = [
    {
        "question": "Machine learning life cycle mein kitne major steps hote hain?",
        "options": ["5", "6", "7", "8"],
        "answer": "7",
        "reason": "Machine learning life cycle mein 7 major steps hote hain: Gathering Data, Data preparation, Data Wrangling, Analyse Data, Train the model, Test the model, Deployment[cite: 1, 2].",
    },
    {
        "question": "Machine learning life cycle ka sabse pehla step kaun sa hai?",
        "options": ["Data preparation", "Gathering Data", "Train Model", "Deployment"],
        "answer": "Gathering Data",
        "reason": "Life cycle ki shuruat data collect karne (Gathering Data) se hoti hai[cite: 2].",
    },
    {
        "question": "Data wrangling ka kya maqsad hota hai?",
        "options": [
            "Raw data ko clean aur useable format mein convert karna",
            "Model ko deploy karna",
            "Sirf graphs banana",
            "Model ko delete karna"
        ],
        "answer": "Raw data ko clean aur useable format mein convert karna",
        "reason": "Data wrangling raw data ko clean aur transform karke analysis ke kabil banati hai[cite: 4].",
    },
    {
        "question": "'Machine Learning' term kis ne aur kis saal mein coin ki thi?",
        "options": [
            "John McCarthy, 1956",
            "Arthur Samuel, 1959",
            "Alan Turing, 1950",
            "Syed Adnan, 2025"
        ],
        "answer": "Arthur Samuel, 1959",
        "reason": "The term machine learning was coined in 1959 by Arthur Samuel[cite: 10].",
    },
    {
        "question": "Artificial Intelligence (AI), Machine Learning (ML), aur Deep Learning (DL ke darmiyan kya talluq hai?",
        "options": [
            "ML is a subset of AI",
            "AI is a subset of ML",
            "DL is broader than AI",
            "Sab alag fields hain"
        ],
        "answer": "ML is a subset of AI",
        "reason": "AI ek broader family hai aur Machine Learning uska ek subset hai[cite: 31].",
    },
    {
        "question": "Supervised learning mein data kaisa hota hai?",
        "options": ["Unlabeled", "Labeled", "Random", "Audio only"],
        "answer": "Labeled",
        "reason": "Supervised learning mein input-output pairs yaani labeled data diya jata hai[cite: 21].",
    },
    {
        "question": "Unlabeled data kis learning type mein use hota hai?",
        "options": [
            "Supervised learning",
            "Unsupervised learning",
            "Reinforcement learning",
            "Classification only"
        ],
        "answer": "Unsupervised learning",
        "reason": "Unsupervised learning unlabeled datasets se inferences draw karta hai[cite: 22].",
    },
    {
        "question": "Reinforcement learning ki misaal in mein se kaun si hai?",
        "options": [
            "Dog ko trick sikhana (Reward/Punishment)",
            "Grayscale image processing",
            "Matrix multiplication",
            "Linear regression line"
        ],
        "answer": "Dog ko trick sikhana (Reward/Punishment)",
        "reason": "Reinforcement learning mein agent rewards aur punishments ke zariye seekhta hai jaise dog ko trick sikhana[cite: 23].",
    },
    {
        "question": "Data ki properties (7Vs ya 10Vs) mein 'Velocity' ka kya matlab hai?",
        "options": [
            "Scale of data",
            "Rate of data streaming and generation",
            "Meaningfulness of data",
            "Security of data"
        ],
        "answer": "Rate of data streaming and generation",
        "reason": "Velocity refers to the rate of data streaming and generation[cite: 28].",
    },
    {
        "question": "PEAS mein 'A' kis ko represent karta hai?",
        "options": ["Agent", "Actuators", "Analysis", "Architecture"],
        "answer": "Actuators",
        "reason": "PEAS stands for Performance measure, Environment, Actuators, Sensors[cite: 32].",
    },
    {
        "question": "Simple reflex agents kis rule par kaam karte hain?",
        "options": [
            "Condition-action rule",
            "Deep neural networks",
            "Reinforcement rewards",
            "Unsupervised clustering"
        ],
        "answer": "Condition-action rule",
        "reason": "Simple reflex agents make use of condition-action rules based on current percept[cite: 79].",
    },
    {
        "question": "Goal-based agents kis tarah ke agents hote hain?",
        "options": [
            "Jo sirf reflex action karte hain",
            "Jo apne goals ko achieve karne ke liye actions choose karte hain",
            "Jo sirf random move karte hain",
            "Jinhein koi goal nahi chahiye hota"
        ],
        "answer": "Jo apne goals ko achieve karne ke liye actions choose karte hain",
        "reason": "Goal-based agents choose their actions in order to achieve specific goals[cite: 60].",
    },
    {
        "question": "Utility-based agents aur Goal-based agents mein main fark kya hai?",
        "options": [
            "Utility agent performance measure/score ko maximize karta hai",
            "Goal agent utility use nahi karta",
            "Donon bilkul same hain",
            "Utility agent slow hota hai"
        ],
        "answer": "Utility agent performance measure/score ko maximize karta hai",
        "reason": "Utility agents provide solutions that maximize the performance measure (utility)[cite: 68].",
    },
    {
        "question": "Learning agent ke four conceptual components mein kaun sa shamil hai?",
        "options": [
            "Critic",
            "Compiler",
            "Database",
            "Monitor"
        ],
        "
