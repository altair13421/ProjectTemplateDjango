# ProjectTemplate (Django)

## Description

This is a basic Django project template. Why I made this? Simple, I don't Want to Do the same thing over and over again. I want to create a project with a few clicks. This template is a starting point for any Django project. It includes a basic project structure, a few useful settings, and some example views and templates. You can use this template to create a new project and then customize it as needed.

## Requirements: Python 3.8+

## Installation

```sh
# create Environment
python -m venv env
# activate Environment
source ./env/bin/activate # Linux
.\env\Scripts\activate # Windows
# install requirements
pip install -r requirements.txt

# changing directories
cd ProjectTemplate

# Migrating, and All
python manage.py makemigrations
python manage.py migrate

# Running Server
python manage.py runserver
```

## Usage

You can use these for Various tasks that Require a Problem to Set up

### What does it Contain?

- Initial Setup of RestFramework, Swagger, DebugToolbar, DjangoExtensions
- Abstract Models for basic Use
- API Blueprints (RestFramework) For Models
- View Blueprints For Normal Django Views, (CreateView, DeleteView, UpdateView, ListView, RetrieveView)
