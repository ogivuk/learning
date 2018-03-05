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
* TDD workflow:
    1. Write a functional test, which initially fails, describing the new functionality from the user's point of view.
    2. Think how to write code that can get the functional test to pass the current failure,
    and write one or more unit tests to define how the code should behave.
    3. Write the smallest amount of application code just enough to pass the unit test.
    4. Rerun functional tests to see if they pass or get a little further. Iterate the steps 2-4 until the functional test passes.
* TDD unit-test/code cycle:
    1. Run the unit tests and see how they fail.
    2. Make a minimal code change to address the current test failure.
    3. Repeat the steps 1. and 2. until the unit tests pass.

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

In Python:
* Module `unittest`, needs to be imported as `import unittest`
* Tests are organised into classes, which inherit from `unittest.TestCase`.
* Any method whose name starts with test is a test method, and will be run by the test runner.
* setUp and tearDown are special methods which get run before and after each test (even if unsuccessful).
* `self.fail` fails no matter what with the given error message.
* Some additional `unittest` helper functions for test assertions: `assertEqual`, `assertTrue`, `assertFalse`.
* If called from command line, the `unittest` test runner can be launched by calling `unittest.main()` within `if __name__ == '__main__'`.

#### Refactoring
* Improving the code without changing its functionality.
* Refactoring should not be done without tests.
* When refactoring, one should work on either the code or the tests, but not both at once.
* If both code and tests need to be refactored:
    1. First, the code should be refactored until all (old) tests are still passing.
    2. Then, the tests can be refactored until they all pass.

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
* urls.py - contains mapping from URLs to view functions for the whole site. 

#### manage.py
* `manage.py` is Django’s Swiss Army knife.
Can be used to:
* Run a development server: ```$ python manage.py runserver```
* Invoke test runner: ```$ python manage.py test```

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
* templates/ - contains the templates for rendering. Not initially created, but Django searches this directory for templates by default.
* tests.py - contains the unit tests for the app.
* views.py - contains the views, which are functions that render templates, called when resolving URLs.

#### Unit Tests
* Django has `TestCase`, an augmented version of the standard `unittest`.
* TestCase has some additional Django-specific features.

The test runner is invoked by executing:
```
$ python manage.py test
```

#### Packages
django.http
* HttpRequest - a class which object captures what Django sees when a user’s browser asks for a page.
* HttpResponse - a class which object is a response of view function.
    * content - the content of the response in raw bytes that would be sent down the wire to the user’s browser.
        * decode(_encoding_) - a function that converts the raw content into the string of HTML that’s being sent to the user.

django.shortcuts
* render(HttpRequest, _templateName_) - a function that renders the given template and returns a HttpResponse.

django.test
* TestCase - a class to be inherited when creating unit tests.
    * assertTemplateUsed(_response_, _templateName_) - a function that asserts if the response, returned by the test client, corresponds to the given template.
* Client - a class that acts as a dummy Web browser used to test views, if the correct template is being rendered.
    * get(_URL_to_be_tested_) - a function that takes a URL, resolves it via views, and returns a HttpResponse

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