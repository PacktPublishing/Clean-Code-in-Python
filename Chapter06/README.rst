Getting More out of our Objects With Descriptors
================================================

Run tests::

  make test

A First Look at Descriptors
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``descriptor_1.py``: First high-level example illustrating the descriptor
  protocol.


Methods
-------

Files for these examples are ``descriptors_methods_{1,2,3,4}.py``, respectively
for:

* ``__get__``
* ``__set__``
* ``__delete__``
* ``__set_name__``

Descriptors in Action
---------------------

* An application of descriptors: ``descriptors_pythonic_{1,2}.py``
* Different forms of implementing descriptors (``__dict__`` vs. ``weakref``):
  ``descriptors_implementation_{1,2}.py``


Uses of Descriptors in CPython
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Internals of descriptors: ``descriptors_cpython_{1..3}.py``.
* Functions and methods: ``descriptors_methods_{1..4}.py``.
* ``__slots__``
* ``@property``, ``@classmethod``, and ``@staticmethod``.


Uses of descriptors
^^^^^^^^^^^^^^^^^^^

* Reuse code
* Avoid class decorators: ``descriptors_uses_{1,2}.py``
