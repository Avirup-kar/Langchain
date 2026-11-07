from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.1, max_tokens=1000)

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

loader = TextLoader('cricket.txt', encoding='utf-8')
docs = loader.load()

# print(type(docs))
# print(docs[0].page_content)

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))
