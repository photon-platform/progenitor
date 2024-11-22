## src/photon_platform/progenitor/__init__.py

```py
"""
progenitor
==========

PHOTON platform
---------------

tools for creating and initializing Python projects

"""

from photon_platform.progenitor.progenitor import create_project

__author__ = "phiarchitect"
__maintainer__ = "PHOTON platform"
__email__ = "github@phiarchitect.com"
__version__ = "0.0.1"
__licence__ = "MIT"

```

## src/photon_platform/progenitor/__main__.py

```py
"""The package entry point into the application."""

from pathlib import Path
from photon_platform.progenitor import create_project
from photon_platform.formulator import load_blueprint, Formulator

#  import pkg_resources


def run():
    """Create a new Python project in an empty folder."""
    script_dir = Path(__file__).parent.absolute()
    blueprint_file = script_dir / "blueprint.yaml"
    blueprint = load_blueprint(blueprint_file)
    #  print(blueprint)

    form = Formulator(blueprint)
    reply = form.run()
    print(reply)

    #  create_project(org_name, namespace, project_name, author, path )
    create_project(**reply, path=".")


if __name__ == "__main__":
    run()

```

## src/photon_platform/progenitor/app.py

```py
import click
from trogon import tui
from .progenitor import create_project
from photon_platform.formulator import load_blueprint, Formulator

import pkg_resources


@tui()
@click.option(
    "--org_name",
    prompt="Name of the github acct/org",
    help="Name of the github acct/org",
)
@click.option(
    "--namespace", prompt="Name of the namespace", help="Name of the namespace"
)
@click.option(
    "--project_name", prompt="Name of the project", help="Name of the project"
)
@click.option("--author", prompt="Author of the project", help="Author of the project")
@click.option(
    "--path", prompt="Path to the project folder", help="Path to the project folder"
)
@click.command()
def run(org_name, namespace, project_name, author, path):
    """Create a new Python project in an empty folder."""
    create_project(org_name, namespace, project_name, author, path)


if __name__ == "__main__":
    run()

```

## src/photon_platform/progenitor/folders.py

```py
import os
from pathlib import Path


def get_base_project_folder() -> Path:
    """
    Retrieve the base project folder from an environment variable or default to '~/PROJECTS'.

    Returns:
    - Path: A pathlib.Path object representing the base project folder.
    """
    base_folder_path = os.environ.get("PHOTON_PROJECTS_BASE", "~/PROJECTS")
    base_folder_path = Path(base_folder_path).expanduser()

    if not base_folder_path.exists():
        print(f"The directory {base_folder_path} does not exist. Creating it now.")
        base_folder_path.mkdir(parents=True)

    return base_folder_path


def list_organization_folders(base_folder_path: str) -> list[str]:
    """
    List the GitHub organization folders present in the base project folder.

    Parameters:
    - base_folder_path (Path): A pathlib.Path object representing the base project folder.

    Returns:
    - list[str]: A list of folder names representing GitHub organizations.
    """
    return [f.name for f in base_folder_path.iterdir() if f.is_dir()]


if __name__ == "__main__":
    base_folder = get_base_project_folder()
    org_folders = list_organization_folders(base_folder)

    print(f"{base_folder=}")
    print(f"{org_folders=}")

```

## src/photon_platform/progenitor/progenitor.py

```py
import yaml
from pathlib import Path
from jinja2 import Environment, PackageLoader

from photon_platform.modulator import Modulator


def create_project(
    github_id,
    package_namespace,
    github_repo_id,
    package_name,
    author,
    description,
    path,
):
    """Create a new Python project in an empty folder."""
    project_path = Path(path) / package_name

    if not project_path.exists():
        project_path.mkdir(parents=True)
    else:
        print(f"Error: The path {project_path} already exists.")
        return

    # create module stubs
    modulator = Modulator(project_path, package_namespace)
    modulator.create_module(package_name)

    # generate templates
    env = Environment(
        loader=PackageLoader("photon_platform.progenitor"),
    )
    template_variables = {
        "author": author,
        "github_id": github_id,
        "github_repo_id": github_repo_id,
        "package_namespace": package_namespace,
        "package_name": package_name,
        "description": description,
    }

    script_dir = Path(__file__).parent.absolute()
    yaml_file_path = script_dir / "templates.yaml"

    with open(yaml_file_path, "r") as f:
        file_structure = yaml.safe_load(f)

    for file_info in file_structure:
        target = project_path / file_info["target"]
        target.parent.mkdir(
            parents=True, exist_ok=True
        )  # create directory if it doesn't exist
        template = env.get_template(file_info["template"])
        target.write_text(template.render(template_variables))

```

