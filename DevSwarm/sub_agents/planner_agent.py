from google.adk.agents import Agent
from ..config import config
from ..agent_utils import suppress_output_callback
from ..tools import get_todo_tickets

planner_agent = Agent(
    name="planner_agent",
    model=config.worker_model,
    description="""
    Plans tasks based on Jira tickets without assigning them.
    Fetch tickets using get_todo_tickets() tool.
    Sort tasks by priority and optional time-to-finish.
    Output as a table or checklist for the developer.
    """,
    output_key="planned_tasks",
    after_agent_callback=suppress_output_callback,
    tools=[get_todo_tickets]
)
