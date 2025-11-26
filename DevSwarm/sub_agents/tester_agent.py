from google.adk.agents import Agent
from ..config import config
from ..agent_utils import suppress_output_callback

tester_agent = Agent(
    name="tester_agent",
    model=config.critic_model,
    description="""
    Performs QA on the developed code.
    Input: developed_code
    Output: test results and bug reports
    """,
    output_key="qa_report",
    after_agent_callback=suppress_output_callback
)
