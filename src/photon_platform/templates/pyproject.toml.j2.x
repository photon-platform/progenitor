
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "{{project_name}}"
version = "0.0.1"
authors = [
  { name="phi ARCHITECT", email="github@phiarchitect.com" },
]
description = "create and manage log entries for a python project"
readme = "README.rst"
requires-python = ">=3.7"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "textual",
    "rich",
    "jinja2",
]

[project.scripts]
{{project_name}} = "{{project_name}}.app:run"

# [project.urls]
# "Homepage" = "https://github.com/{{org_name}}/{{project_name}}"
# "Bug Tracker" = "https://github.com/{{org_name}}/{{project_name}}/issues"
