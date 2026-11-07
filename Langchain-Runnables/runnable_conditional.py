from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnableSequence, RunnablePassthrough

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.1, max_tokens=1000)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

first_chain = RunnableSequence(prompt1, model, parser)

conditional_chain = RunnableBranch(
    (lambda x: len(x.split())>500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
    )

final_chain = first_chain | conditional_chain

res = final_chain.invoke({'topic': 'Russia vs ukraine'})

print(res)