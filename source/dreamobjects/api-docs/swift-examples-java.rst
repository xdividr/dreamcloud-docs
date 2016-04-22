Sample Java Code Using DreamObjects OpenStack Swift-compatible API
==================================================================

.. container:: table_of_content

    - :ref:`Swift_Java_Setup`
    - :ref:`Swift_Java_Create_A_Connection`
    - :ref:`Swift_Java_List_Owned_Containers`
    - :ref:`Swift_Java_Create_A_Container`
    - :ref:`Swift_Java_List_A_Containers_Content`
    - :ref:`Swift_Java_Delete_A_Container`
    - :ref:`Swift_Java_Create_An_Object`
    - :ref:`Swift_Java_Retrieve_Object_Metadata`
    - :ref:`Swift_Java_Delete_An_Object`

.. _Swift_Java_Setup:

Setup
-----

The following examples use `Apache jclouds <http://jclouds.apache.org>`_. Installing jclouds is easy with
`Apache Maven <http://maven.apache.org>`_, just specify an additional dependency in your pom.xml file.

A sample pom.xml file:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
      <properties>
        <jclouds.version>1.8.0</jclouds.version>
      </properties>
      <groupId>com.mycompany.app</groupId>
      <artifactId>my-app</artifactId>
      <version>1.0-SNAPSHOT</version>
      <dependencies>
        <dependency>
            <groupId>org.apache.jclouds</groupId>
            <artifactId>jclouds-all</artifactId>
            <version>${jclouds.version}</version>
          </dependency>
      </dependencies>
    </project>


Our examples will require some or all of the following java classes to
be imported:

.. code-block:: java

    import org.jclouds.ContextBuilder;
    import org.jclouds.blobstore.BlobStore;
    import org.jclouds.blobstore.BlobStoreContext;
    import org.jclouds.blobstore.domain.Blob;
    import org.jclouds.blobstore.domain.PageSet;
    import org.jclouds.blobstore.domain.BlobMetadata;
    import org.jclouds.blobstore.domain.StorageMetadata;
    import org.jclouds.blobstore.domain.StorageType;
    import org.jclouds.io.Payload;
    import static org.jclouds.Constants.*;
    import com.google.common.io.Files;
    import com.google.common.io.ByteSource;
    import static com.google.common.io.ByteSource.wrap;
    import com.google.common.net.MediaType;
    import com.google.common.base.Charsets;
    import java.io.File;


.. _Swift_Java_Create_A_Connection:

Create a Connection
---------------------

This creates a connection so that you can interact with the server.

.. code-block:: java

    String provider = "swift";
    String identity = "USER:SUB-USER"; // Your DreamObjects user and sub-user
    String password = "SECRET-KEY";    // Your DreamObjects secret key
    String auth_url = "https://objects-us-west-1.dream.io/auth";

    BlobStoreContext context = ContextBuilder.newBuilder(provider)
        .endpoint(auth_url)
        .credentials(identity, password)
        .buildView(BlobStoreContext.class);

    BlobStore blobStore = context.getBlobStore();

    // Close the connection after completing all operations!
    context.close();


.. _Swift_Java_List_Owned_Containers:

List Owned Containers
------------------------

This gets a list of Containers that you own.
This also prints out the container name.

.. code-block:: java

    for (StorageMetadata resourceMd : blobStore.list()) {
        System.out.println(resourceMd.getName());
    }

The output will look something like this::

    container1
    container2
    container3


.. _Swift_Java_Create_A_Container:

Create a Container
--------------------

This creates a new container called ``my-new-container``

.. code-block:: java

    blobStore.createContainerInLocation(null, "my-new-container");


.. _Swift_Java_List_A_Containers_Content:

List a Container's Content
-----------------------------

This gets a list of objects in the container ``my-new-container``.

.. code-block:: java

    PageSet<? extends StorageMetadata> objects = blobStore.list("my-new-container");
    for (StorageMetadata resourceMd : objects) {
        System.out.println(resourceMd.getName());
    }

The output will look something like this::

   myphoto1.jpg
   myphoto2.jpg


.. _Swift_Java_Delete_A_Container:

Delete a Container
--------------------

This deletes the container called ``my-old-container``

.. note::

   The Container must be empty! Otherwise it won't work!

.. code-block:: java

    blobStore.deleteContainer("my-old-container");


.. _Swift_Java_Create_An_Object:

Create an Object
------------------

This creates an object ``foo.txt`` with the string ``Hello World!``
into the container ``my-new-container``

.. code-block:: java

    ByteSource payload = ByteSource.wrap("Hello World!".getBytes(StandardCharsets.UTF_8));
    Blob blob = blobStore.blobBuilder("foo.txt")
        .payload(payload)
        .contentLength(payload.size())
        .contentType("text/plain")
        .build();
    blobStore.putBlob("my-new-container", blob);


This uploads a file called ``bar.txt`` into the container ``my-new-container``

.. code-block:: java

    ByteSource payload = Files.asByteSource(new File("bar.txt"));
    Blob blob = blobStore.blobBuilder("bar.txt")
        .payload(payload)
        .contentDisposition("bar.txt")
        .contentLength(payload.size())
        .contentType(MediaType.OCTET_STREAM.toString())
        .build();
    blobStore.putBlob("my-new-container", blob);


.. _Swift_Java_Retrieve_Object_Metadata:

Retrieve Object Metadata
------------------------

Retrieves metadata and gets content type for object named ``foo.txt``
in the container ``my-new-container``

.. code-block:: java

   BlobMetadata metadata = blobStore.blobMetadata("my-new-container", "foo.txt");
   String contentType = metadata.getContentMetadata().getContentType();


.. _Swift_Java_Delete_An_Object:

Delete an Object
----------------

This deletes the object ``goodbye.txt`` from the container
called ``my-new-container``

.. code-block:: java

    blobStore.removeBlob("my-new-container", "goodbye.txt");

.. meta::
    :labels: java swift
