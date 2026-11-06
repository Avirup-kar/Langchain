from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0
)

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

