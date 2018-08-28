Chapter 10 - Example of a Service
=================================

Case: A delivery platform. Check the status of each delivery order by a
GET.


Service: Delivery Status
Persistency: A RDBMS
Response Format: JSON


Running the Service
-------------------

The following environment variables are required to be set::

   - DBUSER
   - DBPASSWORD
   - DBNAME
   - DBHOST
   - DBPORT


Create the container as (this is needed only the first time)::

   sudo make container

Run the container with::

   sudo -E make service


This will start the service, which requires a database available to connect to,
according to the provided parameters of the environment variables ``DBHOST``
and ``DBPORT``. There is an example of a database in ``./libs/storage/db``.

If no parameters are configured, the HTTP service will be running in port
``8080`` by default. Assuming data has been loaded, this can be tested with any
HTTP client::

    $ curl http://localhost:8080/status/1
    {"id":1,"status":"dispatched","msg":"Order was dispatched on 2018-08-01T22:25:12+00:00"}

    $ curl http://localhost:8080/status/99
    Error: 99 was not found

Structure
---------
Main directories:

    - ``libs``: With the Python packages (dependencies) needed by the service.
    - ``statusweb``: The service itself. Imports its dependencies from ``libs```.
