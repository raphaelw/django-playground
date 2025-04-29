# django-playground

Documenting my first steps learning Python Django

## TODO

- Customize Django Admin (1:N relation etc.)
    - It's in Pt. 7 of the Tutorial: https://docs.djangoproject.com/en/5.1/intro/tutorial07/
    - https://realpython.com/customize-django-admin-python/
    - https://testdriven.io/blog/customize-django-admin/
- Auth incl. Setup a CUSTOM User Model
    - https://youtu.be/OIC4ounpQjA
    - Video Ref: https://docs.djangoproject.com/en/5.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
    - Full Tutorial by Piko: https://youtu.be/aCWd4loTl68
    - https://learndjango.com/tutorials/django-custom-user-model
- Consider *allauth* library
- CSRF Tokens & Forms in general
- Template Language, HTMX, Unpoly

## Workpointer:

- https://docs.djangoproject.com/en/5.2/intro/tutorial03/#write-views-that-actually-do-something

## The Exploration Log

### Start Project

    django-admin startproject mysite .

### Run Dev Server

    python manage.py runserver

### Create App

(must not be located in the project dir structure; it just have to be importable from Python-PATH)

    python manage.py startapp polls

### VSCode: Create launch.json

- https://code.visualstudio.com/docs/python/debugging
- https://code.visualstudio.com/docs/debugtest/debugging-configuration

### Init DB

    python manage.py migrate

### Generate DB Migration for polls app

    python manage.py makemigrations polls

### Look at migration SQL statements without execution

    python manage.py sqlmigrate polls 0001

### Interactive Shell to wrangle DB data

    python manage.py shell

### Create THE ADMIN in order to log into admin panel

    python manage.py createsuperuser

### URL patterns / Routing / Path

```py
urlpatterns = [
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
]
```

The `int` part is called *Path Converter*. There is also: `str` (default), `slug`, `uuid` and `path`.

More Info: https://docs.djangoproject.com/en/5.2/topics/http/urls/#path-converters

### Standalone Scripts making use of Django ORM incl. project settings etc.

https://stackoverflow.com/questions/39723310/django-standalone-script

- **Approach 1:**
    - https://www.stavros.io/posts/standalone-django-scripts-definitive-guide/
    - equivalent to importing `wsgi`. see also `misc\standalone_script.py`
        - in bash: `PYTHONPATH=. python misc/standalone_script.py`
        - alternative hack: `python -m misc.stanalone_script`
    - you could also move `standalone_script.py` to the same path as `management.py`. this would automatically solve the PYTHONPATH workarounds from above.
- **Approach 2:** (more official and clean)
    - Custom Management Command: https://docs.djangoproject.com/en/5.2/howto/custom-management-commands/

### Pylint django to get rid of false positive errors

- https://stackoverflow.com/a/47343542
- https://sqlpey.com/python/solved-how-to-resolve-class-having-no-objects-member-in-django/