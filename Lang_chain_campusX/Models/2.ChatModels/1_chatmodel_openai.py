from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
print("Api Key loaded")
llm = ChatGroq(model="llama-3.3-70b-versatile")
result = llm.invoke("hey this is a testing of of llm chat model i am learning write how are you ")

print(result.content)
