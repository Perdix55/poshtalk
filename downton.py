import streamlit as st
from transformers import pipeline

# Load the language model pipeline for text transformation
translator = pipeline("text2text-generation", model="t5-base")  # Using T5 model as an example

# Streamlit App
st.title("Chat to Posh Old English Converter")
st.write("Transform your modern chats into posh old English sentences with this fun app.")

# Input box for user chat message
user_input = st.text_area("Enter your chat message here:", height=100)

# Button to trigger the transformation
if st.button("Convert to Posh Old English"):
    if user_input.strip():
        # Process the input using the language model
        transformed_text = translator(f"Translate this modern English sentence to posh old English: {user_input}")
        output_text = transformed_text[0]['generated_text']
        
        # Display the original and transformed text
        st.subheader("Transformation Result")
        st.markdown(f"**Input:** {user_input}")
        st.markdown(f"**Output:** {output_text}")
    else:
        st.error("Please enter a valid chat message.")

# Button to reset the input and output
if st.button("Reset"):
    st.experimental_rerun()

# Example transformations
st.sidebar.header("Examples")
st.sidebar.markdown("**Modern:** Hello, how are you today?")
st.sidebar.markdown("**Old English:** Greetings, how dost thou fare this fine day?")
st.sidebar.markdown("**Modern:** Can we meet at 5 PM?")
st.sidebar.markdown("**Old English:** Might we convene at the fifth hour of the clock?")
