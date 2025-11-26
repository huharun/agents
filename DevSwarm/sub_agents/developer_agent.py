from google.adk.agents import Agent
from ..config import config
from ..agent_utils import suppress_output_callback
from ..tools import analyze_codebase

developer_agent = Agent(
    name="developer_agent",
    model=config.worker_model,
    description="""
    Implements code for assigned tasks and can suggest new features or improvements.
    Input: task_assignments, codebase context (optional)
    Output: 
      - code snippets or files with line-level suggested changes
      - inline feedback for improvements
      - conceptual feature ideas if requested
    """,
    output_key="developed_code",
    after_agent_callback=suppress_output_callback,
    tools=[analyze_codebase]  # provides context and line-level view for code review
)
