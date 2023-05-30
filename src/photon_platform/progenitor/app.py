import click
from trogon import tui
from .progenitor import create_project
from photon_platform.formulator import load_blueprint, Formulator

import pkg_resources


@tui()
@click.option(
    "--org_name", prompt="Name of the github acct/org", help="Name of the github acct/org"
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
<<<<<<< HEAD
    #  org_name = "photon-platform"
    #  namespace = "photon_platform"
    create_project(org_name, namespace, project_name, author, path )
=======
    blueprint_path = pkg_resources.resource_filename(
        "photon_platform.progenitor", "blueprint.yaml"
    )
    blueprint = load_blueprint(blueprint_path)

    org_name = "photon-platform"
    namespace = "photon_platform"
    create_project(project_name, author, path, org_name, namespace)
>>>>>>> e30ae3929923502be6065e5d99e3c868cd0761f5


if __name__ == "__main__":
    run()
