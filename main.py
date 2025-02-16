import os, sys
from src.exception import BlogException
from src.logger import logging
from src.components.agents import simple_llm



try:
    simple_llm()
except Exception as e:
    raise BlogException(e, sys)
