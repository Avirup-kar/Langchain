from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv


load_dotenv()
model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.1, max_tokens=500)


messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)