import agent
import os
from agent import Agent
from dotenv import load_dotenv

# Load default environment variables (.env)
load_dotenv()

AGENT_NAME = os.getenv("AGENT_NAME", "my-agent")

agent = Agent(AGENT_NAME)

# Creates Pinecone Index
agent.createIndex()

print("Talk to the AI!")

while True:
    userInput = input()
    if userInput:
        if (userInput.startswith("read:")):
            agent.read(" ".join(userInput.split(" ")[1:]))
            print("Understood! The information is stored in my memory.")
        elif (userInput.startswith("think:")):
            agent.think(" ".join(userInput.split(" ")[1:]))
            print("Understood! I stored that thought into my memory.")
        elif (userInput.startswith("readDoc:")):
            agent.readDoc(" ".join(userInput.split(" ")[1:]))
            print("Understood! I stored the document into my memory.")
        else:
            print(agent.action(userInput), "\n")
    else:
        print("SYSTEM - Give a valid input")
