How to use DreamObjects S3-compatible API with various SDKs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Use C++ with DreamObjects S3-compatible API
===========================================

Setup
-----

The following contains includes and globals that will be used in later examples:

.. code-block:: cpp

    #include "libs3.h"
    #include <stdlib.h>
    #include <iostream>
    #include <fstream>

    const char access_key[] = "ACCESS_KEY";
    const char secret_key[] = "SECRET_KEY";
    const char host[] = "HOST";
    const char sample_bucket[] = "sample_bucket";
    const char sample_key[] = "hello.txt";
    const char sample_file[] = "resource/hello.txt";

    S3BucketContext bucketContext =
    {
            host,
            sample_bucket,
            S3ProtocolHTTP,
            S3UriStylePath,
            access_key,
            secret_key
    };

    S3Status responsePropertiesCallback(
                    const S3ResponseProperties *properties,
                    void *callbackData)
    {
            return S3StatusOK;
    }

    static void responseCompleteCallback(
                    S3Status status,
                    const S3ErrorDetails *error,
                    void *callbackData)
    {
            return;
    }

    S3ResponseHandler responseHandler =
    {
            &responsePropertiesCallback,
            &responseCompleteCallback
    };


Creating (and Closing) a Connection
-----------------------------------

This creates a connection so that you can interact with the server.

.. code-block:: cpp

    S3_initialize("s3", S3_INIT_ALL, host);
    // Do stuff...
    S3_deinitialize();


Listing Owned Buckets
---------------------

This gets a list of Buckets that you own.
This also prints out the bucket name, owner ID, and display name
for each bucket.

.. code-block:: cpp

    static S3Status listServiceCallback(
                    const char *ownerId,
                    const char *ownerDisplayName,
                    const char *bucketName,
                    int64_t creationDate, void *callbackData)
    {
            bool *header_printed = (bool*) callbackData;
            if (!*header_printed) {
                    *header_printed = true;
                    printf("%-22s", "       Bucket");
                    printf("  %-20s  %-12s", "     Owner ID", "Display Name");
                    printf("\n");
                    printf("----------------------");
                    printf("  --------------------" "  ------------");
                    printf("\n");
            }

            printf("%-22s", bucketName);
            printf("  %-20s  %-12s", ownerId ? ownerId : "", ownerDisplayName ? ownerDisplayName : "");
            printf("\n");

            return S3StatusOK;
    }

    S3ListServiceHandler listServiceHandler =
    {
            responseHandler,
            &listServiceCallback
    };
    bool header_printed = false;
    S3_list_service(S3ProtocolHTTP, access_key, secret_key, host, 0, &listServiceHandler, &header_printed);


Creating a Bucket
-----------------

This creates a new bucket.

.. code-block:: cpp

    S3_create_bucket(S3ProtocolHTTP, access_key, secret_key, host, sample_bucket, S3CannedAclPrivate, NULL, NULL, &responseHandler, NULL);


Listing a Bucket's Content
--------------------------

This gets a list of objects in the bucket.
This also prints out each object's name, the file size, and
last modified date.

.. code-block:: cpp

    static S3Status listBucketCallback(
                    int isTruncated,
                    const char *nextMarker,
                    int contentsCount,
                    const S3ListBucketContent *contents,
                    int commonPrefixesCount,
                    const char **commonPrefixes,
                    void *callbackData)
    {
            printf("%-22s",	"      Object Name");
            printf("  %-5s  %-20s", "Size", "   Last Modified");
            printf("\n");
            printf("----------------------");
            printf("  -----" "  --------------------");
            printf("\n");

        for (int i = 0; i < contentsCount; i++) {
            char timebuf[256];
                    char sizebuf[16];
            const S3ListBucketContent *content = &(contents[i]);
                    time_t t = (time_t) content->lastModified;

                    strftime(timebuf, sizeof(timebuf), "%Y-%m-%dT%H:%M:%SZ", gmtime(&t));
                    sprintf(sizebuf, "%5llu", (unsigned long long) content->size);
                    printf("%-22s  %s  %s\n", content->key, sizebuf, timebuf);
        }

        return S3StatusOK;
    }

    S3ListBucketHandler listBucketHandler =
    {
            responseHandler,
            &listBucketCallback
    };
    S3_list_bucket(&bucketContext, NULL, NULL, NULL, 0, NULL, &listBucketHandler, NULL);

