import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Configure the Google Generative AI client
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found. Please set it in the .env file.")
genai.configure(api_key=api_key)

# Initialize the Gemini chat model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


# Function to get a response from the Gemini model
def get_gemini_response(question):
    try:
        response = chat.send_message(question, stream=True)
        return response
    except Exception as e:
        return f"Error: {str(e)}"


# Main CLI Loop
def main():
    print("Welcome to the Gemini Chatbot!")
    print("Type 'exit' to quit the program.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit": 
            print("Goodbye!")
            break

        response = get_gemini_response(user_input)
        print("\nGemini: ")
        for chunk in response:
            print(chunk.text, end="")
        print("\n" + "_" * 80)  # Separator line
        print("Chat history:", chat.history)


if __name__ == "__main__":
    main()
