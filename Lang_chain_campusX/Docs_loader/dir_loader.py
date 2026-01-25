from langchain_groq import ChatGroq
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
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
    template=("Analyze the relationship between the following two texts.\n\n"
        "Text A:\n{text}\n\n"
        "Text B:\n{text_2}\n\n"),
    input_variables=['text','text_2']
)

parser=StrOutputParser()

loader=DirectoryLoader(path='books',
                       glob='*.pdf',
                       loader_cls=PyPDFLoader
                       )

docs=loader.load()
print(type(docs))
print(len(docs))
print(docs[0].metadata)
print(docs[14].metadata)

chain=prompt|model|parser

print(chain.invoke({'text':docs[0].page_content,'text_2':docs[13].page_content})) 