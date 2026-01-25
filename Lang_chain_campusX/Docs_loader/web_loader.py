import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    print("GROQ_API_KEY not set")
else:
    print("Working ")
model = ChatGroq(model="llama-3.3-70b-versatile")

parser=StrOutputParser()

URL = "https://docs.langchain.com/"
loader = WebBaseLoader(URL)

docs = list(loader.lazy_load())

print(type(docs))
print(len(docs))
print(docs[0].metadata)

template=PromptTemplate(
    template="what is this page about {text}",
    input_variables=['text']
)
chain=template|model|parser

print(chain.invoke(docs[0].page_content))