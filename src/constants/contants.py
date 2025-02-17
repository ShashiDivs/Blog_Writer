# src/config.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

load_dotenv()

# Set the API key from the environment file
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
#os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


# Create and export your LLM instance
llm = ChatOpenAI(model="gpt-4o")
#llm= ChatGroq(model="gemma2.9b-it")
