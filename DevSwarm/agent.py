from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from .config import config
from .tools import save_task_report, analyze_codebase, get_todo_tickets
from .sub_agents import planner_agent, developer_agent, tester_agent, analytics_agent

root_agent = Agent(
    name="devswarm_root_agent",
    model=config.worker_model,
    description="""Root DevSwarm Agent. Orchestrates the software project...""",
    sub_agents=[planner_agent, developer_agent, tester_agent, analytics_agent],
    tools=[
        FunctionTool(save_task_report),
        FunctionTool(analyze_codebase),
        FunctionTool(get_todo_tickets)
    ],
    output_key="project_status"
)
