============================================
How To Use DreamObjects Swift Compatible API
============================================

.. container:: table_of_content

    - :ref:`Common_Entities_Swift`
    - :ref:`Authentication_Swift`
    - :ref:`Service_Operations_Swift`
    - :ref:`Container_Operations_Swift`
    - :ref:`Object_Operations_Swift`

.. _Common_Entities_Swift:

Common Entities
---------------

Response Status
~~~~~~~~~~~~~~~

+---------------+-----------------------------------+-------------------+
| HTTP Status   | Response Code                     | Description       |
+===============+===================================+===================+
| 100           |                                   | Continue          |
+---------------+-----------------------------------+-------------------+
| 200           |                                   | Success           |
+---------------+-----------------------------------+-------------------+
| 201           | Created                           |                   |
+---------------+-----------------------------------+-------------------+
| 202           | Accepted                          |                   |
+---------------+-----------------------------------+-------------------+
| 204           | NoContent                         |                   |
+---------------+-----------------------------------+-------------------+
| 206           |                                   | Partial content   |
+---------------+-----------------------------------+-------------------+
| 304           | NotModified                       |                   |
+---------------+-----------------------------------+-------------------+
| 400           | InvalidArgument                   |                   |
+---------------+-----------------------------------+-------------------+
| 400           | InvalidDigest                     |                   |
+---------------+-----------------------------------+-------------------+
| 400           | BadDigest                         |                   |
+---------------+-----------------------------------+-------------------+
| 400           | InvalidBucketName                 |                   |
+---------------+-----------------------------------+-------------------+
| 400           | InvalidObjectName                 |                   |
+---------------+-----------------------------------+-------------------+
| 400           | UnresolvableGrantByEmailAddress   |                   |
+---------------+-----------------------------------+-------------------+
| 400           | RequestTimeout                    |                   |
+---------------+-----------------------------------+-------------------+
| 400           | EntityTooLarge                    |                   |
+---------------+-----------------------------------+-------------------+
| 401           | UserSuspended                     |                   |
+---------------+-----------------------------------+-------------------+
| 401           | AccessDenied                      |                   |
+---------------+-----------------------------------+-------------------+
| 403           | RequestTimeTooSkewed              |                   |
+---------------+-----------------------------------+-------------------+
| 404           | NoSuchKey                         |                   |
+---------------+-----------------------------------+-------------------+
| 404           | NoSuchBucket                      |                   |
+---------------+-----------------------------------+-------------------+
| 404           | NoSuchUpload                      |                   |
+---------------+-----------------------------------+-------------------+
| 405           | MethodNotAllowed                  |                   |
+---------------+-----------------------------------+-------------------+
| 408           | RequestTimeout                    |                   |
+---------------+-----------------------------------+-------------------+
| 409           | BucketAlreadyExists               |                   |
+---------------+-----------------------------------+-------------------+
| 409           | BucketNotEmpty                    |                   |
+---------------+-----------------------------------+-------------------+
| 411           | MissingContentLength              |                   |
+---------------+-----------------------------------+-------------------+
| 412           | PreconditionFailed                |                   |
+---------------+-----------------------------------+-------------------+
| 412           | Invalid UTF8                      |                   |
+---------------+-----------------------------------+-------------------+
| 412           | BadURL                            |                   |
+---------------+-----------------------------------+-------------------+
| 416           | InvalidRange                      |                   |
+---------------+-----------------------------------+-------------------+
| 422           | UnprocessableEntity               |                   |
+---------------+-----------------------------------+-------------------+
| 500           | InternalError                     |                   |
+---------------+-----------------------------------+-------------------+

.. _Authentication_Swift:

How to Authenticate to DreamObjects with the Swift API
------------------------------------------------------

Using the Swift API, authenticated requests need to contain an
authentication token. The authentication token may be obtained through
an authenticator. DreamObjects can also serve as the authenticator. The
``{api version}/{account}`` prefix that this documentation specify in each
request is also obtained through the authentication process.

Swift Auth Compatible RESTful API
---------------------------------

