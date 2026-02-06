from crewai import Agent, Crew, Task

trend_agent = Agent(
    role="Trend Researcher",
    goal="Identify trending topics",
    backstory="Expert social trend analyst"
)

content_agent = Agent(
    role="Content Creator",
    goal="Generate viral content",
    backstory="Creative influencer AI"
)

task1 = Task(
    description="Find trending topics in AI and lifestyle",
    agent=trend_agent
)

task2 = Task(
    description="Create an engaging post using trends",
    agent=content_agent
)

crew = Crew(
    agents=[trend_agent, content_agent],
    tasks=[task1, task2]
)

crew.kickoff()
