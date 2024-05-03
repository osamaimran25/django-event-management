```markdown
# Event Management

Welcome to the Event Management project!

## Setup

First, create a virtual environment:

```bash
virtualenv env
```

Activate the virtual environment:

```bash
source env/bin/activate
```

Install all dependencies:

```bash
pip install -r requirements/local.txt
```

Alternatively, you can run the project with Docker.

### Docker Setup

To build the Docker image locally:

```bash
docker-compose -f local.yml build
```

To run the Docker container in detached mode:

```bash
docker-compose -f local.yml up -d
```

## About

This project is built with the help of Cookiecutter Django, making development faster and easier. 

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, simply sign up and verify your email address.
- To create a **superuser account**, use:

```bash
python manage.py createsuperuser
```

### Testing

Run type checks with mypy:

```bash
mypy event_management
```

Run tests and check coverage:

```bash
coverage run -m pytest
coverage html
open htmlcov/index.html
```

Run tests with pytest:

```bash
pytest
```

### Live Reloading and Sass CSS Compilation

Details available [here](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

For deployment, refer to the [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

## License

This project is licensed under the MIT License.
```
I reformatted the README, organizing the content into sections for clarity and added markdown code blocks for commands and code snippets. Let me know if you need further adjustments!