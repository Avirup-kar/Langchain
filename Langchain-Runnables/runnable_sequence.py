from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.1, max_tokens=200)

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke {text}',
    input_variables=['text']
)

# chain = RunnableSequence(prompt, model, parser, prompt2, model, parser) ## using RunnableSequence to create a chain
chain = prompt | model | parser | prompt2 | model | parser ## using the pipe operator to create a RunnableSequence

result = chain.invoke({'topic': 'cat'})

print(result)