The output will look something like this::

   myphoto1.jpg	251262	2011-08-08T21:35:48.000Z
   myphoto2.jpg	262518	2011-08-08T21:38:01.000Z


Deleting a Bucket
-----------------

.. note::

   The Bucket must be empty! Otherwise it won't work!

.. code-block:: cpp

    S3_delete_bucket(S3ProtocolHTTP, S3UriStylePath, access_key, secret_key, host, sample_bucket, NULL, &responseHandler, NULL);


Creating an Object (from a file)
--------------------------------

This creates a file ``hello.txt``.

.. code-block:: cpp

    #include <sys/stat.h>
    typedef struct put_object_callback_data
    {
        FILE *infile;
        uint64_t contentLength;
    } put_object_callback_data;


    static int putObjectDataCallback(int bufferSize, char *buffer, void *callbackData)
    {
        put_object_callback_data *data = (put_object_callback_data *) callbackData;

        int ret = 0;

        if (data->contentLength) {
            int toRead = ((data->contentLength > (unsigned) bufferSize) ? (unsigned) bufferSize : data->contentLength);
                    ret = fread(buffer, 1, toRead, data->infile);
        }
        data->contentLength -= ret;
        return ret;
    }

    put_object_callback_data data;
    struct stat statbuf;
    if (stat(sample_file, &statbuf) == -1) {
            fprintf(stderr, "\nERROR: Failed to stat file %s: ", sample_file);
            perror(0);
            exit(-1);
    }

    int contentLength = statbuf.st_size;
    data.contentLength = contentLength;

    if (!(data.infile = fopen(sample_file, "r"))) {
            fprintf(stderr, "\nERROR: Failed to open input file %s: ", sample_file);
            perror(0);
            exit(-1);
    }

    S3PutObjectHandler putObjectHandler =
    {
            responseHandler,
            &putObjectDataCallback
    };

    S3_put_object(&bucketContext, sample_key, contentLength, NULL, NULL, &putObjectHandler, &data);


Download an Object (to a file)
------------------------------

This downloads a file and prints the contents.

.. code-block:: cpp

    static S3Status getObjectDataCallback(int bufferSize, const char *buffer, void *callbackData)
    {
            FILE *outfile = (FILE *) callbackData;
            size_t wrote = fwrite(buffer, 1, bufferSize, outfile);
            return ((wrote < (size_t) bufferSize) ? S3StatusAbortedByCallback : S3StatusOK);
    }

    S3GetObjectHandler getObjectHandler =
    {
            responseHandler,
            &getObjectDataCallback
    };
    FILE *outfile = stdout;
    S3_get_object(&bucketContext, sample_key, NULL, 0, 0, NULL, &getObjectHandler, outfile);


Delete an Object
----------------

This deletes an object.

.. code-block:: cpp

    S3ResponseHandler deleteResponseHandler =
    {
            0,
            &responseCompleteCallback
    };
    S3_delete_object(&bucketContext, sample_key, 0, &deleteResponseHandler, 0);


Change an Object's ACL
----------------------

This changes an object's ACL to grant full control to another user.


.. code-block:: cpp

    #include <string.h>
    char ownerId[] = "owner";
    char ownerDisplayName[] = "owner";
    char granteeId[] = "grantee";
    char granteeDisplayName[] = "grantee";

    S3AclGrant grants[] = {
            {
                    S3GranteeTypeCanonicalUser,
                    {{}},
                    S3PermissionFullControl
            },
            {
                    S3GranteeTypeCanonicalUser,
                    {{}},
                    S3PermissionReadACP
            },
            {
                    S3GranteeTypeAllUsers,
                    {{}},
                    S3PermissionRead
            }
    };

    strncpy(grants[0].grantee.canonicalUser.id, ownerId, S3_MAX_GRANTEE_USER_ID_SIZE);
    strncpy(grants[0].grantee.canonicalUser.displayName, ownerDisplayName, S3_MAX_GRANTEE_DISPLAY_NAME_SIZE);

    strncpy(grants[1].grantee.canonicalUser.id, granteeId, S3_MAX_GRANTEE_USER_ID_SIZE);
    strncpy(grants[1].grantee.canonicalUser.displayName, granteeDisplayName, S3_MAX_GRANTEE_DISPLAY_NAME_SIZE);

    S3_set_acl(&bucketContext, sample_key, ownerId, ownerDisplayName, 3, grants, 0, &responseHandler, 0);


