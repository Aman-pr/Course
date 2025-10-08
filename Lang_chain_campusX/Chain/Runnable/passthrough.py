from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough
import os
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("GROQ_API_KEY environment variable not set")   
else:
    print("GROQ_API_KEY environment variable found")

#Prompt template
template = PromptTemplate(
    template="Explain the following in simple terms: {text}",
    input_variables=["text"]
)

template_2 = PromptTemplate(
    template="Explain the following in 5 lines: {text}",
    input_variables=["text"]
)

#Output parser
output_parser = StrOutputParser()

#Model
llm=ChatGroq(model="llama-3.3-70b-versatile")

#Runnable sequence
runnable_passthrough = RunnablePassthrough()
runnable = RunnableSequence(
    template,llm,output_parser,runnable_passthrough,llm,template_2
)
result=runnable.invoke({"text":"Nividia vs AMD"})
print(result)