The Swift Auth API is being used for the generation of tokens that can
be used with the RGW Swift API.

Auth Get
~~~~~~~~

Syntax
^^^^^^

::

    GET /auth HTTP/1.1

Request Headers
^^^^^^^^^^^^^^^

+---------------+----------+---------------+
| Name          | Type     | Description   |
+===============+==========+===============+
| X-Auth-Key    | String   |               |
+---------------+----------+---------------+
| X-Auth-User   | String   |               |
+---------------+----------+---------------+

Response Headers
^^^^^^^^^^^^^^^^

+-------------------+----------+---------------+
| Name              | Type     | Description   |
+===================+==========+===============+
| X-Storage-Url     | String   |               |
+-------------------+----------+---------------+
| X-Storage-Token   | String   |               |
+-------------------+----------+---------------+


Access Control Lists
--------------------

TBD

.. _Service_Operations_Swift:

Understand DreamObjects Swift-compatible Service Operations
-----------------------------------------------------------

List Containers
~~~~~~~~~~~~~~~

A request that lists the buckets can only be run using a specific user's
credentials, and cannot be run anonymously

Syntax
^^^^^^

::

    GET /{api version}/{account} HTTP/1.1

Parameters
^^^^^^^^^^

+----------+-----------------+----------------+------------+
| Name     | Description     | Valid Values   | Required   |
+==========+=================+================+============+
| format   | result format   | json, xml      | No         |
+----------+-----------------+----------------+------------+
| marker   |                 |                | No         |
+----------+-----------------+----------------+------------+
| limit    |                 |                | No         |
+----------+-----------------+----------------+------------+

Headers
^^^^^^^

Response Entities
^^^^^^^^^^^^^^^^^

+-------------+-------------+---------------------------------------+
| Name        | Type        | Description                           |
+=============+=============+=======================================+
| account     | Container   | Container for list of containers      |
+-------------+-------------+---------------------------------------+
| container   | Container   | Container for container information   |
+-------------+-------------+---------------------------------------+
| name        | String      | Bucket name                           |
+-------------+-------------+---------------------------------------+
| bytes       | Integer     | Total container size                  |
+-------------+-------------+---------------------------------------+

.. _Container_Operations_Swift:

Understand DreamObjects Swift-compatible Container Operations
-------------------------------------------------------------

Create Container
~~~~~~~~~~~~~~~~

DreamObjects Containers are referred to as "Buckets."  Buckets are storage
areas that can hold data, also known as "Objects."

Constraints
^^^^^^^^^^^

Bucket names are used in the URL when accessing objects, and must be globally unique.


Syntax
^^^^^^

::

    PUT /{api version}/{account}/{container} HTTP/1.1



Parameters
^^^^^^^^^^

Headers
^^^^^^^

+-----------------------+---------------+------------+
| Name                  | Description   | Required   |
+=======================+===============+============+
| X-Container-Read      |               | No         |
+-----------------------+---------------+------------+
| X-Container-Write     |               | No         |
+-----------------------+---------------+------------+
| X-Container-Meta-\*   |               | No         |
+-----------------------+---------------+------------+

HTTP Response
^^^^^^^^^^^^^

If a container with the same name already exists, and the user is the
container owner, the operation will succeed. Otherwise the operation
will fail.

+---------------+-----------------------+-------------------------------------------------------------+
| HTTP Status   | Status Code           | Description                                                 |
+===============+=======================+=============================================================+
| 409           | BucketAlreadyExists   | Container already exists under different user's ownership   |
+---------------+-----------------------+-------------------------------------------------------------+

Remove Container
~~~~~~~~~~~~~~~~

Deletes a DreamObjects container, also known as a "Bucket". Once you've successfully removed the Bucket,
you'll be able to reuse the Bucket name.

If you'd like to check and see if the Bucket is empty, or contains any Objects before you remove it, you
can use a HEAD request against the Bucket

Syntax
^^^^^^

::

     DELETE /{api version}/{account}/{container} HTTP/1.1