Generate Object Download URL (signed)
-------------------------------------

This generates a signed download URL that will be valid for 5 minutes.

.. code-block:: cpp

    #include <time.h>
    char buffer[S3_MAX_AUTHENTICATED_QUERY_STRING_SIZE];
    int64_t expires = time(NULL) + 60 * 5; // Current time + 5 minutes

    S3_generate_authenticated_query_string(buffer, &bucketContext, sample_key, expires, NULL);

Use C# with DreamObjects S3-compatible API
==========================================

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


Creating a Bucket
-----------------
This creates a new bucket called ``my-new-bucket``

.. code-block:: csharp

    PutBucketRequest request = new PutBucketRequest();
    request.BucketName = "my-new-bucket";
    client.PutBucket(request);

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


Deleting a Bucket
-----------------

.. note::

   The Bucket must be empty! Otherwise it won't work!

.. code-block:: csharp

    DeleteBucketRequest request = new DeleteBucketRequest();
    request.BucketName = "my-new-bucket";
    client.DeleteBucket(request);


Forced Delete for Non-empty Buckets
-----------------------------------

.. attention::

   not available


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


Delete an Object
----------------

This deletes the object ``goodbye.txt``

.. code-block:: csharp

    DeleteObjectRequest request = new DeleteObjectRequest();
    request.BucketName = "my-new-bucket";
    request.Key        = "goodbye.txt";
    client.DeleteObject(request);


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

Use Java with DreamObjects S3-compatible API
============================================

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


Creating a Connection
---------------------

This creates a connection so that you can interact with the server.

.. code-block:: java

    String accessKey = "insert your access key here!";
    String secretKey = "insert your secret key here!";

    AWSCredentials credentials = new BasicAWSCredentials(accessKey, secretKey);
    AmazonS3 conn = new AmazonS3Client(credentials);
    conn.setEndpoint("objects.dreamhost.com");


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


Creating a Bucket
-----------------

This creates a new bucket called ``my-new-bucket``

.. code-block:: java

    Bucket bucket = conn.createBucket("my-new-bucket");


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


Deleting a Bucket
-----------------

.. note::
   The Bucket must be empty! Otherwise it won't work!

.. code-block:: java

    conn.deleteBucket(bucket.getName());


Forced Delete for Non-empty Buckets
-----------------------------------
.. attention::
   not available


Creating an Object
------------------

This creates a file ``hello.txt`` with the string ``"Hello World!"``

.. code-block:: java

    ByteArrayInputStream input = new ByteArrayInputStream("Hello World!".getBytes());
    conn.putObject(bucket.getName(), "hello.txt", input, new ObjectMetadata());


Change an Object's ACL
----------------------

This makes the object ``hello.txt`` to be publicly readable, and
``secret_plans.txt`` to be private.

.. code-block:: java

    conn.setObjectAcl(bucket.getName(), "hello.txt", CannedAccessControlList.PublicRead);
    conn.setObjectAcl(bucket.getName(), "secret_plans.txt", CannedAccessControlList.Private);


Download an Object (to a file)
------------------------------

This downloads the object ``perl_poetry.pdf`` and saves it in
``/home/larry/documents``

.. code-block:: java

    conn.getObject(
            new GetObjectRequest(bucket.getName(), "perl_poetry.pdf"),
            new File("/home/larry/documents/perl_poetry.pdf")
    );


Delete an Object
----------------

This deletes the object ``goodbye.txt``

.. code-block:: java

    conn.deleteObject(bucket.getName(), "goodbye.txt");


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


Use Perl with DreamObjects S3-compatible API
============================================

Creating a Connection
---------------------

This creates a connection so that you can interact with the server.

.. code-block:: perl

    use Amazon::S3;
    my $access_key = 'put your access key here!';
    my $secret_key = 'put your secret key here!';

    my $conn = Amazon::S3->new({
            aws_access_key_id     => $access_key,
            aws_secret_access_key => $secret_key,
            host                  => 'objects.dreamhost.com',
            secure                => 1,
            retry                 => 1,
    });


Listing Owned Buckets
---------------------

This gets a list of `Amazon::S3::Bucket`_ objects that you own.
We'll also print out the bucket name and creation date of each bucket.

