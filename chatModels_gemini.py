from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=api_key,   
    temperature=0.1
)


que = llm.invoke("Tell me interesting facts about Mumbai?")


print(que.content)
