# Django - Learning Notes

Django’s workflow:

1. An HTTP request comes in for a particular URL.
2. Django uses some rules to decide which view function should deal with the request (this is referred to as resolving the URL).
3. The view function processes the request and user input, and returns an HTTP response.

Django uses request and response objects to pass state through the system:

* When a page is requested, Django creates an HttpRequest object that contains metadata about the request.
* Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function.
* Each view is responsible for returning an HttpResponse object.

## Installing Django

Prerequisites:

* python3

Installation:

* Linux: `sudo pip3 install django`
* Windows: `pip install django`

## Managing projects

Create a new project: `django-admin.py startproject <project name> .`

Project file structure:

* settings.py - contains the settings of the project.
  * List of registered apps for the project.
  * Specifications for the used database(s) in the project.
  * URL prefix to specify which URLs should be treated as requests for static files; it is `/static/` by default.
* urls.py - contains mapping from URLs to view functions for the whole site.

## Apps

Structuring code into apps is a good practice with Django. One project can have many apps: reused apps or 3rd-party apps developed by others.

Adding a new app:

* start a new app: `python manage.py startapp <app name>`, in the folder of the project
* register the app with the project: edit `settings.py` of the project and add `<app name>` into the `INSTALLED_APPS` variable.

File and folder structure of the app:

* migrations/ - contains the database migrations files.
* static/ - contains the static files, such as CSS files.
* templates/ - contains the templates for rendering. Not initially created, but Django searches this directory for templates by default.
* models.py - contains the models that map to data stored in a database.
* tests.py - contains the unit tests for the app.
* urls.py - contains mapping from URLs to view functions for the app, to make it more contained. It needs to be included in the project's urls.py.
* views.py - contains the views, which are functions that render templates, called when resolving URLs. A view function processes user input and returns an appropriate response.