.. code-block:: perl

    my @buckets = @{$conn->buckets->{buckets} || []};
    foreach my $bucket (@buckets) {
            print $bucket->bucket . "\t" . $bucket->creation_date . "\n";
    }

The output will look something like this::

   mahbuckat1	2011-04-21T18:05:39.000Z
   mahbuckat2	2011-04-21T18:05:48.000Z
   mahbuckat3	2011-04-21T18:07:18.000Z


Creating a Bucket
-----------------

This creates a new bucket called ``my-new-bucket``

.. code-block:: perl

    my $bucket = $conn->add_bucket({ bucket => 'my-new-bucket' });


Listing a Bucket's Content
--------------------------

This gets a list of hashes with info about each object in the bucket.
We'll also print out each object's name, the file size, and last
modified date.

.. code-block:: perl

    my @keys = @{$bucket->list_all->{keys} || []};
    foreach my $key (@keys) {
            print "$key->{key}\t$key->{size}\t$key->{last_modified}\n";
    }

The output will look something like this::

   myphoto1.jpg	251262	2011-08-08T21:35:48.000Z
   myphoto2.jpg	262518	2011-08-08T21:38:01.000Z


Deleting a Bucket
-----------------

.. note::
   The Bucket must be empty! Otherwise it won't work!

.. code-block:: perl

    $conn->delete_bucket($bucket);


Forced Delete for Non-empty Buckets
-----------------------------------

.. attention::

   not available in the `Amazon::S3`_ perl module


Creating an Object
------------------

This creates a file ``hello.txt`` with the string ``"Hello World!"``

.. code-block:: perl

    $bucket->add_key(
            'hello.txt', 'Hello World!',
            { content_type => 'text/plain' },
    );

Change an Object's ACL
----------------------

This makes the object ``hello.txt`` to be publicly readable and
``secret_plans.txt`` to be private.

.. code-block:: perl

    $bucket->set_acl({
            key       => 'hello.txt',
            acl_short => 'public-read',
    });
    $bucket->set_acl({
            key       => 'secret_plans.txt',
            acl_short => 'private',
    });


Download an Object (to a file)
------------------------------

This downloads the object ``perl_poetry.pdf`` and saves it in
``/home/larry/documents/``

.. code-block:: perl

    $bucket->get_key_filename('perl_poetry.pdf', undef,
            '/home/larry/documents/perl_poetry.pdf');


Delete an Object
----------------

This deletes the object ``goodbye.txt``

.. code-block:: perl

    $bucket->delete_key('goodbye.txt');

Generate Object Download URLs (signed and unsigned)
---------------------------------------------------
This generates an unsigned download URL for ``hello.txt``. This works
because we made ``hello.txt`` public by setting the ACL above.
Then this generates a signed download URL for ``secret_plans.txt`` that
will work for 1 hour. Signed download URLs will work for the time
period even if the object is private (when the time period is up, the
URL will stop working).

.. note::
   The `Amazon::S3`_ module does not have a way to generate download
   URLs, so we're going to be using another module instead. Unfortunately,
   most modules for generating these URLs assume that you are using Amazon,
   so we've had to go with using a more obscure module, `Muck::FS::S3`_. This
   should be the same as Amazon's sample S3 perl module, but this sample
   module is not in CPAN. So, you can either use CPAN to install
   `Muck::FS::S3`_, or install Amazon's sample S3 module manually. If you go
   the manual route, you can remove ``Muck::FS::`` from the example below.

.. code-block:: perl

    use Muck::FS::S3::QueryStringAuthGenerator;
    my $generator = Muck::FS::S3::QueryStringAuthGenerator->new(
            $access_key,
            $secret_key,
            0, # 0 means use 'http'. set this to 1 for 'https'
            'objects.dreamhost.com',
    );

    my $hello_url = $generator->make_bare_url($bucket->bucket, 'hello.txt');
    print $hello_url . "\n";

    $generator->expires_in(3600); # 1 hour = 3600 seconds
    my $plans_url = $generator->get($bucket->bucket, 'secret_plans.txt');
    print $plans_url . "\n";

The output will look something like this::

   http://objects.dreamhost.com:80/my-bucket-name/hello.txt
   http://objects.dreamhost.com:80/my-bucket-name/secret_plans.txt?Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXX&Expires=1316027075&AWSAccessKeyId=XXXXXXXXXXXXXXXXXXX


