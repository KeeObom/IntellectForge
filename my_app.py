import os
from crewai import Agent, Task, Crew, Process
from langchain.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()
from langchain.llms import Ollama
ollama_llm = Ollama(model="openhermes")

# Get user input for the topic
topic = input("Enter the topic of interest: ")

researcher = Agent(
    role=f'{topic} Researcher',
    goal=f'Develop ideas for teaching someone new to {topic}.',
    backstory=f'You are an expert in {topic}, skilled in simplifying complex concepts.',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=ollama_llm
)

writer = Agent(
    role=f'{topic} Writer',
    goal=f"Use the Researcher's ideas to write a piece of text to explain {topic}.",
    backstory=f'You have a passion for translating complex {topic} ideas into clear and engaging text.',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=ollama_llm
)

examiner = Agent(
    role=f'{topic} Examiner',
    goal=f'Craft 2 test questions to evaluate understanding of the created text about {topic}, along with the correct answers.',
    backstory=f'You have a background in educational assessment and specialize in crafting questions.',
    verbose=True,
    allow_delegation=True,
    tools=[search_tool],
    llm=ollama_llm
)

student = Agent(
    role=f'{topic} Student',
    goal=f'Provide answers to the 2 questions set by the examiner about {topic}.',
    backstory=f'You are a dedicated learner, eager to demonstrate your understanding.',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=ollama_llm
)



# Task for each agent
task1 = Task(
    description=f"""Develop ideas for teaching someone new to the subject.""",
    agent=researcher
)

task2 = Task(
    description=f"""Write a piece of text to explain the topic.""",
    agent=writer
)

task3 = Task(
    description=f"""Craft 2 test questions to evaluate understanding of the created text, along with the correct answers.""",
    agent=examiner
)

task4 = Task(
    description=f"""Provide answers to the 2 questions set by the examiner.""",
    agent=student
)


# Sequential process for the crew
crew = Crew(
    agents=[researcher, writer, examiner, student],
    tasks=[task1, task2, task3, task4],
    verbose=True
)

# Go to work
result = crew.kickoff()

print("######################")
print(result)

