from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel
from dotenv import load_dotenv
import os

load_dotenv()

# Check API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable not set")

# Function to count words
def word_count(text):
    return len(text.split())

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

# Sequence to generate explanation
explanation_chain = RunnableSequence(prompt_simple, llm, parser)

# Parallel chain to do multiple things with the generated explanation
post_process_chain = RunnableParallel({
    "original": RunnablePassthrough(),
    "word_count": RunnableLambda(word_count)
})

# Full sequential chain: generate -> post-process
final_chain = RunnableSequence(explanation_chain, post_process_chain)

# Invoke
result = final_chain.invoke({"text": "Nvidia vs AMD"})

# Print
final_result = """{} \nWord count: {}""".format(result["original"], result["word_count"])
print(final_result)