.. _`Amazon::S3`: http://search.cpan.org/~tima/Amazon-S3-0.441/lib/Amazon/S3.pm
.. _`Amazon::S3::Bucket`: http://search.cpan.org/~tima/Amazon-S3-0.441/lib/Amazon/S3/Bucket.pm
.. _`Muck::FS::S3`: http://search.cpan.org/~mike/Muck-0.02/

Use PHP with DreamObjects S3-compatible API
===========================================

.. note::

    This library can be obtained in from Amazon as a `zip file <http://pear.amazonwebservices.com/get/aws.zip>`_
    or from `github <https://github.com/aws/aws-sdk-php>`_.  The
    examples in this guide have been tested against version 2.4.5
    obtained from a zip file. The AWS SDK for PHP 2 requires PHP
    5.3.3+.  The complete API reference is available on the
    `Amazon <http://docs.aws.amazon.com/aws-sdk-php-2/latest/class-Aws.S3.S3Client.html>`_
    site.

Creating a Connection
---------------------

Create an S3 client object to interact with the DHO server.

.. code-block:: php

    <?php
    define('AWS_KEY', 'place access key here');
    define('AWS_SECRET_KEY', 'place secret key here');
    define('HOST', 'https://objects.dreamhost.com');

    // require the AWS SDK for PHP library
    require 'aws-autoloader.php';

    use Aws\S3\S3Client;

    // Establish connection with DreamObjects with an S3 client.
    $client = S3Client::factory(array(
        'base_url' => HOST,
        'key'      => AWS_KEY,
        'secret'   => AWS_SECRET_KEY
    ));


Listing Owned Buckets
---------------------

List buckets owned by the S3 user.

.. code-block:: php

    <?php
    $blist = $client->listBuckets();
    echo "   Buckets belonging to " . $blist['Owner']['ID'] . ":\n";
    foreach ($blist['Buckets'] as $b) {
        echo "{$b['Name']}\t{$b['CreationDate']}\n";
    }

The output will look something like this::

   Buckets belonging to happydhouser:
   mahbuckat1	2011-04-21T18:05:39.000Z
   mahbuckat2	2011-04-21T18:05:48.000Z
   mahbuckat3	2011-04-21T18:07:18.000Z

Creating a Bucket
-----------------

.. code-block:: php

    <?php
    $client->createBucket(array('Bucket' => 'my-new-bucket'));

.. note::
   The library is somewhat inconsistent in its validation of
   permissible bucket names.  Typically the command will reject
   bucket names not safe to use as a subdomain, but does allow
   "_" underscores. Sticking to DNS-safe names is generally the
   best practice.

List a Bucket's Content
-----------------------

Here we request an object iterator and loop over it to retrieve
the desired information about the objects (object key, size,
and modification time stamp in this case).

.. code-block:: php

    <?php
    $o_iter = $client->getIterator('ListObjects', array(
        'Bucket' => $bucketname
    ));
    foreach ($o_iter as $o) {
        echo "{$o['Key']}\t{$o['Size']}\t{$o['LastModified']}\n";
    }

The output will look something like this if the bucket has some files::

   myphoto1.jpg	251262	2011-08-08T21:35:48.000Z
   myphoto2.jpg	262518	2011-08-08T21:38:01.000Z


Deleting a Bucket
-----------------

.. note::

   The Bucket must be empty! Otherwise it won't work!

.. code-block:: php

    <?php
    $client->deleteBucket(array('Bucket' => $new_bucket));

    // optionally, you can wait until the bucket is deleted
    $client->waitUntilBucketNotExists(array('Bucket' => $new_bucket));


Forced Delete for Non-empty Buckets
-----------------------------------

.. attention::

    This feature is not currently supported.


Creating an Object
-------------------

This uploads a file from the filesystem and sets it to be private.

.. code-block:: php

    <?php
    $key         = 'hello.txt';
    $source_file = './hello.txt';
    $acl         = 'private';
    $bucket      = 'my-bucket-name';
    $client->upload($bucket, $key, fopen($source_file, 'r'), $acl);


Change an Object's ACL
----------------------

This changes the availability of the object ``hello.txt`` to be
publicly readable, and object ``secret_plans.txt`` to be private.

.. code-block:: php

    <?php
    $client->putObjectAcl(array(
        'Bucket' => 'my-bucket-name',
        'Key'    => 'hello.txt',
        'ACL'    => 'public-read'
    ));
    $client->putObjectAcl(array(
        'Bucket' => 'my-bucket-name',
        'Key'    => 'secret_plans.txt',
        'ACL'    => 'private'
    ));

