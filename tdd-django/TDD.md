# Test Driven Development (TDD)
* TDD does not come naturally, it is more like a discipline.
* Do nothing until you have a test! "Test first, test first!".
* Take one step at the time.
* TDD can be seen as a way to save progress, take a break, and make sure to never slip backwards.
    * No need to worry about forgetting what to do next - ​just rerun the tests and they will tell what you need to work on.
    * "TDD is there to help us out when we’re tired and not so smart".
* Functional tests drive the development at a high level, while the unit tests drive it at a low level.

## TDD workflow with functional and unit tests:
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
* Regression is when new code breaks some aspect of the application which used to work.

## Best practices:
* Ensuring test isolation and managing global state
    * Different tests shouldn’t affect one another.
    * Any permanent state needs to be reset at the end of each test.
* Avoid explicit sleeps, e.g., time.sleep
    * The length of waiting time is just a guess: either too short and vulnerable to spurious failures, or too long and it’ll slow down our test runs.
    * Do not rely on Selenium’s implicit waits - the implementation varies between browsers, and it seems highly unreliable.
    * Prefer a retry loop that polls the app and moves on as soon as possible.
* Do not test:
    * Constants
    * Aesthetics, it is similar as testing a constant. However, the implementation of the aesthetics should be tested, e.g., testing that a CSS file loads.

## Functional tests = Acceptance tests = End-to-end tests
* Functional tests should help building an application with the right functionality, and guarantee that will never be accidentally broken.
* How the application functions from the user's point of view.
* A sort of specification of the application.
* Tracks a *User Story*
* A human readable story that can be followed.

## Unit Tests
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
* Some `unittest` helper functions for test assertions:
    * `self.assertIn(_string1_, _string2_)` - checks if `string1` is contained in `string2`.
    * `self.assertEqual(...)`
    * `self.assertAlmostEqual(_value1_, _value2_,...)`
    * `self.assertTrue(...)`
    * `self.assertFalse(...)`
    * `self.assertRegex(_string_, _regex_)` - checks whether the given string matches the given regex.
    * `self.fail(...)` - fails no matter what with the given error message.
* If called from command line, the `unittest` test runner can be launched by calling `unittest.main()` within `if __name__ == '__main__'`.
    * Tests can be run with more detailed information by passing in the verbosity argument: `unittest.main(verbosity=2)`.

## Refactoring
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

## Working Incrementaly
* A critical TDD technique
* The existing code should be adapted using an incremental, step-by-step process
    * Takes from working state to working state.
* No Big Design Up Front
    * Aiming for a minimum viable application as soon as possible
        * the design evolves gradually based on feedback from real-world usage.
    * Thinking about the design is still required
        * Blundering ahead without design thinking eventually gets to the right answer, but
        * little thinking about design gets there faster.
* YAGNI - "You ain’t gonna need it!"
    * It hard to resist the urge to build things just because an idea occurred that they might be needed.
    * Often, no matter how cool, the idea ended up not being used.
        * Results in a lot of unused code, adding to the complexity of the application.
    * YAGNI is the mantra for resisting overenthusiastic creative urges.