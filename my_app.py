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



# Create tasks for your agents
task1 = Task(
    description=f"""Research and analyze recent developments in {topic}. 
    Identify key trends, new technologies, and their potential impact. 
    Provide a comprehensive report.""",
    agent=researcher
)

task2 = Task(
    description=f"""Write a detailed blog post about noteworthy advancements in {topic}. 
    Ensure it's engaging, easy to understand, and suitable for tech enthusiasts. 
    Aim for at least 4 paragraphs.""",
    agent=writer
)

task3 = Task(
    description=f"""Develop 2-3 test questions related to {topic}. 
    Include correct answers and explanations. 
    Ensure the questions assess a student's understanding of the subject.""",
    agent=examiner
)

task4 = Task(
    description=f"""Study the provided materials on {topic}. 
    Summarize the key concepts and submit questions you have about the topic.""",
    agent=student
)


# Instantiate your crew with a sequential process
crew = Crew(
    agents=[researcher, writer, examiner, student],
    tasks=[task1, task2, task3, task4],
    verbose=True
)

# Crew work
result = crew.kickoff()

print("######################")
print(result)

