from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    print("GROQ_API_KEY not set")
else:
    print("Working ")
model = ChatGroq(model="llama-3.3-70b-versatile")

prompt=PromptTemplate(
    template="The summery of this documents {text}",
    input_variables=['text']
)

parser=StrOutputParser()

loader=TextLoader('word.txt',encoding='utf-8')

docs=loader.load()
print(type(docs))
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)

chain=prompt|model|parser

print(chain.invoke({'text':docs[0].page_content}))