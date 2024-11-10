import os
from dotenv import load_dotenv

load_dotenv()

def get_openai_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise Exception("OPENAI_API_KEY is not set")    
    return api_key