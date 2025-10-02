from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
import os
import streamlit as st


#title
api_key = os.getenv("GROQ_API_KEY")
st.title("UI_Streamlit_Groq")

#Checking if API key is loaded
load_dotenv()
if api_key is None:
    st.warning("GROQ_API_KEY is not set. Please set it in your environment variables.")
else:
    st.header('API key loaded successfully!')
st.header('Research Tool')

#loding model 
llm = ChatGroq(model="llama-3.3-70b-versatile")

paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )
style_input =st.selectbox("Select Style", ["Formal", "Informal", "Technical", "Simplified"])
length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt("template.json")

if st.button("Summarize"):
    chain=template | llm
    result=chain.invoke({'paper_input':paper_input,'style_input':style_input,'length_input':length_input})
    st.write(result.content)