Headers
^^^^^^^

HTTP Response
^^^^^^^^^^^^^

+---------------+---------------+---------------------+
| HTTP Status   | Status Code   | Description         |
+===============+===============+=====================+
| 204           | NoContent     | Container removed   |
+---------------+---------------+---------------------+

List Container Objects
~~~~~~~~~~~~~~~~~~~~~~

Use the Get request in combination with the Bucket name to retrieve a list of the objects stored within.

You can specify query parameters to filter the full list, or leave out the paremeters to return a list
of the first 10,000 object names stored in the Bucket.

Syntax
^^^^^^

::

      GET /{api version}/{account}/{container}[?parm=value] HTTP/1.1

Parameters
^^^^^^^^^^

+-------------+-----------------+----------------+------------+
| Name        | Description     | Valid Values   | Required   |
+=============+=================+================+============+
| format      | result format   | json, xml      | No         |
+-------------+-----------------+----------------+------------+
| prefix      |                 |                | No         |
+-------------+-----------------+----------------+------------+
| marker      |                 |                | No         |
+-------------+-----------------+----------------+------------+
| limit       |                 |                | No         |
+-------------+-----------------+----------------+------------+
| delimiter   |                 |                | No         |
+-------------+-----------------+----------------+------------+
| path        |                 |                | No         |
+-------------+-----------------+----------------+------------+

Response Entities
^^^^^^^^^^^^^^^^^

+------------------+-------------+---------------+
| Name             | Type        | Description   |
+==================+=============+===============+
| container        | Container   |               |
+------------------+-------------+---------------+
| object           | Container   |               |
+------------------+-------------+---------------+
| name             | String      |               |
+------------------+-------------+---------------+
| hash             | String      |               |
+------------------+-------------+---------------+
| last\_modified   | Date        |               |
+------------------+-------------+---------------+
| hash             | String      |               |
+------------------+-------------+---------------+
| content\_type    | String      |               |
+------------------+-------------+---------------+

Update Container Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~

Create any, and as many metadata headers as you want, but they'll need to use the
X-Container-Meta- format.

Syntax
^^^^^^

::

    POST /{api version}/{account}/{container}/{object} HTTP/1.1

Request Headers
^^^^^^^^^^^^^^^

+---------------------+---------------+----------------+------------+
| Name                | Description   | Valid Values   | Required   |
+=====================+===============+================+============+
| X-Container-Read    |               |                | No         |
+---------------------+---------------+----------------+------------+
| X-Container-Write   |               |                | No         |
+---------------------+---------------+----------------+------------+

.. _Object_Operations_Swift:

Understand DreamObjects Swift-compatible Object Operations
----------------------------------------------------------

Put Object
~~~~~~~~~~

Adds an object to a Bucket.  You must have write permissions on the Bucket to
perform this operation.

Syntax
^^^^^^

::

    PUT /{api version}/{account}/{container}/{object} HTTP/1.1

Request Headers
^^^^^^^^^^^^^^^

+---------------------+---------------+----------------+------------+
| Name                | Description   | Valid Values   | Required   |
+=====================+===============+================+============+
| ETag                |               |                | No         |
+---------------------+---------------+----------------+------------+
| Content-Type        |               |                | No         |
+---------------------+---------------+----------------+------------+
| Transfer-Encoding   |               | chunked        | No         |
+---------------------+---------------+----------------+------------+

Copy Object
~~~~~~~~~~~

To copy an object, use PUT and specify a destination bucket and the object name.

Syntax
^^^^^^

::

    PUT /{api version}/{account}/{dest-container}/{dest-object} HTTP/1.1
    x-amz-copy-source: {source-container}/{source-object}

or alternatively:

::

    COPY /{api version}/{account}/{source-container}/{source-object} HTTP/1.1
    Destination: /{dest-container}/{dest-object}

Request Headers
^^^^^^^^^^^^^^^

