# src/graph_builder.py
from langgraph.graph import START, StateGraph, END
from langgraph.prebuilt import tools_condition, ToolNode
from src.components.assistant import assistant, tools
from langgraph.graph import MessagesState
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage
from typing import Annotated
from langgraph.graph.message import add_messages

# Define your state type for the graph
class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]

# Create the state graph
builder = StateGraph(MessagesState)

# Define nodes
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))


# Define edges
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")
builder.add_edge("assistant", END)


# Compile the graph
react_graph = builder.compile()

def get_reactive_graph():
    return react_graph
