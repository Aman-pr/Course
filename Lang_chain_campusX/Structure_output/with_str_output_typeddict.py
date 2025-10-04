from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict , Annotated
import streamlit as st
import time
import os 


st.title("Sentiment Analysis with TypedDict Output")

#api loading
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if api_key is None:
    st.write("GROQ_API_KEY environment variable not set.")
else:
    st.warning("GROQ_API_KEY environment variable is set.")

llm = ChatGroq(model="llama-3.3-70b-versatile")
#typing dict
class SentimentCheck(TypedDict):
    key_themes: Annotated[list[str],"A list of key themes identified in the text."]
    key_words: Annotated[list[str],"A list of key keywords identified in the text."]
    pros=Annotated[list[str],"A list of positive aspects mentioned in the text."]
    dows=Annotated[list[str],"A list of negative aspects mentioned in the text."]
    sentiment: Annotated[str,"The sentiment of the text, either 'positive', 'negative', or 'neutral' "]
    confidence: Annotated[float,"A float between 0 and 1 representing the confidence level of the sentiment analysis."]

structure_model = llm.with_structured_output(SentimentCheck)    

sentiment_check_data=st.text_area("Enter text to analyze sentiment:")
result=structure_model.invoke(sentiment_check_data )
st.write("Analysis in progress wait plz")
time.sleep(2)
st.write(result)