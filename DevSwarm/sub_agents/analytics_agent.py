from google.adk.agents import Agent
from ..config import config
from ..agent_utils import suppress_output_callback

analytics_agent = Agent(
    name="analytics_agent",
    model=config.critic_model,
    description="""
    Generates analytics reports for the project.
    Input: task_assignments, developed_code, qa_report
    Output: project report summary
    """,
    output_key="analytics_report",
    after_agent_callback=suppress_output_callback
)
