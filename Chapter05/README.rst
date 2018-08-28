Chapter 05 - Decorators
=======================

Run the tests with::

    make test

Creating Decorators
^^^^^^^^^^^^^^^^^^^

1. Function decorators

   1.1 ``decorator_function_1.py``.

   1.2 ``decorator_function_2.py``

2. Class decorators

    2.1 ``decorator_class_1.py``

    2.2 ``decorator_class_2.py``

    2.3 ``decorator_class_3.py``

3. Other decorators (generators, coroutines, etc.).

4. Passing Arguments to Decorators

    4.1 As a decorator function: ``decorator_parametrized_1.py``

    4.2 As a decorator object: ``decorator_parametrized_2.py``


Issues to avoid when creating decorators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Keep the properties of the original attributes (docstring, name, etc.),
   by using ``functools.wraps``.

    1.1 ``decorator_wraps_1.py``

2. Don't have side effects on the main body of the decorator. This will run
   at parsing time, and will most likely fail.

    2.1 ``decorator_side_effects_1.py``

    2.2 ``decorator_side_effects_2.py``

3. Make sure the decorated function is equivalent to the wrapped one, in
   terms of inspection, signature checking, etc.

    3.1 Create decorators that work for functions, methods, static methods, class methods, etc.

    3.2 Use the ``wrapt`` package to create effective decorators.


Other Topics
^^^^^^^^^^^^

* The DRY Principle with Decorators (reusing code).
* Separation of Concerns with Decorators.

    Listings: ``decorator_SoC_{1,2}.py``
