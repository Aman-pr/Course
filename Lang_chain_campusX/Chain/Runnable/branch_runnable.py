from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableBranch, RunnablePassthrough
from dotenv import load_dotenv
import os

load_dotenv()

# Load API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("GROQ_API_KEY environment variable not set")   
else:
    print("GROQ_API_KEY environment variable found")

# Prompt templates
prompt_report = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

prompt_summary = PromptTemplate(
    template="Summarize the following text:\n{text}",
    input_variables=["text"]
)

# Output parser
output_parser = StrOutputParser()

# Model
llm = ChatGroq(model="llama-3.3-70b-versatile")  # Replace with your model name

# Branch: If the report has >300 words, summarize it
branch = RunnableBranch(
    condition=lambda x: len(x.split()) > 300,
    true=RunnableSequence(prompt_summary, llm, output_parser),
    false=RunnablePassthrough()
)

# Full runnable sequence
final_runnable = RunnableSequence(
    prompt_report,  # Generate report
    llm,
    output_parser,
    branch           # Conditionally summarize
)

# Invoke
result = final_runnable.invoke({"topic": "Russia vs Ukraine"})
print(result)
