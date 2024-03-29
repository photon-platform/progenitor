import yaml
from pathlib import Path
from jinja2 import Environment, PackageLoader

from photon_platform.modulator import Modulator


def create_project(org_name, namespace, project_name, author, path):
    """Create a new Python project in an empty folder."""
    project_path = Path(path) / project_name

    if not project_path.exists():
        project_path.mkdir(parents=True)
    else:
        click.echo(f"Error: The path {project_path} already exists.")
        return

    copy_template_files(project_path, project_name, author, org_name, namespace)

    #  create_module(project_path, namespace, project_name)
    modulator = Modulator(project_path, namespace)
    modulator.create_module(project_name)
    #  click.echo(f"Python project '{project_name}' has been created at {project_path}")


def copy_template_files(project_path, project_name, author, org_name, namespace):
    env = Environment(
        loader=PackageLoader("photon_platform.progenitor"),
    )
    template_variables = {
        "project_name": project_name,
        "author": author,
        "org_name": org_name,
        "namespace": namespace,
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

    
