from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
)

loader = PyPDFLoader("wadhaawani.pdf")
docs = loader.load()

chunks = text_splitter.split_documents(docs)

print(chunks[5].page_content)
