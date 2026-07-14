from typing import List

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq as chat_groq
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field

load_dotenv()


class Source(BaseModel):
    """Schema for a source used by the agent."""

    url: str = Field(description="The URL of the source.")


class AgentResponse(BaseModel):
    """Schema for the agent's response with answer and sources."""

    answer: str = Field(description="The answer provided by the agent.")
    sources: List[Source] = Field(description="A list of sources used by the agent.")


llm = chat_groq(model="llama-3.3-70b-versatile", temperature=0.0)

tools = [TavilySearch()]

agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details"
                )
            ]
        }
    )
    print(result)


if __name__ == "__main__":
    main()
