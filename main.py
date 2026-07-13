
from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI




def search(query: str) -> str:
    """
    Tool that searches over internet 
    Args:
        query: The query to search for
    Returns:
    The search results
    """
    print(f"Searching for: {query}")
    return "Tokkyo weather is sunny"

llm = ChatOpenAI()
tools = [search]
agent = create_agent(model=llm, tools=tools)
def main():
    print("Hello from search-engine-ai-agent!")
    result = agent.invoke({"message": HumanMessage(content="What is the weather in Tokyo?")})
    print(result)
    print("Goodbye from search-engine-ai-agent!")


if __name__ == "__main__":
    main()
