from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import streamlit as st
from dotenv import load_dotenv
import os 

# importing Api_key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if api_key is None:
    st.warning("GROQ_API_KEY is not set. Please set it in your environment variables.")
else:
    st.header('API key loaded successfully!')

st.title("Chatbot_UI_Streamlit_Groq")

llm = ChatGroq(model="llama-3.3-70b-versatile")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content='You are a helpful assistant.')
    ]

User_input = st.text_input("You:", key="user_input")

if User_input:
    if User_input == "exit":
        st.stop()
    
    st.session_state.chat_history.append(
        HumanMessage(content=User_input)
    )
    
    result = llm.invoke(st.session_state.chat_history)
    st.session_state.chat_history.append(AIMessage(content=result.content))
    st.write("AI: " + result.content)