from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, PydanticOutputParser
from pydantic import BaseModel,fields
from dotenv import load_dotenv
import os

# API checking
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if api_key is None:
    print("The api key is not loaded.")
else:
    print("The api key is loaded.") 

# Class definition
class person(BaseModel):
    name:str
    age:int
    city:str
    profession:str

#calling pydanticoutputparser
parser=PydanticOutputParser(pydantic_object=person)    


# Prompt template
template = PromptTemplate(
    template="Explain the following concept in simple terms: {concept} {format_instructions}",
    input_variables=["concept"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Main code
llm = ChatGroq(model="llama-3.3-70b-versatile")
chain = template | llm | parser

topic_input = input("Enter a concept you want to learn about: ")
result = chain.invoke({"concept": topic_input})

# Displaying the result
print("\n--- Result ---\n")
print(result)