+-----------------------+---------------+----------------+--------------+
| Name                  | Description   | Valid Values   | Required     |
+=======================+===============+================+==============+
| X-Copy-From           |               |                | Yes (PUT)    |
+-----------------------+---------------+----------------+--------------+
| Destination           |               |                | Yes (COPY)   |
+-----------------------+---------------+----------------+--------------+
| If-Modified-Since     |               |                | No           |
+-----------------------+---------------+----------------+--------------+
| If-Unmodified-Since   |               |                | No           |
+-----------------------+---------------+----------------+--------------+
| Copy-If-Match         |               |                | No           |
+-----------------------+---------------+----------------+--------------+
| Copy-If-None-Match    |               |                | No           |
+-----------------------+---------------+----------------+--------------+

Remove Object
~~~~~~~~~~~~~

Removes an object. Requires WRITE permission set on the containing
Bucket.


Syntax
^^^^^^

::

    DELETE /{api version}/{account}/{container}/{object} HTTP/1.1

Get Object
~~~~~~~~~~

Retrieve an Object's data using the GET request.

You can pefrom conditional GET requests using if-* headers.

You can also fetch only a portion of the data using Range headers.


Syntax
^^^^^^

::

    GET /{api version}/{account}/{container}/{object} HTTP/1.1

Request Headers
^^^^^^^^^^^^^^^

+-----------------------+---------------+----------------+------------+
| Name                  | Description   | Valid Values   | Required   |
+=======================+===============+================+============+
| Range                 |               |                | No         |
+-----------------------+---------------+----------------+------------+
| If-Modified-Since     |               |                | No         |
+-----------------------+---------------+----------------+------------+
| If-Unmodified-Since   |               |                | No         |
+-----------------------+---------------+----------------+------------+
| If-Match              |               |                | No         |
+-----------------------+---------------+----------------+------------+
| If-None-Match         |               |                | No         |
+-----------------------+---------------+----------------+------------+

Response Headers
^^^^^^^^^^^^^^^^

+-----------------+---------------------------------------------------+
| Name            | Description                                       |
+=================+===================================================+
| Content-Range   | Data range, will only be returned if the range    |
|                 | header field was specified in the request         |
+-----------------+---------------------------------------------------+

Get Object Info
~~~~~~~~~~~~~~~

Returns information about object. This request will return the same
header information as the Get Object request, but will not include
the object data payload.

Syntax
^^^^^^

::

    HEAD /{api version}/{account}/{container}/{object} HTTP/1.1

Request Headers
^^^^^^^^^^^^^^^

+-----------------------+---------------+----------------+------------+
| Name                  | Description   | Valid Values   | Required   |
+=======================+===============+================+============+
| Range                 |               |                | No         |
+-----------------------+---------------+----------------+------------+
| If-Modified-Since     |               |                | No         |
+-----------------------+---------------+----------------+------------+
| If-Unmodified-Since   |               |                | No         |
+-----------------------+---------------+----------------+------------+
| If-Match              |               |                | No         |
+-----------------------+---------------+----------------+------------+
| If-None-Match         |               |                | No         |
+-----------------------+---------------+----------------+------------+

Update Object Metadata
~~~~~~~~~~~~~~~~~~~~~~

You can use POST operations against an object name to set and
overwrite arbitrary key/value metadata.  You can also use POST operations
to assign headers that are not already assigned such as X-Delete-At
or X-Delete-After for expiring objects.

You cannot use the POST operation to change any of the object's other
headers such as Content-Type, ETag, etc. It is not used to upload storage
objects (see PUT). When you need to update metadata or other headers such
as Content-Type or CORS headers, refer to copying an object.

Key names must be prefixed with X-Object-Meta-. A POST request will delete
all existing metadata added with a previous PUT/POST.

Syntax
^^^^^^

::

    POST /{api version}/{account}/{container}/{object} HTTP/1.1

Request Headers
^^^^^^^^^^^^^^^

+--------------------+----------+---------------+
| Name               | Type     | Description   |
+====================+==========+===============+
| X-Object-Meta-\*   | String   |               |
+--------------------+----------+---------------+


.. meta::
    :labels: swift authentication bucket object
