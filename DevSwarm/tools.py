import requests, urllib.parse
from typing import List, Dict
from .config import config

def get_todo_tickets() -> List[Dict]:
    # working JQL
    jql = 'project = KAN AND status = "To Do" ORDER BY priority DESC'

    encoded_jql = urllib.parse.quote(jql)

    # Jira endpoint
    url = (
        f"{config.jira_domain}/rest/api/3/search/jql"
        f"?jql={encoded_jql}"
        f"&maxResults=100"
        f"&fields=key,summary,status,assignee,priority"
    )

    resp = requests.get(
        url,
        auth=(config.jira_email, config.jira_token),
        headers={"Accept": "application/json"}
    )

    if resp.status_code != 200:
        print("Jira API error:", resp.status_code, resp.text)
        return []

    data = resp.json()
    issues = data.get("issues", [])
    tickets = []

    for issue in issues:
        fields = issue["fields"]

        tickets.append({
            "issue_key": issue["key"],
            "task": fields.get("summary", "No summary"),
            "assigned_to": (
                fields["assignee"]["displayName"]
                if fields.get("assignee")
                else "Unassigned"
            ),
            "status": fields["status"]["name"],
            "priority": (
                fields["priority"]["name"]
                if fields.get("priority")
                else "None"
            )
        })

    return tickets

def save_task_report(report: str, filename: str) -> dict:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    return {"status": "success"}

def analyze_codebase(directory: str) -> dict:
    """Return a summary of codebase."""
    import os, glob
    files = glob.glob(os.path.join(directory, "**"), recursive=True)
    codebase_context = ""
    for file in files:
        if os.path.isfile(file):
            codebase_context += f"\n- **{file}**:\n"
            try:
                with open(file, "r", encoding="utf-8") as f:
                    codebase_context += f.read()
            except UnicodeDecodeError:
                with open(file, "r", encoding="latin-1") as f:
                    codebase_context += f.read()
    return {"codebase_context": codebase_context}
