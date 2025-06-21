## Agent App

This repo contains the code for a production-grade agentic system built with:

1. A Streamlit UI
2. A FastAPI server
3. A Postgres database with the PgVector extension.

You can run the agent app in 2 environments:

1. A local development environment using Overmind (recommended)
2. A development environment running locally on docker

## Setup

1. [Install uv](https://docs.astral.sh/uv/#getting-started) for managing the python environment.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create a virtual environment and install dependencies:

```sh
./scripts/dev_setup.sh
```

3. Activate virtual environment

```
source .venv/bin/activate
```

## Run application locally using Overmind (Recommended)

This method runs all services directly on your local machine without Docker.

### Prerequisites

1. Install PostgreSQL via Homebrew:
```bash
brew install postgresql
brew services start postgresql
```

2. Install Overmind:
```bash
brew install overmind
```

3. Create and configure environment variables:
```bash
cp .env.example .env
# Edit .env file with your API keys and configuration
```

4. Set up the database:
```bash
# Create database
createdb opt_out_dev
```

5. Run database migrations:
```bash
uv run alembic -c db/alembic.ini upgrade head
```

### Start the application

```bash
overmind start
```

This will start:
- FastAPI server on [localhost:8000](http://localhost:8000/docs)
- Streamlit UI on [localhost:8501](http://localhost:8501)

### Stop the application

```bash
overmind stop
```

Or press `Ctrl+C` in the terminal running Overmind.

## Run application locally using docker

1. Install [docker desktop](https://www.docker.com/products/docker-desktop)

2. Export API keys

Required: Set the `OPENAI_API_KEY` environment variable using

```sh
export OPENAI_API_KEY=***
```

> You may use any supported model provider, just need to update the respective Agent, Team or Workflow.

3. Start the workspace:

```sh
ag ws up
```

- This will run 3 containers:
  - Streamlit on [localhost:8501](http://localhost:8501)
  - FastAPI on [localhost:8000](http://localhost:8000/docs)
  - Postgres on  [localhost:5432](http://localhost:5432)
- Open [localhost:8501](http://localhost:8501) to view the Streamlit App.
- Open [localhost:8000/docs](http://localhost:8000/docs) to view the FastAPI docs.

4. Stop the workspace using:

```sh
ag ws down
```

## More Information

Learn more about this application and how to customize it in the [Agno Workspaces](https://docs.agno.com/workspaces) documentaion
