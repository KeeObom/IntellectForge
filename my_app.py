import os
from crewai import Agent, Task, Crew, Process
from langchain.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()
from langchain.llms import Ollama
ollama_llm = Ollama(model="openhermes")

# Get user input for the topic
topic = input("Enter the topic of interest: ")

researcher = Agent(
    role=f'{topic} Research Analyst',
    goal=f'Uncover cutting-edge developments in {topic}',
    backstory=f'You are an expert in {topic} research, skilled in identifying trends and analyzing complex data.'
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=ollama_llm
)

writer = Agent(
    role=f'{topic} Content Writer',
    goal=f'Translate complex {topic} findings into clear and engaging text',
    backstory=f'You have a passion for simplifying complex {topic} topics and making them accessible to a broader audience.'
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=ollama_llm
)

examiner = Agent(
    role=f'{topic} Assessment Specialist',
    goal=f'Create accurate and insightful test questions for {topic}',
    backstory=f'You have a background in educational assessment and specialize in crafting questions that evaluate understanding of {topic}.'
    verbose=True,
    allow_delegation=True,
    tools=[search_tool],
    llm=ollama_llm
)

student = Agent(
    role=f'{topic} Enthusiast',
    goal=f'Understand and grasp the intricacies of {topic} concepts',
    backstory=f'You are a dedicated learner, eager to explore the fascinating world of {topic}.'
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=ollama_llm
)