import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    MODEL_NAME = "gpt-3.5-turbo"
    MAX_TOKENS = 150
    TEMPERATURE = 0.7