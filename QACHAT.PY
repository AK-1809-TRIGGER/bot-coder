from dotenv import load_dotenv

load_dotenv()  # Loading all the environment variables

from dotenv import load_dotenv

load_dotenv()  # Load environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure the Google Generative AI client
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])


def get_gemini_response(question):
    try:
        # Generate a response for the question
        response = chat.send_message(question, stream=True)
        # Combine all response chunks into a single string
        full_response = "".join(chunk.text for chunk in response)
        return full_response
    except Exception as e:
        return f"Error: {str(e)}"


# Initialize the Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input and submission handling
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input:
    # Add user query to session state chat history
    st.session_state['chat_history'].append(("You", input))

    # Call the Gemini API to generate a response
    bot_response = get_gemini_response(input)

    # Add bot response to the chat history
    st.session_state['chat_history'].append(("Bot", bot_response))

# Display the chat history
st.subheader("Chat History")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")

