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
* Functional tests drive the development a high level, while the unit tests drive it at a low level.
* TDD workflow:
    1. Write a functional test, which initially fails, describing the new functionality from the user's point of view.
    2. Think how to write code that can get the functional test to pass the current failure,
    and write one or more unit tests to define how the code should behave.
    3. Write the smallest amount of application code just enough to pass the unit test.
    4. Rerun functional tests to see if they pass or get a little further. Iterate the steps 2-4 until the functional test passes.

#### Functional tests = Acceptance tests = End-to-end tests
* Functional tests should help building an application with the right functionality, and guarantee that will never be accidentally broken.
* How the application functions from the user's point of view.
* A sort of specification of the application.
* Tracks a *User Story*
* A human readable story that can be followed.

#### Unit Tests
* Unit tests should help writing code that’s clean and bug free.
* Unit tests test the application from the inside, from the point of view of the programmer.
* ​The idea is that each line of production code should be tested by (at least) one of unit tests.

In Python:
* Module `unittest`, needs to be imported as `import unittest`
* Tests are organised into classes, which inherit from `unittest.TestCase`.
* Any method whose name starts with test is a test method, and will be run by the test runner.
* setUp and tearDown are special methods which get run before and after each test (even if unsuccessful).
* `self.fail` fails no matter what with the given error message.
* Some additional `unittest` helper functions for test assertions: `assertEqual`, `assertTrue`, `assertFalse`.
* If called from command line, the `unittest` test runner can be launched by calling `unittest.main()` within `if __name__ == '__main__'`.

### Django
Creating a new project:
```
$ django-admin.py startproject <project name> .
```

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

File structure:
* tests.py - contains the unit tests for the app.

#### Unit Tests
* Django has `TestCase`, an augmented version of the standard `unittest`.
* TestCase has some additional Django-specific features.

The test runner is invoked by executing:
```
$ python manage.py test
```