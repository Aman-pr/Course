from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
 
load_dotenv()

llm=ChatGroq(model="llama-3.3-70b-versatile")

message=[
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="tell me about langchain?"),
]

result=llm.invoke(message)
message.append(AIMessage(content=result.content))
print(message)