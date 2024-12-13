import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

openai_api_key = st.secrets["openai_api_key"]

st.title("Dental Decision Support System")

chat = ChatOpenAI(
    model="gpt-4",
    openai_api_key=openai_api_key,
    temperature=0.7,
    max_tokens=200
)

user_input_symptoms = st.text_input("Enter Initial list of SYMPTOMS:")
user_input_history = st.text_input("Enter MEDICAL HISTORY:")

if st.button("Initial diagnosis and additional symptoms to investigate"):
    if user_input_symptoms and user_input_history:
        with st.spinner("Analyzing..."):
            try:
                prompt = (
                    "You are a medical assistant specializing in dentistry that is trying to reach a diagnosis of the dental condition before the patient visits the dentist. Based on the following inputs "
                    f"- Symptoms: {user_input_symptoms}\n"
                    f"- Medical History: {user_input_history}\n"
                    "provide an initial diagnosis of the list of possible dental conditions. "
                    "provide as well a list of 2-3 additional symptoms to check to reach the final diagnosis. Ensure your request for additional symptoms minimize the number of questions through a very smart process of entropy minimization."
                )
                response = chat([HumanMessage(content=prompt)])
                result = response.content
                st.session_state["initial_diagnosis"] = result  # Store in session state
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in both fields before submitting!")

# Display initial diagnosis if available
if "initial_diagnosis" in st.session_state:
    st.subheader("Initial Diagnosis pre-visit:")
    st.write(st.session_state["initial_diagnosis"])

additional_input_symptoms = st.text_input("Enter Additional list of SYMPTOMS:")

if st.button("Final Diagnosis pre-visit"):
    if user_input_symptoms and user_input_history and additional_input_symptoms:
        with st.spinner("Analyzing..."):
            try:
                prompt = (
                    "You are a medical assistant specializing in dentistry that is trying to reach a diagnosis of the dental condition before the patient visits the dentist. Based on the following inputs "
                    f"- Symptoms: {user_input_symptoms} {additional_input_symptoms}\n"
                    f"- Medical History: {user_input_history}\n"
                    "provide the most likely diagnosis of the dental condition with a probability percent number "
                    "Provide a list of additional tests that the dentist might run once the patient comes for the visit."
                )
                response = chat([HumanMessage(content=prompt)])
                result = response.content
                st.session_state["final_diagnosis"] = result
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in all fields before submitting!")

# Display final diagnosis if available
if "final_diagnosis" in st.session_state:
    st.subheader("Final Diagnosis:")
    st.write(st.session_state["final_diagnosis"])

final_diagnosis = st.text_input("Enter final DIAGNOSIS based on visit:")

if st.button("Possible Treatments"):
    if user_input_symptoms and user_input_history and additional_input_symptoms and final_diagnosis:
        with st.spinner("Analyzing..."):
            try:
                prompt = (
                    "You are a medical assistant specializing in dentistry that given a final diagnosis wants to offer the patient with different treatment options along with pros and cons of each alson including drug-drug interactions. Based on the following inputs "
                    f"- diagnosis: {final_diagnosis}\n"
                    f"- Medical History: {user_input_history}\n"
                    "provide the treatment options along with pros and cons of each."
                )
                response = chat([HumanMessage(content=prompt)])
                result = response.content
                st.session_state["treatments"] = result
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in all fields before submitting!")

# Display treatments if available
if "treatments" in st.session_state:
    st.subheader("Possible Treatments:")
    st.write(st.session_state["treatments"])