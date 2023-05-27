import click
from .progenitor import create_project
from photon_platform.formulator import load_blueprint, Formulator

import pkg_resources


@click.command()
@click.option(
    "--project_name", prompt="Name of the project", help="Name of the project"
)
@click.option("--author", prompt="Author of the project", help="Author of the project")
@click.option(
    "--path", prompt="Path to the project folder", help="Path to the project folder"
)
def run(project_name, author, path):
    """Create a new Python project in an empty folder."""
    blueprint_path = pkg_resources.resource_filename(
        "photon_platform.progenitor", "blueprint.yaml"
    )
    blueprint = load_blueprint(blueprint_path)

    org_name = "photon-platform"
    namespace = "photon_platform"
    create_project(project_name, author, path, org_name, namespace)


if __name__ == "__main__":
    run()
