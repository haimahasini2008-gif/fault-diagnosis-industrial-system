import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# ------------------------------
# PAGE TITLE
# ------------------------------
st.set_page_config(page_title="AI Fault Diagnosis System")

st.title("AI-Based Fault Diagnosis System")
st.subheader("CO-wise AI Mini Project")

# ------------------------------
# CO1 – RULE-BASED DIAGNOSIS
# ------------------------------
st.header("CO1 – Rule-Based Diagnosis")

knowledge_base = {
    "System Slow": "Possible RAM Issue",
    "Overheating": "Cooling Fan Failure",
    "No Internet": "Router/Network Adapter Issue",
    "Battery Draining": "Battery Health Problem",
    "Blue Screen": "Operating System Failure"
}

symptom = st.selectbox(
    "Select System Symptom",
    list(knowledge_base.keys())
)

if st.button("Run Rule-Based Diagnosis"):
    st.success(f"Diagnosis Result: {knowledge_base[symptom]}")

# ------------------------------
# CO2 – SEARCH GRAPH
# ------------------------------
st.header("CO2 – Search Technique")

fault_graph = {
    "Start": ["Check Power", "Check Internet"],
    "Check Power": ["Battery Fault"],
    "Check Internet": ["Router Fault"]
}

st.write("Fault Diagnosis Graph:")
st.write(fault_graph)

# ------------------------------
# CO3 – CONSTRAINT SATISFACTION
# ------------------------------
st.header("CO3 – Constraint Satisfaction")

temperature = st.slider("System Temperature", 0, 120, 70)
fan_running = st.checkbox("Cooling Fan Running")

if st.button("Check Constraints"):
    if temperature > 80 and not fan_running:
        st.error("Constraint Violated: Cooling Fan Failure")
    else:
        st.success("System Constraints Satisfied")

# ------------------------------
# CO4 – PROBABILISTIC REASONING
# ------------------------------
st.header("CO4 – Probabilistic Diagnosis")

fault_probability = {
    "Battery Fault": 0.7,
    "RAM Fault": 0.2,
    "Virus": 0.1
}

st.write("Fault Probabilities")

prob_df = pd.DataFrame(
    fault_probability.items(),
    columns=["Fault", "Probability"]
)

st.table(prob_df)

# ------------------------------
# CO5 – MACHINE LEARNING MODEL
# ------------------------------
st.header("CO5 – Machine Learning Diagnosis")

X = [
    [1, 0],
    [1, 1],
    [0, 1],
    [0, 0]
]

Y = [
    "Battery Fault",
    "Overheating",
    "Network Fault",
    "Normal"
]

model = DecisionTreeClassifier()
model.fit(X, Y)

power_issue = st.selectbox("Power Issue", [0, 1])
network_issue = st.selectbox("Network Issue", [0, 1])

if st.button("Predict Fault"):
    prediction = model.predict([[power_issue, network_issue]])
    st.success(f"Predicted Fault: {prediction[0]}")

# ------------------------------
# CO6 – FINAL INTELLIGENT AGENT
# ------------------------------
st.header("CO6 – Intelligent Agent System")

st.write("This AI agent combines:")
st.write("- Rule-Based Diagnosis")
st.write("- Search Techniques")
st.write("- Constraint Satisfaction")
st.write("- Probabilistic Reasoning")
st.write("- Machine Learning")

st.success("Integrated Fault Diagnosis System Successfully Running")
