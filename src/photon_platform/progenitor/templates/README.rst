{{ project_name }}
{{ '=' * project_name|length }}
{{ description }}

Features
--------

{# insert #}

Installation
------------

You can install **{{ project_name }}** using pip:

.. code-block:: bash

   pip install {{org_name}}-{{project_name}}

Usage
-----

After installation, you can use the `{{project_name}}` command to create a new project:

.. code-block:: bash

   {{project_name}} 


Dependencies
------------

Progenitor depends on the following Python packages:

{# read from pyproject.toml #}

Contributing
------------

Contributions are welcome! Please see our [GitHub issues](https://github.com/{{org_name}}/{{project_name}}/issues) for ways to contribute.

License
-------

**{{project_name}}** is licensed under the MIT License. See the `LICENSE` file for more details.

