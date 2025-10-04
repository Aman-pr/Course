from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
Api_key = os.getenv("GROQ_API_KEY")

if Api_key is None:
    print("The api key is not loaded.")
else:
    print("The api key is loaded.")

llm = ChatGroq(model="llama-3.3-70b-versatile")
#1.st prompt

prompt_template_1="As a teacher explain the following concept in simple terms: {concept}"

result_1=llm.invoke(prompt_template_1.format(concept="photosynthesis"))

print("1.st prompt result:\n", result_1)

#2.nd prompt
prompt_template_2="Explain the following concept in 5 lines or less: {concept} "
result_2=llm.invoke(prompt_template_2.format(concept=result_1.content))


print("\n--- 2.nd prompt result: ---\n")
for line in result_2.content.split('.'):
    print(line)