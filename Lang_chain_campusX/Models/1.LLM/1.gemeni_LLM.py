from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print("API key loaded successfully!")  
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
result = llm.invoke("What is the capital of India?")
print(result.content)
