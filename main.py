import streamlit as st

st.title("Clinical Decision Support System")

# Create an input box for user text
user_input = st.text_input("Enter some text:")

# Display what the user entered
if user_input:
    st.write("You entered:")
    st.write(user_input)