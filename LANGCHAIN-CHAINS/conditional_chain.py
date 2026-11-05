from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGroq(model="openai/gpt-oss-20b", temperature=0.1, max_tokens=1000)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    # partial_variables={'format_instruction':parser2.get_format_instructions()}
)

clasifire_chain = prompt1 | model1 | parser

