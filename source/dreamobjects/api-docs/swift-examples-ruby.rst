Sample Ruby Code Using DreamObjects OpenStack Swift-compatible API
==================================================================

.. container:: table_of_content

    - :ref:`Swift_Ruby_Creating_A_Connection`
    - :ref:`Swift_Ruby_Listing_Owned_Containers`
    - :ref:`Swift_Ruby_Creating_A_Container`
    - :ref:`Swift_Ruby_Listing_A_Containers_Content`
    - :ref:`Swift_Ruby_Delete_A_Container`
    - :ref:`Swift_Ruby_Creating_An_Object`
    - :ref:`Swift_Ruby_Download_An_Object`
    - :ref:`Swift_Ruby_Delete_An_Object`

.. _Swift_Ruby_Creating_A_Connection:

Creating a Connection
---------------------

This creates a connection so that you can interact with the server.

.. code-block:: ruby

    require 'cloudfiles'
    username = 'account_name:user_name'
    api_key  = 'your_secret_key'

    conn = CloudFiles::Connection.new(
            :username => username,
            :api_key  => api_key,
            :auth_url => 'http://objects.dreamhost.com/auth'
    )


.. _Swift_Ruby_Listing_Owned_Containers:

Listing Owned Containers
------------------------

This gets a list of Containers that you own.
This also prints out the container name.

.. code-block:: ruby

    conn.containers.each do |container|
            puts container
    end

The output will look something like this::

   mahbuckat1
   mahbuckat2
   mahbuckat3


.. _Swift_Ruby_Creating_A_Container:

Creating a Container
--------------------

This creates a new container called ``my-new-container``

.. code-block:: ruby

    container = conn.create_container('my-new-container')


.. _Swift_Ruby_Listing_A_Containers_Content:

Listing a Container's Content
-----------------------------

This gets a list of objects in the container.
This also prints out each object's name, the file size, and last
modified date.

.. code-block:: ruby

    require 'date'  # not necessary in the next version

    container.objects_detail.each do |name, data|
            puts "#{name}\t#{data[:bytes]}\t#{data[:last_modified]}"
    end

The output will look something like this::

   myphoto1.jpg	251262	2011-08-08T21:35:48.000Z
   myphoto2.jpg	262518	2011-08-08T21:38:01.000Z


.. _Swift_Ruby_Delete_A_Container:

Deleting a Container
--------------------

.. note::

   The Container must be empty! Otherwise it won't work!

.. code-block:: ruby

    container.delete_container('my-new-container')


.. _Swift_Ruby_Creating_An_Object:

Creating an Object
------------------

This creates a file ``hello.txt`` from the file named ``my_hello.txt``

.. code-block:: ruby

    obj = container.create_object('hello.txt')
    obj.load_from_filename('./my_hello.txt')
    obj.content_type = 'text/plain'


.. _Swift_Ruby_Download_An_Object:

Download an Object (to a file)
------------------------------

This downloads the object ``hello.txt`` and saves it in
``./my_hello.txt``

.. code-block:: ruby

    obj = container.object('hello.txt')
    obj.save_to_filename('./my_hello.txt')


.. _Swift_Ruby_Delete_An_Object:

Delete an Object
----------------

This deletes the object ``goodbye.txt``

.. code-block:: ruby

    container.delete_object('goodbye.txt')

.. meta::
    :labels: ruby swift
