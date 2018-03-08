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


## Learning Notes

### TDD
* TDD does not come naturally, it is more like a discipline.
* Do nothing until you have a test! "Test first, test first!".
* Take one step at the time.
* TDD can be seen as a way to save progress, take a break, and make sure to never slip backwards.
    * No need to worry about forgetting what to do next - ​just rerun the tests and they will tell what you need to work on.
    * "TDD is there to help us out when we’re tired and not so smart".
* Functional tests drive the development at a high level, while the unit tests drive it at a low level.
* TDD process with functional and unit tests:
    * [F1] Write a functional test, describing the new functionality from the user's point of view. Proceed with [F2] and see the test failing.
    * [F2] Run the functional test, does it pass? If yes, go to [F4]. If no, proceed with [F3].
    * [F3] Mini-TDD cycle with unit tests:
        * [U1] Write unit test(s) - think how to write code that can get the functional test to pass the current failure, and write one or more unit tests to define how the code should behave. Proceed with [U2] and see the unit tests failing.
        * [U2] TDD Unit-test/code cycle:
            * [UC1] Run the unit tests, do they pass? If yes, finish the unit-test/code cycle and go to [U3]. If no, proceed with [UC2].
            * [UC2] Write some minimal code to get it a little further. Go to [UC1].
        * [U3] Need refactoring? If yes, go to [UC2]. If not finish the mini-TDD cycle and go back to [F2].
    * [F4] Need refactoring? If yes, go back to [F3]. If no, finish or go back to [F1].
* TDD Unit-test/code cycle is also known as Red, Green, Refactor:
    * Start by writing a unit test which fails (Red).
    * Write the simplest possible code to get it to pass (Green), even if that means cheating.
    * Refactor to get to better code that makes more sense.

#### Functional tests = Acceptance tests = End-to-end tests
* Functional tests should help building an application with the right functionality, and guarantee that will never be accidentally broken.
* How the application functions from the user's point of view.
* A sort of specification of the application.
* Tracks a *User Story*
* A human readable story that can be followed.

#### Unit Tests
* Unit tests should help writing code that’s clean and bug free.
* Unit tests test the application from the inside, from the point of view of the programmer.
* ​Each line of production code should be tested by (at least) one of unit tests.
* Every single code change should be driven by the tests.
* Unit tests are about testing logic, flow control, and configuration.
    * Do not test constants, e.g., HTML strings.
* Each unit test should only test one thing.
    * Makes it easier to track down bugs.
    * With multiple assertions in a test: if the test fails on an early assertion, the status of the later assertions is unknown.
* Unit test structure:
    * Code for the test setup.
    * Code that does the exercise.
    * Assert(s).

In Python:
* Module `unittest`, needs to be imported as `import unittest`
* Tests are organised into classes, which inherit from `unittest.TestCase`.
* Any method whose name starts with test is a test method, and will be run by the test runner.
* `setUp()` and `tearDown()` are special methods which get run before and after each test (even if unsuccessful).
* `self.fail(...)` fails no matter what with the given error message.
* Some additional `unittest` helper functions for test assertions: `self.assertEqual(...)`, `self.assertTrue(...)`, `self.assertFalse(...)`.
* If called from command line, the `unittest` test runner can be launched by calling `unittest.main()` within `if __name__ == '__main__'`.

#### Refactoring
* Improving the code without changing its functionality.
* Refactoring should not be done without tests.
* When refactoring, one should work on either the code or the tests, but not both at once.
* If both code and tests need to be refactored:
    1. First, the code should be refactored until all (old) tests are still passing.
    2. Then, the tests can be refactored until they all pass.
* Refactoring should prevent "cheating" code to pass:
    * Triangulation technique: if tests allow "cheating" code to pass, like returning a magic constant, another test should be written that forces some better code to be written.
* Don't Repeat Yourself (DRY) and Three Strikes and Refactor
    * Code can be copy/pasted once, and it may be premature to try to remove the duplication it causes, but once there are three occurrences, it’s time to remove duplication.

### Django
Django’s workflow:
1. An HTTP request comes in for a particular URL.
2. Django uses some rules to decide which view function should deal with the request (this is referred to as resolving the URL).
3. The view function processes the request and returns an HTTP response.

#### Projects
Creating a new project:
```
$ django-admin.py startproject <project name> .
```
File structure:
* settings.py - contains the settings of the project.
    * List of registered apps for the project.
    * Specifications for the used database(s) in the project.
* urls.py - contains mapping from URLs to view functions for the whole site. 

