# TDD with Django, Selenium, and Javascript

Literature: Harry J.W. Percival, "Test-Driven Development with Python. Obey the Testing Goat: Using Django, Selenium, and Javascript", O'Reilly, 2014, Online version https://www.obeythetestinggoat.com/pages/book.html.

## Requirements
* Web browser (Firefox)
* Git
* Python3
* Pip3
* Python modules:
   * Django ```sudo pip3 install django```
   * Selenium ```sudo pip3 install --upgrade selenium``` (need to be kept up to date)
       * [Selenium drivers](https://github.com/SeleniumHQ/selenium/blob/master/py/docs/source/index.rst) for browsers
* [Bootstrap](http://getbootstrap.com/)


## Learning Notes

### Django
Django’s workflow:
1. An HTTP request comes in for a particular URL.
2. Django uses some rules to decide which view function should deal with the request (this is referred to as resolving the URL).
3. The view function processes the request and user input, and returns an HTTP response.

Django uses request and response objects to pass state through the system.
* When a page is requested, Django creates an HttpRequest object that contains metadata about the request.
* Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function.
* Each view is responsible for returning an HttpResponse object.

#### Projects
Creating a new project:
```
$ django-admin.py startproject <project name> .
```
File structure:
* settings.py - contains the settings of the project.
    * List of registered apps for the project.
    * Specifications for the used database(s) in the project.
    * URL prefix to specify which URLs should be treated as requests for static files; it is `/static/` by default.
* urls.py - contains mapping from URLs to view functions for the whole site. 

#### manage.py
* `manage.py` is Django’s Swiss Army knife.
Can be used to:
* Run a development server: ```$ python manage.py runserver```
* Invoke test runner: ```$ python manage.py test [appName or PythonPackageDirWithTests]```
* Build a database migration: ```$ python manage.py makemigrations```
* Execute a database migration: ```$ python manage.py migrate```
    * Recreate a fresh and empty database: ```$ python manage.py migrate --noinput```
* Gather all static files from various app folders: ```$ python manage.py collectstatic```
    * The destination folder is defined in settings.py as STATIC_ROOT.

#### Apps
* Structuring code into apps is a good practice with Django.
* One project can have many apps: reused apps or 3rd-party apps developed by others.

Starting an app:
```
$ python manage.py startapp <app name>
```

Registering the app with the project:
* in the project's `settings.py`, add `<app name>` into the `INSTALLED_APPS` variable.

File and folder structure:
* migrations/ - contains the database migrations files.
* static/ - contains the static files, such as CSS files.
* templates/ - contains the templates for rendering. Not initially created, but Django searches this directory for templates by default.
* models.py - contains the models that map to data stored in a database.
* tests.py - contains the unit tests for the app.
* urls.py - contains mapping from URLs to view functions for the app, to make it more contained. It needs to be included in the project's urls.py.
* views.py - contains the views, which are functions that render templates, called when resolving URLs. A view function processes user input and returns an appropriate response.

#### Testing Tools
* Unit Testing
    * Django has `TestCase`, an augmented version of the standard `unittest`.
    * TestCase has some additional Django-specific features.
        * Creates a special test database for unit tests.
            * Reset before each individual test is run.
            * Throw away at the end.
    * The test runner is invoked by executing: ```$ python manage.py test [appName]```
* Functional Testing
    * `LiveServerTestCase` class
        * Automatically creates a test database (just like in a unit test run)
        * Automatically starts up a development server for the functional tests to run against.
    * `StaticLiveServerTestCase` class
        * Subclass of `LiveServerTestCase` class
        * Transparently serve all the assets during execution of the tests, incl. static files.
        * Similar to running a development web server with DEBUG = True.
    * The test runner is invoked by executing: ```$python manage.py test [folder_with_functional_tests]```
        * The folder with the functional tests needs to be a valid Python package directory (i.e., with a `___init___.py` in it).
        * The test runner will find any files whose name begins with test.

#### Security
* CSRF protection:
    * Integrated protection that involves placing an auto-generated token into each generated form, to be able to identify POST requests as having come from the original site.
    * The CSRF token can be added by using the template tag `{% csrf_token %}`.
    * During template rendering, the tag is substituted with an `<input type="hidden">` containing the CSRF token.

#### Best Practices
* Always redirect after a POST to prevent duplicate form submissions: Post->Redirect->Get (PRG) web development design pattern.

#### Templates
* Python Variables can be added to HTML templates with the notation: `{{ variable }}`
    * `{{ forloop.counter }}` - a built in variable that indicates the current value of the for loop counter.
* Commands can be added to HTML templates with the notation: `{% command %}`
    * `{% for .. in .. %}` - used for iterating through lists.
        * `{% endfor %}` - indicates the end of the for loop.
    * `{% csrf_token %}` - inserts a CSRF token.
* Inheritance
    * Common content of multiple templates can be put in a common "superclass" template.
    * Supperclass template contains markers of the "blocks", which are places where child templates can customize it.
    * Syntax
        * `{% extends '_superclassTemplate_.html' %}` - used in a child template to define which supperclass template is being inherited.
        * `{% block _blockName_ %}`
            * used in a supperclass template to mark the place which child templates can customize.
            * used in a child template to define the content to be customized in the supperclass template for that block.
        * `{% endblock %}` - specifies the end of block.
* Rendering
    * Templates can be rendered using `django.shortcuts.render` or `django.template.loader.render_to_string` functions
        * The function `django.shortcuts.render` takes a request as its first parameter and the name of the template to render.
        * The function `django.template.loader.render_to_string` takes the name of the template as its parameter.
        * Django automatically searches folders called `templates` inside any of the application directories.
        * Builds and returns an `HttpResponse`, based on the content of the template.

#### Static Files
* Django, as well as any web server, needs to know two things to deal with static files:
    * How to tell when a URL request is for a static file vs. an HTML served via a view function.
        * By defining a URL prefix in settings.py, so that any URLs starting with the prefix should be treated as requests for static files.
    * Where to find the requested static file.
* Django should not be used to serve static content on a production web server
    * Using Python to serve raw files is slow and inefficient
    * Web servers like Apache or Nginx can serve the static files.
* Gathering all static files for deployment
    * All static files should be gather up from inside various app folders, and copied into a single location, ready for deployment.
    * This can be done using the `collectstatic` command.
    * The destination folder, where the collected static files go, is defined in settings.py as `STATIC_ROOT`.

#### Storing Data - Working with Databases

##### Django Object-Relational Mapper (ORM)
* Models the database - a layer of abstraction for data stored in a database with tables, rows, and columns.
* Allows to work with databases using familiar object-oriented metaphors:
    * Classes map to database tables
    * Attributes map to columns
    * Individual instance of the class represents a row of data in the database.
* Database APIs
    * Creating a new record:
        1. Create an object
        2. Assigning some attributes
        3. Calling a .save() function of the object.
    * Querying the database:
        * Using the class attribute .objects
            * .objects.all() retrieves all the records for that table.
            * .objects.count() retrieves the number of entries in the table.
* Create a new model/database table:
    * Create a class in `models.py`, inherit from `django.db.models.Model`.
    * By default, it will get an auto-generated `id` attribute, which will be a primary key column in the database.
    * Other fields(columns) need to be defined explicitly.
    * Build the database = run a migration.
* Relationships between two models/databases:
    * Use `django.db.models.ForeignKey()` to save the relationship to an object from another class.

##### Migrations
* In charge of actually building the database.
* Give the ability to add and remove tables and columns, based on the models.py files.
* Can be seen as a version control system for the database.
    * Particularly useful when there is a need to upgrade a database that’s deployed on a live server.
* Database migration can be built by running ```$ python manage.py makemigrations <app_name>```
    * The migrations are applied automatically to the test database.
* Database migrations for the real database can be executed by running ```$ python manage.py migrate <app_name>```
    * Database can be recreated fresh and empty by running ```$ python manage.py migrate --noinput```
* Deleting migrations is dangerous, but it is needed sometimes when making changes to the models code.
    * Deleting a migration that’s already been applied to a database somewhere should not be done: Django will be confused about what state it’s in, and how to apply future migrations.
    * A migration should be deleted only if it hasn’t been used.
    * A good rule is to never delete or modify a migration that’s already been committed to the VCS.

##### Database Configuration
* The database configuration is in the settings.py file.
* 'ENGINE' specifies the type of database
* 'NAME' specifies the name, with the full path, of the database file.

#### Packages
django.conf
* urls
    * include - a function used to include urls.py from another application, e.g., in the top project.
    * url - a function used to map a part of requested URL to an appropriate view. It is used in the urls.py. It’s likely to be deprecated in a future release.

django.contrib
* staticfiles
    * testing
        * StaticLiveServerTestCase - class derived from django.test.LiveServerTestCase with the ability to transparently serve all the (static) assets during execution of the tests.

django.db
* models
    * Model - a class to be inherited when creating a model for storing data in a database. Classes that inherit map to tables in the databases.
        * save() - saves the record in the database.
        * id - auto-generated id attribute, which is a primary key column.
        * objects - a class attribute
            * all() - a function that retrieves all the records for the modeled table (for the instantiated class).
            * count() - a function that retrieves the number of records in the modeled table. The same as .all().count().
            * create(_variable_=_value_) - a function that is creating a new record in the modeled table with the given variable values. The same as creating an object and calling save().
            * first() - a function that retrieves the first record in the modeled table. The same as objects.all()[0].
            * get(id=_searched\_id_) - a function that returns the entry with the given id.
            * filter(_criterion_) - function that returns objects that satisfy the criterion.
        * _object_\_all -  a reverse lookup, if it has a ForeignKey, that returns all instances of the first model with that ForeignKey.
            * Supports all functions as objects.
    * TextField(_defaultValue_), IntegerField(), CharField(), DateField() - field types.
    * ForeignKey(_Model_, _on\_delete_) - creates a Foreign Key connection between the two Model based classes: in the _self_ one towards the given one

django.http
* HttpRequest - a class which object captures what Django sees when a user’s browser asks for a page.
    * method - contains the information about the request method, e.g., GET, POST.
    * POST - a variable that is a dictionary which contains the POST request variable=value pairs.
        * get(_key_[,_default_]) - a function that returns the value for the given key, if it exists, and _default_ value if it does not exist.
* HttpResponse - a class which object is a response of view function.
    * content - the content of the response in raw bytes that would be sent down the wire to the user’s browser.
        * decode(_encoding_) - a function that converts the raw content into the string of HTML that’s being sent to the user.
    * context - a dictionary that contains the context being passed into the render function.
    * status_code - HTTP response status code

django.shortcuts
* render(HttpRequest, _templateName_, _variables_) - a function that renders the given template with the given variables (as a dictionary).
    * returns an HttpResponse object.
* redirect(_URL_) - a function that does a redirect. Particularly used after processing a POST request, when following the Post/Redirect/Get (PRG) design pattern.

django.test
* TestCase - a class to be inherited when creating unit tests.
    * assertContains(_response_, _string_) - a function that asserts if the given string is in the given response.
    * assertTemplateUsed(_response_, _templateName_) - a function that asserts if the response, returned by the test client, corresponds to the given template.
    * assertRedirects(_response_, _URL_) - a function that asserts if the response redirects to the given URL.
* Client - a class that acts as a dummy Web browser used to test views, if the correct template is being rendered.
    * get(_URL_) - a function that takes a URL, resolves it via views, and returns a HttpResponse.
    * post(_URL_, _data_) - a function that submits a POST request for a given URL with the given data, and returns a HttpResponse.
* LiveServerTestCase - a class to be inherited when creating functional tests.
    * live_server_url - an attribute that holds the URL of the LiveServerTestCase web server.
    * set_window_size(_width_, _height_) - a function that sets the window size of the test browser to the given values.

django.template
* loader
    * render_to_string(_templateName_) - a function that renders the given template and returns a string.

django.urls
* resolve(_url_) - an internal function used to resolve URLs to find what view function they should map to.
    * returns a ResolverMatch object.
* ResolverMatch - a class that captures various metadata about the resolved URL (by the resolve function).
    * func - the view function that would be used to serve the URL.
* path(_route_, _view_, kwargs=None, name=None) - a function used to map the _route_ URL to an appropriate view. It is used in the urls.py.
* re_path(_route_, _view_, kwargs=None, name=None) - a function used to map a part of URL formulated as a RegEx expression _route_ to an appropriate view. It is used in the urls.py.

Key difference between path and re_path is that path uses route without regex 

### Selenium
* common
    * exceptions
        * WebDriverException - an exception raised by Selenium, e.g., when the page hasn’t loaded or Selenium can’t find an element on the page.
* webdriver - used to open a web browser.
    * Firefox() - opens the Firefox web browser.
        * current_url - a variable containing the current URL as a string.
        * get() - opens the web page on the given URL.
        * title - a variable containing the title of the opened webpage.
        * find_elements_by_tag_name() - returns a list of elements with the given tag
        * find_element_by_tag_name() - returns an element with the given tag
        * find_elements_by_id() - returns a list of elements with the given id
        * find_element_by_id() - returns an element with the given id
            * text - the text content of the element
            * get_attribute()
            * location - contains the location cordinates of the element as a dictionary (['x'], ['y']).
            * size - contains the size of the element as a dictionary (['width'], ['height'])
            * send_keys() - typing into input elements the given content, can also send keys (e.g., Keys.ENTER)
        * quit() - closes the web browser.
    * common
        * keys
            * Keys - a class that allows the use of special keys, such as Enter.

### Web Design
#### REST
* Representational State Transfer (REST) is an approach to web design that’s usually used to guide the design of web-based APIs.
* REST suggests to have a URL structure that matches the data structure
* A convention: URLs without a trailing slash are "action" URLs which modify the database.

### Bootstrap
* One of the earliest and most popular CSS frameworks, made by Twitter.
* Facilitates designing websites for multiple platforms, such as mobile, tablets, desktops, etc.
* Comes with a plain, uncustomised installation.
    * Should not be used directly out-of-the-box, at least some minor changes should be made, as ​vanilla Bootstrap is instantly recognisable and a big signal to anyone in the know that no effort was made to style the website. 

## Recommended Readings
* [Mark Pilgrim, Dive Into Python](http://www.diveintopython.net/)
* [Zed A. Shaw, Learn Python the Hard Way](http://learnpythonthehardway.org/)
* [Al Sweigart, Invent Your Own Computer Games with Python](http://inventwithpython.com)
* Kent Beck, Test Driven Development: By Example, Addison-Wesley
* Martin Fowler, Refactoring, Addison-Wesley
* [Ross Anderson, Security Engineering, Second Edition, Addison-Wesley](http://www.cl.cam.ac.uk/~rja14/book.html). First edition is freely available in [PDF](http://www.cl.cam.ac.uk/~rja14/musicfiles/manuscripts/SEv1.pdf)
* Douglas Crockford, JavaScript: The Good Parts, O’Reilly
* [Daniel Greenfeld and Audrey Roy, Two Scoops of Django](http://twoscoopspress.com/products/two-scoops-of-django-1-6)
* [Emily Bache, Mocks, Fakes and Stubs](https://leanpub.com/mocks-fakes-stubs)
* Steve Freeman and Nat Pryce, Growing Object-Oriented Software Guided by Tests, Addison-Wesley
* [How to Customize Twitter's Bootstrap](https://coding.smashingmagazine.com/2013/03/customizing-bootstrap/)