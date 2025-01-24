import os
import sys
from openai import OpenAI
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config import Config

class PersonalAIAssistant:
    def __init__(self):
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.conversation_history = []

    def chat(self, user_input):
        try:
            # Add user input to conversation history
            self.conversation_history.append({"role": "user", "content": user_input})
            
            # Get response from OpenAI
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.conversation_history,
                max_tokens=150,
                temperature=0.7
            )

            # Extract and store assistant's response
            assistant_response = response.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
            
            return assistant_response

        except Exception as e:
            return f"An error occurred: {str(e)}"

def main():
    assistant = PersonalAIAssistant()
    print("Personal AI Assistant initialized. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
            
        response = assistant.chat(user_input)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()