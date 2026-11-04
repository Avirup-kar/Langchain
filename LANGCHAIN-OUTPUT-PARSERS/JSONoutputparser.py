from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.1, max_tokens=500)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = template.format_prompt()

result = model.invoke(prompt)

final_result = parser.parse(result.content)
print(final_result)
print(final_result['name'])