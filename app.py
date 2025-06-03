import os
import asyncio
from dotenv import load_dotenv # Add this import
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.models.google import GoogleModel

load_dotenv() # Call this at the beginning of your script

# Use model based on environment variable
model_type = os.getenv("AI_MODEL", "openai").lower()

if model_type == "claude":
    model = AnthropicModel(model_name="claude-3-opus-20240229")
elif model_type == "gemini":
    model = GoogleModel(model_name="gemini-1.5-flash")
elif model_type == "deepseek":
    model = OpenAIModel(
        model_name="deepseek-chat",
        base_url="https://api.deepseek.com/v1"
    )
else:
    model = OpenAIModel(model_name="gpt-4o-mini")

# Define the MCP Servers
brave_server = MCPServerStdio(
    'python',
    ['brave_search.py']
)

python_tools_server = MCPServerStdio(
    'python',
    ['python_tools.py']
)

tool_recommendation_server = MCPServerStdio(
    'python',
    ['tool_recommendation/mcp_server.py']
)

# Define the Agent with all MCP servers
agent = Agent(
    model, 
    mcp_servers=[brave_server, python_tools_server, tool_recommendation_server],
    retries=3,
    system_prompt="""You are an intelligent tool recommendation assistant specializing in:

**TOOL RECOMMENDATION & DISCOVERY**
Your primary purpose is to help developers, engineers, and technical professionals discover, analyze, and implement the best tools for their projects and workflows.

CORE CAPABILITIES:
- Search for tools using live web data via Brave API
- Analyze tool quality, reliability, and suitability using AI
- Provide comprehensive installation guides for recommended tools
- Compare multiple tools side-by-side with detailed analysis
- Recommend complete tool workflows for specific tasks and projects
- Support all development categories: web, mobile, desktop, database, devops, testing, design, data science, AI/ML, game development, security, productivity

RECOMMENDATION APPROACH:
When users ask about tools, provide comprehensive recommendations with:
- Relevance scoring and detailed reasoning
- Installation complexity assessment (Easy/Medium/Hard)
- Community support and documentation evaluation
- Cost considerations (free vs paid options)
- Performance and scalability analysis
- Integration capabilities with other tools
- Learning curve assessment based on user skill level

INTERACTION STYLE:
- Always ask clarifying questions about project requirements, skill level, and constraints
- Provide actionable, practical recommendations
- Include installation guides and getting-started tips
- Suggest tool combinations and workflows when relevant
- Consider budget constraints and open-source alternatives

Your goal is to accelerate development productivity by connecting users with the perfect tools for their specific needs."""
)

# Main async function
async def main():
    async with agent.run_mcp_servers():
        print("🔧 Tool Recommendation Assistant Ready! Type 'exit' to quit.\n")
        print("I can help you find the best tools for any development project!")
        print("Try asking me about:")
        print("- 'I need tools for web development'")
        print("- 'Compare React vs Vue.js'")
        print("- 'How do I set up Docker on Ubuntu?'")
        print("- 'What are the best tools for data analysis?'\n")
        
        conversation = []
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                break
            
            conversation.append({"role": "user", "content": user_input})
            
            # Build context from recent conversation
            context = "Recent conversation:\n"
            context += "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation[-6:]])
            
            result = await agent.run(f"{context}\n\nCurrent message: {user_input}")
            print(f"\nAssistant: {result.output}\n")
            
            conversation.append({"role": "assistant", "content": result.output})
            
            conversation.append({"role": "assistant", "content": result.output})

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())