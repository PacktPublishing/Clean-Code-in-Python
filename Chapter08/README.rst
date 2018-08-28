Clean code in Python - Chapter 8: Unit testing and refactoring
==============================================================

Install the dependencies::

    make setup


Run the tests::

    make test


Running extra test cases
^^^^^^^^^^^^^^^^^^^^^^^^
For example for to try the mutation testing, or coverage, you can use the
following command::

    make coverage
    make mutation

There are two test cases for each one (1 & 2), which can be specified in the
command. For example::

    make coverage CASE=1
    make mutation CASE=1

As usual, if you don't have the ``make`` command available, you can always run
the code manually with ``python3 <filename>.py``.
