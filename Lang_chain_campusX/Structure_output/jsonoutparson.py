from langchain_groq import ChatGroq 
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
import os
#api checking 
load_dotenv()
Api_key = os.getenv("GROQ_API_KEY")

if Api_key is None:
    print("The api key is not loaded.")
else:
    print("The api key is loaded.")

#parser calling
parser=JsonOutputParser()

#1.st prompt

prompt_template_1=PromptTemplate(
template="As a teacher explain the following concept in simple terms: {concept} {format_instructions}",
input_variables=["concept"],
partial_variables={"format_instructions": parser.get_format_instructions()}
)

#2.nd prompt
prompt_template_2=PromptTemplate(
    template="Explain the following concept in 5 lines or less: {text} {format_instructions}",
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

#Main code 

llm = ChatGroq(model="llama-3.3-70b-versatile")


chain=prompt_template_1|llm|parser| (lambda x: {"text": str(x)})|prompt_template_2|llm|parser

result=chain.invoke({"concept":"photosynthesis"})

print("\n---  Result loading t: ---\n")
print(result)
print(type(result))