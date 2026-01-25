from langchain_groq import ChatGroq
from langchain_community.document_loaders import CSVLoader
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
    template=("Analyze the this file tell me data least aged person .\n\n"
        "Text A:\n{text}\n\n"),
    input_variables=['text']
)

parser=StrOutputParser()
loader = CSVLoader(file_path='Social_Network_Ads.csv')
docs=loader.load()
print(type(docs))
print(len(docs))
print(docs[0].metadata)


chain=prompt|model|parser

print(chain.invoke({'text':docs[0].page_content}))