from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text_splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=" "
)

loader = PyPDFLoader("wadhaawani.pdf")
docs = loader.load()

chunks = text_splitter.split_documents(docs)

print(chunks[1].page_content)
