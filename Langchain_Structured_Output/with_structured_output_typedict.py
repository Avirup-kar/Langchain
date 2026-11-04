from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.1, max_tokens=500)

# schema
class Review(TypedDict):
    summary: str
    sentiment: str
    
structured_model = model.with_structured_output(
        Review,
        method="json_schema",
        strict=True
    )

result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

print(f"Summary: {result['summary']}")
print(f"Sentiment: {result['sentiment']}")