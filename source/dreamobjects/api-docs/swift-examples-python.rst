Sample Python Code Using DreamObjects OpenStack Swift-compatible API
====================================================================

.. container:: table_of_content

    - :ref:`Swift_Python_Creating_A_Connection`
    - :ref:`Swift_Python_Listing_Owned_Containers`
    - :ref:`Swift_Python_Creating_A_Container`
    - :ref:`Swift_Python_Listing_A_Containers_Content`
    - :ref:`Swift_Python_Deleting_A_Container`
    - :ref:`Swift_Python_Creating_An_Object`
    - :ref:`Swift_Python_Download_An_Object`
    - :ref:`Swift_Python_Delete_An_Object`

.. _Swift_Python_Creating_A_Connection:

Creating a Connection
---------------------

This creates a connection so that you can interact with the server.

.. code-block:: python

    import cloudfiles
    username = 'account_name:username'
    api_key = 'your_api_key'

    conn = cloudfiles.get_connection(
            username=username,
            api_key=api_key,
            authurl='https://objects-us-west-1.dream.io/auth',
            )


.. _Swift_Python_Listing_Owned_Containers:

Listing Owned Containers
------------------------

This gets a list of Containers that you own.
This also prints out the container name.

.. code-block:: python

    for container in conn.get_all_containers():
            print container.name

The output will look something like this::

   mahbuckat1
   mahbuckat2
   mahbuckat3


.. _Swift_Python_Creating_A_Container:

Creating a Container
--------------------

This creates a new container called ``my-new-container``

.. code-block:: python

    container = conn.create_container('my-new-container')


.. _Swift_Python_Listing_A_Containers_Content:

Listing a Container's Content
-----------------------------

This gets a list of objects in the container.
This also prints out each object's name, the file size, and last
modified date.

.. code-block:: python

    for obj in container.get_objects():
            print "{0}\t{1}\t{2}".format(obj.name, obj.size, obj.last_modified)

The output will look something like this::

   myphoto1.jpg	251262	2011-08-08T21:35:48.000Z
   myphoto2.jpg	262518	2011-08-08T21:38:01.000Z


.. _Swift_Python_Deleting_A_Container:

Deleting a Container
--------------------

.. note::

   The Container must be empty! Otherwise it won't work!

.. code-block:: python

    conn.delete_container(container.name)


.. _Swift_Python_Creating_An_Object:

Creating an Object
------------------

This creates a file ``hello.txt`` from the file named ``my_hello.txt``

.. code-block:: python

    obj = container.create_object('hello.txt')
    obj.content_type = 'text/plain'
    obj.load_from_filename('./my_hello.txt')


.. _Swift_Python_Download_An_Object:

Download an Object (to a file)
------------------------------

This downloads the object ``hello.txt`` and saves it in
``./my_hello.txt``

.. code-block:: python

    obj = container.get_object('hello.txt')
    obj.save_to_filename('./my_hello.txt')


.. _Swift_Python_Delete_An_Object:

Delete an Object
----------------

This deletes the object ``goodbye.txt``

.. code-block:: python

    container.delete_object('goodbye.txt')

.. meta::
    :labels: python swift
