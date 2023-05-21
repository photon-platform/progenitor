Progenitor - give life to Python projects
==========

Progenitor is a Python utility for creating new Python projects. It sets up a new project with everything ready for development, documentation, and publication.

Features
--------

- Creates a new Python project in an empty folder.
- Sets up a basic project structure with directories for source code, documentation, tests, and GitHub workflows.
- Copies template files into the project, including a license, README, and configuration files for various tools.

Installation
------------

You can install Progenitor using pip:

.. code-block:: bash

    pip install photon-platform-progenitor

Usage
-----

After installation, you can use the `progenitor` command to create a new project:

.. code-block:: bash

    progenitor --project_name my_project --author "My Name" --path /path/to/projects

This will create a new project named `my_project` in the `/path/to/projects` directory.

Dependencies
------------

Progenitor depends on the following Python packages:

- click
- textual
- rich
- jinja2

Contributing
------------

Contributions are welcome! Please see our [GitHub issues](https://github.com/photon-platform/progenitor/issues) for ways to contribute.

License
-------

Progenitor is licensed under the MIT License. See the `LICENSE` file for more details.

