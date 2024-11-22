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
