from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional
from pydantic import BaseModel, Field
import time
import os 


print("Sentiment Analysis with TypedDict Output")

#api loading
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if api_key is None:
    print("GROQ_API_KEY environment variable not set.")
else:
    print("GROQ_API_KEY environment variable is set.")

llm = ChatGroq(model="llama-3.3-70b-versatile")

#typing dict
class SentimentCheck(BaseModel):
    key_themes: list[str] = Field(description="A list of key themes identified in the text.")
    key_words: list[str] = Field(description="A list of key words identified in the text.")
    pros: list[str] = Field(description="A list of postive aspects mentioned in the text.")
    dows: list[str] = Field(description="A list of neagtive aspects mentioned in the text.")
    sentiment: Optional[str] = Field(description="The overall sentiment of the text, which can be 'negative', 'neutral', or 'positive'.")   
    confidence: float = Field(description="A confidence score between 0 and 1 indicating the certainty of the sentiment analysis.")     
    impact_rate: float = Field(description="A score between 0 and 1 indicating the potential impact of the sentiment on the subject matter.")

structure_model = llm.with_structured_output(SentimentCheck)    

sentiment_check_data = input("Enter text to analyze sentiment: ")
result = structure_model.invoke(sentiment_check_data)
print("Analysis in progress wait plz")
time.sleep(2)
print(result)
result_json = result.model_dump_json()
print("JSON Output:")
print(result_json)