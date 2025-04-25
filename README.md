# django-playground

## TODO

- Customize Django Admin (1:N relation etc.)
    - It's in Pt. 7 of the Tutorial: https://docs.djangoproject.com/en/5.1/intro/tutorial07/
    - https://realpython.com/customize-django-admin-python/
    - https://testdriven.io/blog/customize-django-admin/
- Setup a CUSTOM User Model
    - https://youtu.be/OIC4ounpQjA
    - Video Ref: https://docs.djangoproject.com/en/5.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
    - https://learndjango.com/tutorials/django-custom-user-model
- Consider *allauth* library

## Workpointer:

- https://docs.djangoproject.com/en/5.2/intro/tutorial02/

## The Exploration Log

Start Project

    django-admin startproject mysite .

Run Dev Server

    python manage.py runserver

Create App (must not be located in the project dir structure; it just have to be importable from Python-PATH)

    python manage.py startapp polls

VSCode: Create launch.json

- https://code.visualstudio.com/docs/python/debugging
- https://code.visualstudio.com/docs/debugtest/debugging-configuration

Init DB

    python manage.py migrate

Generate DB Migration for polls app

    python manage.py makemigrations polls

Look at migration SQL statements without execution

    python manage.py sqlmigrate polls 0001

Interactive Shell to wrangle DB data

    python manage.py shell

Create THE ADMIN in order to log into admin panel

    python manage.py createsuperuser