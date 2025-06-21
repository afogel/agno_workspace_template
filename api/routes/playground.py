from os import getenv

from agno.playground import Playground

from agents.sage import get_sage
from agents.scholar import get_scholar
from teams.finance_researcher import get_finance_researcher_team
from teams.multi_language import get_multi_language_team

######################################################
## Router for the Playground Interface
######################################################

sage_agent = get_sage(debug_mode=True)
scholar_agent = get_scholar(debug_mode=True)
finance_researcher_team = get_finance_researcher_team(debug_mode=True)
multi_language_team = get_multi_language_team(debug_mode=True)

# Create a playground instance
playground = Playground(agents=[sage_agent, scholar_agent], teams=[finance_researcher_team, multi_language_team])

# Register the playground with agno.com in development mode
if getenv("RUNTIME_ENV") == "dev":
    api_port = getenv("API_PORT", "8000")
    playground_url = f"http://localhost:{api_port}"
    print(f"🎮 Playground will be available at: {playground_url}")
    # The playground routes are automatically registered via playground_router

playground_router = playground.get_async_router()
