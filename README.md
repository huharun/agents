# DevSwarm

## Overview

DevSwarm is a modular multi-agent system for software project management. It automates planning, development, testing, and analytics reporting, orchestrated through a root agent. Built on **Google Agent Development Kit (ADK)**, DevSwarm coordinates specialized sub-agents to streamline workflows and generate detailed reports.

---

## Architecture

**Root Agent:** `devswarm_root_agent`
Orchestrates the workflow and delegates tasks to sub-agents. Equipped with tools like `save_task_report`, `analyze_codebase`, and `get_todo_tickets`.
![DevSwarm Architecture](https://github.com/huharun/agents/blob/main/ui.png)


**Sub-Agents:**

* **Planner Agent:** `planner_agent` – Fetches Jira tickets, prioritizes tasks, and produces development checklists.
* **Developer Agent:** `developer_agent` – Implements code and provides feature suggestions. Can analyze codebase context.
* **Tester Agent:** `tester_agent` – Performs QA and generates test results.
* **Analytics Agent:** `analytics_agent` – Produces project reports based on tasks, code, and QA results.

**Utilities & Tools:**

* `agent_utils.py` – Helper functions like output suppression.
* `tools.py` – Functions for code analysis, Jira tickets fetching, and report saving.
* `config.py` – Configuration for models, Jira credentials, and iteration limits.
* `.env` – Environment variables.

---

## Workflow

1. **Fetch & Plan:** `planner_agent` fetches Jira "To Do" tickets, sorts by priority, and prepares a task plan.
2. **Develop:** `developer_agent` implements changes and new features, optionally analyzing the codebase.
3. **Test:** `tester_agent` runs QA tests to ensure correctness and stability.
4. **Report:** `analytics_agent` compiles:

   * Development Summary
   * QA & Testing Summary
   * Overall Project Report
5. **Save:** Reports are exported as Markdown files using `save_task_report`.

## Demo Video 

![DevSwarm Demo](input.gif)

(4.34 min)

Example: Fixing a medium-priority Jira ticket triggers all sub-agents to produce reports and save them automatically.

---

## Project Structure

```
DevSwarm/
├─ sub_agents/
│  ├─ planner_agent.py
│  ├─ developer_agent.py
│  ├─ tester_agent.py
│  ├─ analytics_agent.py
│  ├─ __init__.py
├─ agent.py
├─ agent_utils.py
├─ tools.py
├─requirements.txt
├─ config.py
├─ .env
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/huharun/agents
cd DevSwarm
```

2. Install dependencies (replace with your actual list):

```bash
pip install -r requirements.txt
```

---

## Running DevSwarm (ADK Web)

Start the system in ADK Web mode:

```bash
adk web
```

Workflow example in ADK Web:

* Root agent orchestrates `planner_agent`, `developer_agent`, `tester_agent`, `analytics_agent`.
* Jira tickets are fetched.
* Developer implements fixes.
* Tester validates code.
* Analytics agent generates reports and saves them automatically.

---

## Example Reports Generated

* `KAN-8_Development_Summary.md`
* `KAN-8_QA_Testing_Summary.md`
* `KAN-8_Overall_Project_Report.md`

---

## License

Apache-2.0
