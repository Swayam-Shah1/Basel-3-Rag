import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from fastapi import FastAPI

app = FastAPI()
load_dotenv()

LLM_URL = os.getenv("LLM_URL")
LLM_MODEL = os.getenv("LLM_MODEL")

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/ask")
def ask(question: str):
    return {"message": llm.invoke(question)}

llm = ChatOpenAI(model=LLM_MODEL, base_url=LLM_URL)

#print(llm.invoke("What is the capital of France?"))