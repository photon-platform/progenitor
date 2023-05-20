import click
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


@click.command()
@click.option(
    "--project_name", prompt="Name of the project", help="Name of the project"
)
@click.option("--author", prompt="Author of the project", help="Author of the project")
@click.option(
    "--path", prompt="Path to the project folder", help="Path to the project folder"
)
def main(project_name, author, path):
    """Create a new Python project in an empty folder."""
    project_path = Path(path) / project_name

    if not project_path.exists():
        project_path.mkdir(parents=True)
    else:
        click.echo(f"Error: The path {project_path} already exists.")
        return

    create_project_structure(project_path)
    copy_template_files(project_path, project_name, author)

    click.echo(f"Python project '{project_name}' has been created at {project_path}")


def create_project_structure(project_path):
    (project_path / "src").mkdir(parents=True)
    (project_path / "docsrc").mkdir(parents=True)
    (project_path / "docsrc" / "modules").mkdir(parents=True)
    (project_path / "docsrc" / "log").mkdir(parents=True)
    (project_path / "tests").mkdir(parents=True)
    (project_path / ".github" / "workflows").mkdir(parents=True)


def copy_template_files(project_path, project_name, author):
    env = Environment(loader=FileSystemLoader("templates"))
    template_variables = {"project_name": project_name, "author": author}

    # Render and create LICENSE file
    template = env.get_template("LICENSE.j2")
    (project_path / "LICENSE").write_text(template.render(template_variables))

    # Render and create pyproject.toml file
    template = env.get_template("pyproject.toml.j2")
    (project_path / "pyproject.toml").write_text(template.render(template_variables))

    # Render and create index.rst file
    template = env.get_template("index.rst.j2")
    (project_path / "docsrc" / "index.rst").write_text(
        template.render(template_variables)
    )

    # Render and create action.yml file
    template = env.get_template("action.yml.j2")
    (project_path / ".github" / "workflows" / "action.yml").write_text(
        template.render(template_variables)
    )


if __name__ == "__main__":
    main()
