from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from dotenv import load_dotenv
import os

# API checking
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if api_key is None:
    print("The api key is not loaded.")
else:
    print("The api key is loaded.") 

# Schema definition
schemas = [
    ResponseSchema(
        name="explanation", 
        description="A detailed explanation of the concept in simple terms."
    ),
    ResponseSchema(
        name="summary", 
        description="A brief summary of the explanation in 3 lines or less."
    ),
    ResponseSchema(
        name="keywords", 
        description="A list of keywords related to the concept."
    )
]

# StructuredOutputParser call 
parser = StructuredOutputParser.from_response_schemas(schemas)

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
