Database Service
^^^^^^^^^^^^^^^^

Not strictly required, it jsut creates a database to test the service against.

This needs some environment variables to be set:

   - DBUSER
   - DBPASSWORD
   - DBNAME

Create the container with::

   make db


Depending on the setup, docker might need to run with sudo permissions, in
which case, the environment variables will have to be passed to this process,
as::

   sudo -E make db


Create the schema::

   sudo -E make schema

Add some test data::

   sudo -E make data
