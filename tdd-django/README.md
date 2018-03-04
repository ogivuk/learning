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
* TDD steps:
    1. Write a test, run it and check that it fails as expected.

#### Functional tests = Acceptance tests = End-to-end tests
* How the application functions from the user's point of view.
* A sort of specification of the application.
* Tracks a *User Story*
* A human readable story that can be followed.

#### Unit Tests

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
$ django-admin.py startproject <emph>projectName</emph> .
```
*manage.py* is Django’s Swiss Army knife. 

Running a development server:
```
$ python manage.py runserver
```