.. note::

   'ACL' can be one of: private, public-read, public-read-write, authenticated-read,
   bucket-owner-read, bucket-owner-full-control; `full reference
   <http://docs.aws.amazon.com/aws-sdk-php-2/latest/class-Aws.S3.S3Client.html#_putObjectAcl>`_.

Delete an Object
----------------

This deletes the object ``goodbye.txt``

.. code-block:: php

    <?php
    $client->deleteObject(array(
        'Bucket' => 'my-bucket-name',
        'Key'    => 'goodbye.txt',
    ));


Download an Object (to a file)
------------------------------

This downloads the object ``poetry.pdf`` from 'my-bucket-name' and saves it
in ``/home/larry/documents``

.. code-block:: php

    <?php
    $client->getObject(array(
        'Bucket' => 'my-bucket-name',
        'Key'    => 'poetry.pdf',
        'SaveAs' => '/home/larry/documents/poetry.pdf'
    ));


Generate Object Download URLs (signed and unsigned)
---------------------------------------------------

This generates an unsigned download URL for ``hello.txt``.
This works because we made ``hello.txt`` public by setting
the ACL above. This then generates a signed download URL
for ``secret_plans.txt`` that will work for 1 hour.
Signed download URLs will work for the time period even
if the object is private (when the time period is up,
the URL will stop working).

.. code-block:: php

    <?php
    $plain_url = $client->getObjectUrl('my-bucket-name', 'hello.txt');
    echo $plain_url . "\n";
    $signed_url = $client->getObjectUrl('my-bucket-name', 'secret_plans.txt', '+1 hour');
    echo $signed_url . "\n";

The output of this will look something like:::

   http://my-bucket-name.objects.dreamhost.com/hello.txt
   http://my-bucket-name.objects.dreamhost.com/secret_plans.txt?Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXX&Expires=1316027075&AWSAccessKeyId=XXXXXXXXXXXXXXXXXXX

Use Python and Boto with DreamObjects S3-compatible API
=======================================================

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
            host = 'objects.dreamhost.com',
            calling_format = boto.s3.connection.OrdinaryCallingFormat(),
            )


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


Creating a Bucket
-----------------

This creates a new bucket called ``my-new-bucket``

.. code-block:: python

    bucket = conn.create_bucket('my-new-bucket')


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


Deleting a Bucket
-----------------

.. note::

   The Bucket must be empty! Otherwise it won't work!

.. code-block:: python

    conn.delete_bucket(bucket.name)


Forced Delete for Non-empty Buckets
-----------------------------------

.. attention::

   not available in python


Creating an Object
------------------

This creates a file ``hello.txt`` with the string ``"Hello World!"``

.. code-block:: python

    key = bucket.new_key('hello.txt')
    key.set_contents_from_string('Hello World!')


Change an Object's ACL
----------------------

This makes the object ``hello.txt`` to be publicly readable, and
``secret_plans.txt`` to be private.

.. code-block:: python

    hello_key = bucket.get_key('hello.txt')
    hello_key.set_canned_acl('public-read')
    plans_key = bucket.get_key('secret_plans.txt')
    plans_key.set_canned_acl('private')


Download an Object (to a file)
------------------------------

This downloads the object ``perl_poetry.pdf`` and saves it in
``/home/larry/documents/``

.. code-block:: python

    key = bucket.get_key('perl_poetry.pdf')
    key.get_contents_to_filename('/home/larry/documents/perl_poetry.pdf')


Delete an Object
----------------

This deletes the object ``goodbye.txt``

.. code-block:: python

    bucket.delete_key('goodbye.txt')


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

   http://objects.dreamhost.com/my-bucket-name/hello.txt
   http://objects.dreamhost.com/my-bucket-name/secret_plans.txt?Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXX&Expires=1316027075&AWSAccessKeyId=XXXXXXXXXXXXXXXXXXX

Use Ruby with DreamObjects S3-compatible API
============================================

Creating a Connection
---------------------

This creates a connection so that you can interact with the server.

.. code-block:: ruby

    AWS::S3::Base.establish_connection!(
            :server            => 'objects.dreamhost.com',
            :use_ssl           => true,
            :access_key_id     => 'my-access-key',
            :secret_access_key => 'my-secret-key'
    )


