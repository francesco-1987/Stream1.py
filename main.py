import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Set OpenAI API key (from Streamlit secrets, as in the original code)
openai_api_key = st.secrets["openai_api_key"]

st.title("Dental Decision Support System")

# Initialize the ChatOpenAI model (adjust parameters as needed)
chat = ChatOpenAI(
    model="gpt-4",
    openai_api_key=openai_api_key,
    temperature=0.7,
    max_tokens=200
)

# Create input boxes for user input
user_input_symptoms = st.text_input("Enter Initial list of SYMPTOMS:")
user_input_history = st.text_input("Enter MEDICAL HISTORY:")

# Button to get possible conditions
if st.button("Initial diagnosis and additional symptoms to check for final diagnosis"):
    if user_input_symptoms and user_input_history:
        with st.spinner("Analyzing..."):
            try:
                # Combine user inputs into a prompt
                prompt = (
                    "You are a medical assistant specializing in dentistry that is trying to reach a diagnosis of the dental condition before the patient visits the dentist. Based on the following inputs"
                    f"- Symptoms: {user_input_symptoms}\n"
                    f"- Medical History: {user_input_history}\n"
                    "provide an initial diagnosis of the list of possible dental conditions. "
                    "provide as well a list of 2-3 additional symptoms to check to reach the final diagnosis.Ensure your request for additional symptoms minimize the number of questions through a very smart process of entropy minimization"
                )

                # Call the LangChain LLM
                response = chat([HumanMessage(content=prompt)])
                result = response.content

                # Display the result
                st.subheader("Possible Conditions:")
                st.write(result)

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in both fields before submitting!")

# Create input boxes for user input
additional_input_symptoms = st.text_input("Enter Additional list of SYMPTOMS:")

# Button to get final diagnosis
if st.button("Final Diagnosis pre-visit"):
    if user_input_symptoms and user_input_history and additional_input_symptoms:
        with st.spinner("Analyzing..."):
            try:
                # Combine user inputs into a prompt
                prompt = (
                    "You are a medical assistant specializing in dentistry that is trying to reach a diagnosis of the dental condition before the patient visits the dentist. Based on the following inputs"
                    f"- Symptoms: {user_input_symptoms} {additional_input_symptoms}\n"
                    f"- Medical History: {user_input_history}\n"
                    "provide the most likely diagnosis of the dental condition with a probability percent number"
                    "Provide a list of additional tests that the dentist might run once the patient comes for the visit"
                )

                # Call the LangChain LLM
                response = chat([HumanMessage(content=prompt)])
                result = response.content

                # Display the result
                st.subheader("Possible Conditions:")
                st.write(result)

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in both fields before submitting!")

# Create input boxes for user input
final_diagnosis = st.text_input("Enter final DIAGNOSIS based on visit:")

# Button to get final diagnosis
if st.button("Possible Treatments"):
    if user_input_symptoms and user_input_history and additional_input_symptoms:
        with st.spinner("Analyzing..."):
            try:
                # Combine user inputs into a prompt
                prompt = (
                    "You are a medical assistant specializing in dentistry that given a final diagnosis wants to offer the patient different treatment options along with pros and cons of each. Based on the following inputs"
                    f"- diagnosis: {final_diagnosis}\n"
                    f"- Medical History: {user_input_history}\n"
                    "provide the treatment options along with pros and cons of each"
                )

                # Call the LangChain LLM
                response = chat([HumanMessage(content=prompt)])
                result = response.content

                # Display the result
                st.subheader("Possible Conditions:")
                st.write(result)

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in both fields before submitting!")
