from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model1 = ChatGroq(model="openai/gpt-oss-20b", temperature=0.1, max_tokens=1000)

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model1 | parser2

result = classifier_chain.invoke({'feedback': 'This is a wonderful smartphone'})

print(result.sentiment)  # Output: Feedback(sentiment='negative')