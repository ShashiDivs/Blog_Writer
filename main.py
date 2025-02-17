# src/main.py
from langchain_core.messages import HumanMessage
from src.components.agents import get_reactive_graph

def main():
    # Get user input for the blog topic (or title, depending on your flow)
    user_input = input("Enter the blog topic: ")

    # For example, you might want to use the title_creator separately, or pass it as input.
    # Here, we simply pass the user input as the content of the HumanMessage.
    messages = [HumanMessage(content=user_input)]
    
    # Build the reactive graph
    react_graph = get_reactive_graph()
    
    # Invoke the graph
    state = react_graph.invoke({"messages": messages})
    
    # Print the resulting messages
    for m in state['messages']:
        m.pretty_print()


if __name__ == "__main__":
    main()
