from langchain_core.messages import HumanMessage, SystemMessage
from src.utils.blog_tools import title_creator, content_writer,recommendation_agent
from src.constants.contants import llm

tools = [title_creator, content_writer,recommendation_agent]

# Bind the tools to the LLM
llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=False)


# System message for context
sys_msg = SystemMessage(content="You are a helpful assistant for writing comprhensive blogs.")

def assistant(state):
    # state should be a dictionary with "messages" as a list of messages
    return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}
