Sample C# Code Using DreamObjects S3-compatible API
===================================================

.. container:: table_of_content

    - :ref:`S3_C#_Creating_A_Connection`
    - :ref:`S3_C#_Listing_Owned_Buckets`
    - :ref:`S3_C#_Creating_A_Buckets`
    - :ref:`S3_C#_Listing_A_Buckets_Content`
    - :ref:`S3_C#_Deleting_A_Bucket`
    - :ref:`S3_C#_Forced_Delete_For_Non-Empty_Buckets`
    - :ref:`S3_C#_Creating_An_Objects`
    - :ref:`S3_C#_Change_An_Objects_ACL`
    - :ref:`S3_C#_Download_An_Object`
    - :ref:`S3_C#_Delete_An_Object`
    - :ref:`S3_C#_Generate_Object_Download_URLs`


.. _S3_C#_Creating_A_Connection:

Creating a Connection
---------------------

This creates a connection so that you can interact with the server.

.. code-block:: csharp

    using System;
    using Amazon;
    using Amazon.S3;
    using Amazon.S3.Model;

    string accessKey = "put your access key here!";
    string secretKey = "put your secret key here!";

    AmazonS3Config config = new AmazonS3Config();
    config.ServiceURL = "objects.dreamhost.com";

    AmazonS3 client = Amazon.AWSClientFactory.CreateAmazonS3Client(
            accessKey,
            secretKey,
            config
            );


.. _S3_C#_Listing_Owned_Buckets:

Listing Owned Buckets
---------------------

This gets a list of Buckets that you own.
This also prints out the bucket name and creation date of each bucket.

.. code-block:: csharp

    ListBucketResponse response = client.ListBuckets();
    foreach (S3Bucket b in response.Buckets)
    {
            Console.WriteLine("{0}\t{1}", b.BucketName, b.CreationDate);
    }

The output will look something like this::

   mahbuckat1	2011-04-21T18:05:39.000Z
   mahbuckat2	2011-04-21T18:05:48.000Z
   mahbuckat3	2011-04-21T18:07:18.000Z


.. _S3_C#_Creating_A_Buckets:

Creating a Bucket
-----------------
This creates a new bucket called ``my-new-bucket``

.. code-block:: csharp

    PutBucketRequest request = new PutBucketRequest();
    request.BucketName = "my-new-bucket";
    client.PutBucket(request);


.. _S3_C#_Listing_A_Buckets_Content:

Listing a Bucket's Content
--------------------------

This gets a list of objects in the bucket.
This also prints out each object's name, the file size, and last
modified date.

.. code-block:: csharp

    ListObjectsRequest request = new ListObjectsRequest();
    request.BucketName = "my-new-bucket";
    ListObjectsResponse response = client.ListObjects(request);
    foreach (S3Object o in response.S3Objects)
    {
            Console.WriteLine("{0}\t{1}\t{2}", o.Key, o.Size, o.LastModified);
    }

The output will look something like this::

   myphoto1.jpg	251262	2011-08-08T21:35:48.000Z
   myphoto2.jpg	262518	2011-08-08T21:38:01.000Z


.. _S3_C#_Deleting_A_Bucket:

Deleting a Bucket
-----------------

.. note::

   The Bucket must be empty! Otherwise it won't work!

.. code-block:: csharp

    DeleteBucketRequest request = new DeleteBucketRequest();
    request.BucketName = "my-new-bucket";
    client.DeleteBucket(request);


.. _S3_C#_Forced_Delete_For_Non-Empty_Buckets:

Forced Delete for Non-empty Buckets
-----------------------------------

.. attention::

   not available


.. _S3_C#_Creating_An_Objects:

Creating an Object
------------------

This creates a file ``hello.txt`` with the string ``"Hello World!"``

.. code-block:: csharp

    PutObjectRequest request = new PutObjectRequest();
    request.Bucket      = "my-new-bucket";
    request.Key         = "hello.txt";
    request.ContentType = "text/plain";
    request.ContentBody = "Hello World!";
    client.PutObject(request);


.. _S3_C#_Change_An_Objects_ACL:

Change an Object's ACL
----------------------

This makes the object ``hello.txt`` to be publicly readable, and
``secret_plans.txt`` to be private.

.. code-block:: csharp

    SetACLRequest request = new SetACLRequest();
    request.BucketName = "my-new-bucket";
    request.Key        = "hello.txt";
    request.CannedACL  = S3CannedACL.PublicRead;
    client.SetACL(request);

    SetACLRequest request2 = new SetACLRequest();
    request2.BucketName = "my-new-bucket";
    request2.Key        = "secret_plans.txt";
    request2.CannedACL  = S3CannedACL.Private;
    client.SetACL(request2);


.. _S3_C#_Download_An_Object:

Download an Object (to a file)
------------------------------

This downloads the object ``perl_poetry.pdf`` and saves it in
``C:\Users\larry\Documents``

.. code-block:: csharp

    GetObjectRequest request = new GetObjectRequest();
    request.BucketName = "my-new-bucket";
    request.Key        = "perl_poetry.pdf"
    GetObjectResponse response = client.GetObject(request);
    response.WriteResponseStreamToFile("C:\\Users\\larry\\Documents\\perl_poetry.pdf");


.. _S3_C#_Delete_An_Object:

Delete an Object
----------------

This deletes the object ``goodbye.txt``

.. code-block:: csharp

    DeleteObjectRequest request = new DeleteObjectRequest();
    request.BucketName = "my-new-bucket";
    request.Key        = "goodbye.txt";
    client.DeleteObject(request);


.. _S3_C#_Generate_Object_Download_URLs:

Generate Object Download URLs (signed and unsigned)
---------------------------------------------------

This generates an unsigned download URL for ``hello.txt``. This works
because we made ``hello.txt`` public by setting the ACL above.
This then generates a signed download URL for ``secret_plans.txt`` that
will work for 1 hour. Signed download URLs will work for the time
period even if the object is private (when the time period is up, the
URL will stop working).

.. note::

   The C# S3 Library does not have a method for generating unsigned
   URLs, so the following example only shows generating signed URLs.

.. code-block:: csharp

    GetPreSignedUrlRequest request = new GetPreSignedUrlRequest();
    request.BucketName = "my-bucket-name";
    request.Key        = "secret_plans.txt";
    request.Expires    = DateTime.Now.AddHours(1);
    request.Protocol   = Protocol.HTTP;
    string url = client.GetPreSignedURL(request);
    Console.WriteLine(url);

The output of this will look something like::

   http://objects.dreamhost.com/my-bucket-name/secret_plans.txt?Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXX&Expires=1316027075&AWSAccessKeyId=XXXXXXXXXXXXXXXXXXX

.. meta::
    :labels: C# S3
