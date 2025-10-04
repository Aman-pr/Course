from langchain_groq import ChatGroq 
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
#api checking 
load_dotenv()
Api_key = os.getenv("GROQ_API_KEY")

if Api_key is None:
    print("The api key is not loaded.")
else:
    print("The api key is loaded.")

#1.st prompt

prompt_template_1=PromptTemplate(
template="As a teacher explain the following concept in simple terms: {concept}",
input_variables=["concept"]
)

#2.nd prompt
prompt_template_2=PromptTemplate(
    template="Explain the following concept in 5 lines or less: {text} "
    ,
    input_variables=["text"]
)

#Main code 

llm = ChatGroq(model="llama-3.3-70b-versatile")

parser=StrOutputParser()

chain=prompt_template_1|llm|parser|prompt_template_2|llm|parser

result=chain.invoke({"concept":"photosynthesis"})

print("\n---  Result loading t: ---\n")
print(result)