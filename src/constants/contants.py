# src/config.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Set the API key from the environment file
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Create and export your LLM instance
llm = ChatOpenAI(model="gpt-4o")
