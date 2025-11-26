import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class DevConfig:
    worker_model: str = "gemini-2.5-flash"
    critic_model: str = "gemini-2.5-pro"
    max_iterations: int = 5
    jira_domain: str = os.getenv("JIRA_DOMAIN")
    jira_email: str = os.getenv("JIRA_EMAIL")
    jira_token: str = os.getenv("JIRA_API_TOKEN")

config = DevConfig()