#### manage.py
* `manage.py` is Django’s Swiss Army knife.
Can be used to:
* Run a development server: ```$ python manage.py runserver```
* Invoke test runner: ```$ python manage.py test [appName]```
* Build a database migration: ```$ python manage.py makemigrations```
* Execute a database migration: ```$ python manage.py migrate```
    * Recreate a fresh and empty database: ```$ python manage.py migrate --noinput```

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
* templates/ - contains the templates for rendering. Not initially created, but Django searches this directory for templates by default.
* models.py - contains the models that map to data stored in a database.
* tests.py - contains the unit tests for the app.
* views.py - contains the views, which are functions that render templates, called when resolving URLs. A view function processes user input and returns an appropriate response.

#### Unit Tests
* Django has `TestCase`, an augmented version of the standard `unittest`.
* TestCase has some additional Django-specific features.
    * Creates a special test database for unit tests.

The test runner is invoked by executing:
```
$ python manage.py test [appName]
```

#### Security
* CSRF protection:
    * Integrated protection that involves placing an auto-generated token into each generated form, to be able to identify POST requests as having come from the original site.
    * The CSRF token can be added by using the template tag {% csrf_token %}.
    * During template rendering, the tag is substituted with an `<input type="hidden">` containing the CSRF token.

#### Template Syntax
* Python Variables can be added to HTML templates with the notation: `{{ variable }}`
    * `{{ forloop.counter }}` - a built in variable that indicates the current value of the for loop counter.
* Commands can be added to HTML templates with the notation: `{% command %}`
    * `{% for .. in .. %}` - used for iterating through lists.
        * `{% endfor %}` - indicates the end of the for loop.
    * `{% csrf_token %}` - inserts a CSRF token.

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
        * Using the class attribute .objects, e.g., .objects.all() to retrieve all the records for that table.

##### Migrations
* In charge of actually building the database.
* Give the ability to add and remove tables and columns, based on the models.py files.
* Can be seen as a version control system for the database.
    * Particularly useful when there is a need to upgrade a database that’s deployed on a live server.
* Database migration can be built by running ```$ python manage.py makemigrations```
* Database migrations can be executed by running ```$ python manage.py migrate```
    * Database can be recreated fresh and empty by running ```$ python manage.py migrate --noinput```

##### Database Configuration
* The database configuration is in the settings.py file.
* 'ENGINE' specifies the type of database
* 'NAME' specifies the name, with the full path, of the database file.

#### Packages
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
    * TextField(_defaultValue_), IntegerField(), CharField(), DateField() - field types.

django.http
* HttpRequest - a class which object captures what Django sees when a user’s browser asks for a page.
    * method - contains the information about the request method, e.g., GET, POST.
    * POST - a variable that is a dictionary which contains the POST request variable=value pairs.
        * get(_key_[,_default_]) - a function that returns the value for the given key, if it exists, and _default_ value if it does not exist.
* HttpResponse - a class which object is a response of view function.
    * content - the content of the response in raw bytes that would be sent down the wire to the user’s browser.
        * decode(_encoding_) - a function that converts the raw content into the string of HTML that’s being sent to the user.

django.shortcuts
* render(HttpRequest, _templateName_, _variables_) - a function that renders the given template with the given variables (as a dictionary) and returns a HttpResponse.
* redirect(_URL_) - a function that does a redirect. Particularly used after processing a POST request, when following the Post/Redirect/Get (PRG) design pattern.

django.test
* TestCase - a class to be inherited when creating unit tests.
    * assertTemplateUsed(_response_, _templateName_) - a function that asserts if the response, returned by the test client, corresponds to the given template.
* Client - a class that acts as a dummy Web browser used to test views, if the correct template is being rendered.
    * get(_URL_) - a function that takes a URL, resolves it via views, and returns a HttpResponse.
    * post(_URL_, _data_) - a function that submits a POST request for a given URL with the given data, and returns a HttpResponse.

django.template
* loader
    * render_to_string(_templateName_) - a function that renders the given template and returns a string.

django.urls
* resolve - an internal function used to resolve URLs and find what view function they should map to.

### Selenium
* webdriver - used to open a web browser.
    * Firefox() - opens the Firefox web browser.
        * get() - opens the web page on the given URL.
        * find_elements_by_tag_name() - returns a list of elements with the given tag
        * find_element_by_tag_name() - returns an element with the given tag
        * find_elements_by_id() - returns a list of elements with the given id
        * find_element_by_id() - returns an element with the given id
            * text - the text content of the element
            * get_attribute()
            * send_keys() - typing into input elements the given content, can also send keys (e.g., Keys.ENTER)
        * quit() - closes the web browser.
    * common
        * keys
            * Keys - a class that allows the use of special keys, such as Enter.

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