from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from dotenv import load_dotenv
import os

#load environment variables from a .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY") 
if api_key is None:
    print("GROQ_API_KEY environment variable not set")   
else:
    print("GROQ_API_KEY found")


# Define the response schema
schema=[
    ResponseSchema(
        name="notes", 
        description="Detailed notes on the topic provided."
    ),
    ResponseSchema(
        name="quiz", 
        description="A quiz based on the notes provided."
    )
]
parser=StructuredOutputParser.from_response_schemas(schema)


# Template 1: Generate a detailed Notes 
PromptTemplate_1=PromptTemplate(
    template="Write detailed notes on the following topic: {topic} {format_instructions}",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
    )

# Template 2: Generate a Quiz from the Notes   
PromptTemplate_2=PromptTemplate(
    template="Create a quiz based on the following notes: {topic} {format_instructions} ",
    input_variables=["topic"],
    partial_variables={
    "format_instructions": parser.get_format_instructions()
    }
    )

#template_3 : Compile Notes and Quiz
PromptTemplate_3=PromptTemplate(
    template="Compile the following notes and quiz into a single document.\n\nNotes:\n{notes_chain}\n\nQuiz:\n{quiz_chain}\n {format_instructions}",
    input_variables=["notes_chain","quiz_chain"],
    partial_variables={ 
        "format_instructions": parser.get_format_instructions()
    }
    )

# Define the Model and Output Parser
llm=ChatGroq(model="llama-3.3-70b-versatile")
llm_m=ChatGroq(model="llama-3.3-70b-versatile")
llm_d=ChatGroq(model="llama-3.3-70b-versatile")
parser_str=StrOutputParser()

# Define and parallel chain
parallel_chain= RunnableParallel({
    "notes_chain": PromptTemplate_1 | llm | parser_str,
    "quiz_chain": PromptTemplate_2 | llm_d | parser_str
})
chain=parallel_chain | PromptTemplate_3 | llm_m | parser

# The topic and graphs 
chain.get_graph().print_ascii()
topic="Gean AI (Hub & Smart Solutions) is a UAE-based company building generative AI and “digital + smart” solutions across industries (retail, hospitality, real estate, education, etc.). Their services include things like digital humans / avatars, talking photos, AI tracking, smart hotels, IoT integration. They aim for immersive & tailored AI experiences and partner with entities like Investopia and EROS Investments"
 

# Run the chain
result=chain.invoke({"topic": topic})
print(result)