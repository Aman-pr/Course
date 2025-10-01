from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
print("API key loaded successfully!")  # safe to print
llm = ChatGroq(model="llama-3.3-70b-versatile")
result = llm.invoke("What is the capital of India")

print(result.content)
