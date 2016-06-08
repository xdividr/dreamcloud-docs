Sample Python Code Using DreamObjects S3-compatible API And Boto
================================================================

.. container:: table_of_content

    - :ref:`S3_Python_Creating_A_Connection`
    - :ref:`S3_Python_Listing_Owned_Buckets`
    - :ref:`S3_Python_Creating_A_Bucket`
    - :ref:`S3_Python_Listing_A_Buckets_Content`
    - :ref:`S3_Python_Deleting_A_Bucket`
    - :ref:`S3_Python_Forced_Delete_For_Non-Empty_Buckets`
    - :ref:`S3_Python_Creating_An_Object`
    - :ref:`S3_Python_Change_An_Objects_ACL`
    - :ref:`S3_Python_Download_An_Object`
    - :ref:`S3_Python_Delete_An_Object`
    - :ref:`S3_Python_Generate_Object_Download_URLs`

.. _S3_Python_Creating_A_Connection:

Creating a Connection
---------------------

This creates a connection so that you can interact with the server.

.. code-block:: python

    import boto
    import boto.s3.connection
    access_key = 'put your access key here!'
    secret_key = 'put your secret key here!'

    conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = 'objects-us-west-1.dream.io',
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )


.. _S3_Python_Listing_Owned_Buckets:

Listing Owned Buckets
---------------------

This gets a list of Buckets that you own.
This also prints out the bucket name and creation date of each bucket.

.. code-block:: python

    for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
            name = bucket.name,
            created = bucket.creation_date,
            )

The output will look something like this::

   mahbuckat1	2011-04-21T18:05:39.000Z
   mahbuckat2	2011-04-21T18:05:48.000Z
   mahbuckat3	2011-04-21T18:07:18.000Z


.. _S3_Python_Creating_A_Bucket:

Creating a Bucket
-----------------

This creates a new bucket called ``my-new-bucket``

.. code-block:: python

    bucket = conn.create_bucket('my-new-bucket')


.. _S3_Python_Listing_A_Buckets_Content:

Listing a Bucket's Content
--------------------------

This gets a list of objects in the bucket.
This also prints out each object's name, the file size, and last
modified date.

.. code-block:: python

    for key in bucket.list():
        print "{name}\t{size}\t{modified}".format(
            name = key.name,
            size = key.size,
            modified = key.last_modified,
            )

The output will look something like this::

   myphoto1.jpg	251262	2011-08-08T21:35:48.000Z
   myphoto2.jpg	262518	2011-08-08T21:38:01.000Z


.. _S3_Python_Deleting_A_Bucket:

Deleting a Bucket
-----------------

.. note::

   The Bucket must be empty! Otherwise it won't work!

.. code-block:: python

    conn.delete_bucket(bucket.name)


.. _S3_Python_Forced_Delete_For_Non-Empty_Buckets:

Forced Delete for Non-empty Buckets
-----------------------------------

.. attention::

   not available in python


.. _S3_Python_Creating_An_Object:

Creating an Object
------------------

This creates a file ``hello.txt`` with the string ``"Hello World!"``

.. code-block:: python

    key = bucket.new_key('hello.txt')
    key.set_contents_from_string('Hello World!')


.. _S3_Python_Change_An_Objects_ACL:

Change an Object's ACL
----------------------

This makes the object ``hello.txt`` to be publicly readable, and
``secret_plans.txt`` to be private.

.. code-block:: python

    hello_key = bucket.get_key('hello.txt')
    hello_key.set_canned_acl('public-read')
    plans_key = bucket.get_key('secret_plans.txt')
    plans_key.set_canned_acl('private')


.. _S3_Python_Download_An_Object:

Download an Object (to a file)
------------------------------

This downloads the object ``perl_poetry.pdf`` and saves it in
``/home/larry/documents/``

.. code-block:: python

    key = bucket.get_key('perl_poetry.pdf')
    key.get_contents_to_filename('/home/larry/documents/perl_poetry.pdf')


.. _S3_Python_Delete_An_Object:

Delete an Object
----------------

This deletes the object ``goodbye.txt``

.. code-block:: python

    bucket.delete_key('goodbye.txt')


.. _S3_Python_Generate_Object_Download_URLs:

Generate Object Download URLs (signed and unsigned)
---------------------------------------------------

This generates an unsigned download URL for ``hello.txt``. This works
because we made ``hello.txt`` public by setting the ACL above.
This then generates a signed download URL for ``secret_plans.txt`` that
will work for 1 hour. Signed download URLs will work for the time
period even if the object is private (when the time period is up, the
URL will stop working).

.. code-block:: python

    hello_key = bucket.get_key('hello.txt')
    hello_url = hello_key.generate_url(0, query_auth=False, force_http=True)
    print hello_url

    plans_key = bucket.get_key('secret_plans.txt')
    plans_url = plans_key.generate_url(3600, query_auth=True, force_http=True)
    print plans_url

The output of this will look something like::

   http://objects-us-west-1.dream.io/my-bucket-name/hello.txt
   http://objects-us-west-1.dream.io/my-bucket-name/secret_plans.txt?Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXX&Expires=1316027075&AWSAccessKeyId=XXXXXXXXXXXXXXXXXXX

.. meta::
    :labels: python S3
