from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv
import os

load_dotenv()

# Check API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable not set")

# Prompt templates
prompt_simple = PromptTemplate(
    template="Explain the following in simple terms: {text}",
    input_variables=["text"]
)

prompt_5lines = PromptTemplate(
    template="Explain the following in 5 lines: {text}",
    input_variables=["text"]
)

# Output parser
parser = StrOutputParser()

# Model
llm = ChatGroq(model="llama-3.3-70b-versatile")

# Parallel chain: two outputs simultaneously
parallel_chain = RunnableParallel({
    "simple": RunnableSequence(prompt_simple, llm, parser),
    "five_lines": RunnableSequence(prompt_5lines, llm, parser)
})

# Invoke parallel chain
result = parallel_chain.invoke({"text": "Nvidia vs AMD"})

# Print results
print("Simple explanation:\n", result["simple"])
print("\nFive-line explanation:\n", result["five_lines"])