Listing Owned Buckets
---------------------

This gets a list of `AWS::S3::Bucket`_ objects that you own.
This also prints out the bucket name and creation date of each bucket.

.. code-block:: ruby

    AWS::S3::Service.buckets.each do |bucket|
            puts "#{bucket.name}\t#{bucket.creation_date}"
    end

The output will look something like this::

   mahbuckat1	2011-04-21T18:05:39.000Z
   mahbuckat2	2011-04-21T18:05:48.000Z
   mahbuckat3	2011-04-21T18:07:18.000Z


Creating a Bucket
-----------------

This creates a new bucket called ``my-new-bucket``

.. code-block:: ruby

    AWS::S3::Bucket.create('my-new-bucket')


Listing a Bucket's Content
--------------------------

This gets a list of hashes with the contents of each object
This also prints out each object's name, the file size, and last
modified date.

.. code-block:: ruby

    new_bucket = AWS::S3::Bucket.find('my-new-bucket')
    new_bucket.each do |object|
            puts "#{object.key}\t#{object.about['content-length']}\t#{object.about['last-modified']}"
    end

The output will look something like this if the bucket has some files::

   myphoto1.jpg	251262	2011-08-08T21:35:48.000Z
   myphoto2.jpg	262518	2011-08-08T21:38:01.000Z


Deleting a Bucket
-----------------
.. note::
   The Bucket must be empty! Otherwise it won't work!

.. code-block:: ruby

    AWS::S3::Bucket.delete('my-new-bucket')


Forced Delete for Non-empty Buckets
-----------------------------------

.. code-block:: ruby

    AWS::S3::Bucket.delete('my-new-bucket', :force => true)


Creating an Object
------------------

This creates a file ``hello.txt`` with the string ``"Hello World!"``

.. code-block:: ruby

    AWS::S3::S3Object.store(
            'hello.txt',
            'Hello World!',
            'my-new-bucket',
            :content_type => 'text/plain'
    )


Change an Object's ACL
----------------------

This makes the object ``hello.txt`` to be publicly readable, and ``secret_plans.txt``
to be private.

.. code-block:: ruby

    policy = AWS::S3::S3Object.acl('hello.txt', 'my-new-bucket')
    policy.grants = [ AWS::S3::ACL::Grant.grant(:public_read) ]
    AWS::S3::S3Object.acl('hello.txt', 'my-new-bucket', policy)

    policy = AWS::S3::S3Object.acl('secret_plans.txt', 'my-new-bucket')
    policy.grants = []
    AWS::S3::S3Object.acl('secret_plans.txt', 'my-new-bucket', policy)


Download an Object (to a file)
------------------------------

This downloads the object ``poetry.pdf`` and saves it in
``/home/larry/documents/``

.. code-block:: ruby

    open('/home/larry/documents/poetry.pdf', 'w') do |file|
            AWS::S3::S3Object.stream('poetry.pdf', 'my-new-bucket') do |chunk|
                    file.write(chunk)
            end
    end


Delete an Object
----------------

This deletes the object ``goodbye.txt``

.. code-block:: ruby

    AWS::S3::S3Object.delete('goodbye.txt', 'my-new-bucket')


Generate Object Download URLs (signed and unsigned)
---------------------------------------------------

This generates an unsigned download URL for ``hello.txt``. This works
because we made ``hello.txt`` public by setting the ACL above.
This then generates a signed download URL for ``secret_plans.txt`` that
will work for 1 hour. Signed download URLs will work for the time
period even if the object is private (when the time period is up, the
URL will stop working).

.. code-block:: ruby

    puts AWS::S3::S3Object.url_for(
            'hello.txt',
            'my-new-bucket',
            :authenticated => false
    )

    puts AWS::S3::S3Object.url_for(
            'secret_plans.txt',
            'my-new-bucket',
            :expires_in => 60 * 60
    )

The output of this will look something like::

   http://objects.dreamhost.com/my-bucket-name/hello.txt
   http://objects.dreamhost.com/my-bucket-name/secret_plans.txt?Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXX&Expires=1316027075&AWSAccessKeyId=XXXXXXXXXXXXXXXXXXX

.. _`AWS::S3`: http://amazon.rubyforge.org/
.. _`AWS::S3::Bucket`: http://amazon.rubyforge.org/doc/

.. meta::
    :labels: ruby python perl c++ C# php S3 api
