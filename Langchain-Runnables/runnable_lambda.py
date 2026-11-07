from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.1, max_tokens=200)

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

jock_gen_chain = RunnableSequence(prompt, model, parser)

def count_joke(joke: str) -> int:
    return len(joke.split())

parallel_chain = RunnableParallel({
    'jock': RunnablePassthrough(),
    'count': RunnableLambda(count_joke)
})

final_chain = jock_gen_chain | parallel_chain

result = final_chain.invoke({'topic': 'cat'})

print("Joke:")
print(result['jock'])   
print("Count:")
print(result['count'])