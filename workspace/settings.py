from pathlib import Path

from agno.workspace.settings import WorkspaceSettings

#
# We define workspace settings using a WorkspaceSettings object
# these values can also be set using environment variables
# Import them into your project using `from workspace.settings import ws_settings`
#
ws_settings = WorkspaceSettings(
    # Workspace name
    ws_name="agent-app",
    # Path to the workspace root
    ws_root=Path(__file__).parent.parent.resolve(),
    # -*- Workspace Environments
    dev_env="dev",
    prd_env="prd",
    # default env for `agno ws` commands
    default_env="dev",
    # -*- Image Settings
    # Repository for images
    image_repo="agnohq",
    # 'Name:tag' for the image
    image_name="agent-app",
    # Build images locally
    build_images=False,
    # Push images to the registry
    push_images=False,
    # Skip cache when building images
    skip_image_cache=False,
    # Force pull images
    force_pull_images=False,
)
