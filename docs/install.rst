Installation
============

PyPI
----

Install pmesh and its dependencies from PyPI:

.. code-block:: sh

    pip install pmesh

pmesh depends on `pfft-python <http://github.com/rainwoodman/pfft-python>`_ for fast fourier
transformation, which will be installed automatically.


For Development
---------------

Clone the repository and install in development mode:

.. code-block:: sh

    git clone https://github.com/rainwoodman/pmesh
    cd pmesh
    pip install -e ".[full]"

This will install pmesh in editable mode with all optional dependencies.

The development shall ideally be test driven. Write test cases
in the tests directories in the source code, then invoke them with

.. code-block:: sh

    python run-tests.py pmesh/tests/test_....py::test_...

or with a single rank

.. code-block:: sh

    python run-tests.py --single pmesh/tests/test_....py::test_...

Replace `...` with names of files and functions.

`run-tests.py` takes care of building and installation before testing.

