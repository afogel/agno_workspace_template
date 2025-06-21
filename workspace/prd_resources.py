from os import getenv

from agno.docker.resource.image import DockerImage
from agno.docker.resources import DockerResources

from workspace.settings import ws_settings

#
# -*- Resources for the Production Environment
#
# Skip resource deletion when running `ag ws down` (set to True after initial deployment)
skip_delete: bool = False
# Save resource outputs to workspace/outputs
save_output: bool = True

# -*- Production image
prd_image = DockerImage(
    name=f"{ws_settings.image_repo}/{ws_settings.image_name}",
    tag=ws_settings.prd_env,
    enabled=ws_settings.build_images,
    path=str(ws_settings.ws_root),
    platforms=["linux/amd64", "linux/arm64"],
    # Push images after building
    push_image=ws_settings.push_images,
)

# -*- Build container environment
container_env = {
    "RUNTIME_ENV": "prd",
    # Get the OpenAI API key from the local environment
    "OPENAI_API_KEY": getenv("OPENAI_API_KEY"),
    # Enable monitoring
    "AGNO_MONITOR": "True",
    "AGNO_API_KEY": getenv("AGNO_API_KEY"),
    # Database configuration (use environment variables)
    "DB_HOST": getenv("DB_HOST"),
    "DB_PORT": getenv("DB_PORT", "5432"),
    "DB_USER": getenv("DB_USER"),
    "DB_PASS": getenv("DB_PASS"),
    "DB_DATABASE": getenv("DB_DATABASE"),
    # Migrate database on startup using alembic
    "MIGRATE_DB": getenv("MIGRATE_DB", "false"),
}

# -*- Production DockerResources (cloud-agnostic)
prd_docker_resources = DockerResources(
    env=ws_settings.prd_env,
    network=ws_settings.ws_name,
    resources=[prd_image],
)

# Note: For cloud deployment, use your preferred cloud provider's deployment tools
# or container orchestration platforms like Kubernetes, Docker Swarm, etc.
# The container environment variables above can be used with any deployment method.
