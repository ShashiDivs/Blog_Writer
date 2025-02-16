from src.exception import BlogException
from src.logger import logging
import os, sys
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")


def simple_llm():
    try:
        llm=ChatOpenAI(model="o1-mini")
        result = llm.invoke("What is generative AI")
        return result.content
    except Exception as e:
        raise BlogException(e, sys)