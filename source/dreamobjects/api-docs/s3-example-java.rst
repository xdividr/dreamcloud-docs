.. _java:

Sample Java Code Using DreamObjects S3-compatible API
=====================================================

.. container:: table_of_content

    - :ref:`S3_Java_Setup`
    - :ref:`S3_Java_Creating_A_Connection`
    - :ref:`S3_Java_Listing_Owned_Buckets`
    - :ref:`S3_Java_Creating_A_Bucket`
    - :ref:`S3_Java_Listing_A_Buckets_Content`
    - :ref:`S3_Java_Deleting_A_Bucket`
    - :ref:`S3_Java_Forced_Delete_For_Non-Empty_Buckets`
    - :ref:`S3_Java_Creating_An_Object`
    - :ref:`S3_Java_Change_An_Objects_ACL`
    - :ref:`S3_Java_Download_An_Object`
    - :ref:`S3_Java_Delete_An_Object`
    - :ref:`S3_Java_Generate_Object_Download_URLs`

.. _S3_Java_Setup:

Setup
-----

The following examples may require some or all of the following java
classes to be imported:

.. code-block:: java

    import java.io.ByteArrayInputStream;
    import java.io.File;
    import java.util.List;
    import com.amazonaws.auth.AWSCredentials;
    import com.amazonaws.auth.BasicAWSCredentials;
    import com.amazonaws.util.StringUtils;
    import com.amazonaws.services.s3.AmazonS3;
    import com.amazonaws.services.s3.AmazonS3Client;
    import com.amazonaws.services.s3.model.Bucket;
    import com.amazonaws.services.s3.model.CannedAccessControlList;
    import com.amazonaws.services.s3.model.GeneratePresignedUrlRequest;
    import com.amazonaws.services.s3.model.GetObjectRequest;
    import com.amazonaws.services.s3.model.ObjectListing;
    import com.amazonaws.services.s3.model.ObjectMetadata;
    import com.amazonaws.services.s3.model.S3ObjectSummary;


.. _S3_Java_Creating_A_Connection:

Creating a Connection
---------------------

This creates a connection so that you can interact with the server.

.. code-block:: java

    String accessKey = "insert your access key here!";
    String secretKey = "insert your secret key here!";

    AWSCredentials credentials = new BasicAWSCredentials(accessKey, secretKey);
    AmazonS3 conn = new AmazonS3Client(credentials);
    conn.setEndpoint("objects.dreamhost.com");


.. _S3_Java_Listing_Owned_Buckets:

Listing Owned Buckets
---------------------

This gets a list of Buckets that you own.
This also prints out the bucket name and creation date of each bucket.

.. code-block:: java

    List<Bucket> buckets = conn.listBuckets();
    for (Bucket bucket : buckets) {
            System.out.println(bucket.getName() + "\t" +
                    StringUtils.fromDate(bucket.getCreationDate()));
    }

The output will look something like this::

   mahbuckat1	2011-04-21T18:05:39.000Z
   mahbuckat2	2011-04-21T18:05:48.000Z
   mahbuckat3	2011-04-21T18:07:18.000Z


.. _S3_Java_Creating_A_Bucket:

Creating a Bucket
-----------------

This creates a new bucket called ``my-new-bucket``

.. code-block:: java

    Bucket bucket = conn.createBucket("my-new-bucket");


.. _S3_Java_Listing_A_Buckets_Content:

Listing a Bucket's Content
--------------------------
This gets a list of objects in the bucket.
This also prints out each object's name, the file size, and last
modified date.

.. code-block:: java

    ObjectListing objects = conn.listObjects(bucket.getName());
    do {
            for (S3ObjectSummary objectSummary : objects.getObjectSummaries()) {
                    System.out.println(objectSummary.getKey() + "\t" +
                            ObjectSummary.getSize() + "\t" +
                            StringUtils.fromDate(objectSummary.getLastModified()));
            }
            objects = conn.listNextBatchOfObjects(objects);
    } while (objects.isTruncated());

The output will look something like this::

   myphoto1.jpg	251262	2011-08-08T21:35:48.000Z
   myphoto2.jpg	262518	2011-08-08T21:38:01.000Z


.. _S3_Java_Deleting_A_Bucket:

Deleting a Bucket
-----------------

.. note::
   The Bucket must be empty! Otherwise it won't work!

.. code-block:: java

    conn.deleteBucket(bucket.getName());


.. _S3_Java_Forced_Delete_For_Non-Empty_Buckets:

Forced Delete for Non-empty Buckets
-----------------------------------
.. attention::
   not available


.. _S3_Java_Creating_An_Object:

Creating an Object
------------------

This creates a file ``hello.txt`` with the string ``"Hello World!"``

.. code-block:: java

    ByteArrayInputStream input = new ByteArrayInputStream("Hello World!".getBytes());
    conn.putObject(bucket.getName(), "hello.txt", input, new ObjectMetadata());


.. _S3_Java_Change_An_Objects_ACL:

Change an Object's ACL
----------------------

This makes the object ``hello.txt`` to be publicly readable, and
``secret_plans.txt`` to be private.

.. code-block:: java

    conn.setObjectAcl(bucket.getName(), "hello.txt", CannedAccessControlList.PublicRead);
    conn.setObjectAcl(bucket.getName(), "secret_plans.txt", CannedAccessControlList.Private);


.. _S3_Java_Download_An_Object:

Download an Object (to a file)
------------------------------

This downloads the object ``perl_poetry.pdf`` and saves it in
``/home/larry/documents``

.. code-block:: java

    conn.getObject(
            new GetObjectRequest(bucket.getName(), "perl_poetry.pdf"),
            new File("/home/larry/documents/perl_poetry.pdf")
    );


.. _S3_Java_Delete_An_Object:

Delete an Object
----------------

This deletes the object ``goodbye.txt``

.. code-block:: java

    conn.deleteObject(bucket.getName(), "goodbye.txt");


.. _S3_Java_Generate_Object_Download_URLs:

Generate Object Download URLs (signed and unsigned)
---------------------------------------------------

This generates an unsigned download URL for ``hello.txt``. This works
because we made ``hello.txt`` public by setting the ACL above.
This then generates a signed download URL for ``secret_plans.txt`` that
will work for 1 hour. Signed download URLs will work for the time
period even if the object is private (when the time period is up, the
URL will stop working).

.. note::
   The java library does not have a method for generating unsigned
   URLs, so the example below just generates a signed URL.

.. code-block:: java

    GeneratePresignedUrlRequest request = new GeneratePresignedUrlRequest(bucket.getName(), "secret_plans.txt");
    System.out.println(conn.generatePresignedUrl(request));

The output will look something like this::

   https://my-bucket-name.objects.dreamhost.com/secret_plans.txt?Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXX&Expires=1316027075&AWSAccessKeyId=XXXXXXXXXXXXXXXXXXX

.. meta::
    :labels: java S3 api
