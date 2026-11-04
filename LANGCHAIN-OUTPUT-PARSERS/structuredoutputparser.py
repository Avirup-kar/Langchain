from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.1, max_tokens=500)

schema = [
    ResponseSchema (name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema (name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema (name='fact_3', description='Fact 3 about the topic'),
]