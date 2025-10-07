from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from dotenv import load_dotenv
import os
#load environment variables from a .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if api_key is None:
    raise ValueError("GROQ_API_KEY environment variable not set")   
else:
    print("GROQ_API_KEY found")


# Define the response schema
schema=[
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

# Create the structured output parser
parser = StructuredOutputParser.from_response_schemas(schema)

# Define the prompt template
template_1=PromptTemplate(
    template="Write a detailed explanation of the following topic: {topic} {format_instructions}",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": "{format_instructions}"
    }
    )

#2nd_template 
template_2=PromptTemplate(
    template="Write a detailed explanations of the following topic in 5 lines : {text}{format_instructions}",
    input_variables=["text"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
    )

# Initialize the Groq model
model = ChatGroq(model="llama-3.3-70b-versatile")
parser_str=StrOutputParser()
chain=template_1|model|parser_str|template_2|model|parser
chain.get_graph().print_ascii()
result=chain.invoke({"topic": "Quantum Computing"})
print(result)