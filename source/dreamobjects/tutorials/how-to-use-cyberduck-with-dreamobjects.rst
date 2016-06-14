======================================
How to Use Cyberduck with DreamObjects
======================================

Overview
~~~~~~~~

`Cyberduck <http://cyberduck.io>`_ is  an FTP, SFTP, and WebDav client as well
as a cloud storage browser for Mac and Windows. You can use Cyberduck to
connect to your DreamObjects account.

The following describes how to use Cyberduck to connect to your DreamObjects
account.

How to use Cyberduck with DreamObjects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can set up your DreamObjects connection inside Cyberduck in two ways:

* Semi-automatically by downloading a preconfigured connection profile
  (Recommended).
* Manually by creating a new profile.

Connecting Cyberduck with DreamObjects semi-automatically using a connection profile
------------------------------------------------------------------------------------


1. Download the `DreamObjects Connection Profile
   <http://applications.objects-us-west-1.dream.io/DreamObjects.cyberduckprofile>`_.
2. Once it's downloaded, double-click the file to open Cyberduck and then
   create a new DreamObjects bookmark.
3. Give your bookmark a nickname and close the window to save it.

    .. figure:: images/cyberduck/auto_01.png

4. Double-click on your newly created bookmark and enter the Access Key and
   Secret Key for the DreamObjects user/buckets to which you wish to connect.

    * If you are using a Mac, the 'Add to Keychain' option appears. If you
      choose to save your credentials, you won't be prompted to enter them
      again.

    .. figure:: images/cyberduck/cyberduck_creds.png

5. Upon successful connection, your buckets appear listed as drives in the
   interface.

    .. figure:: images/cyberduck/cyberduck_buckets.png

Connecting to Cyberduck manually
--------------------------------

1. Open Cyberduck and create a new bookmark.

    .. figure:: images/cyberduck/manual_01.png

2. Click the connection menu, and then select 'S3 (Amazon Simple Storage
   Service)' from the protocol drop down list.

    .. figure:: images/cyberduck/manual_02.png

3. Give your bookmark a nickname and enter the following:
    * **Server**: objects-us-west-1.dream.io
    * **Access Key ID**: enter the Access Key for the DreamObjects user/buckets
      to which you wish to connect, and then close the window to save the
      connection settings.

    .. figure:: images/cyberduck/manual_03.png

4. Double-click on your newly created bookmark and enter the Secret Key for
   the DreamObjects user/buckets to which you wish to connect.

    * If you are using a Mac, the 'Add to Keychain' option appears. If you
      choose to save your credentials, you won't be prompted to enter them
      again.

    .. figure:: images/cyberduck/cyberduck_creds.png

5. Upon successful connection, your buckets appear listed as drives in the
   interface.

    .. figure:: images/cyberduck/cyberduck_buckets.png

Managing DreamObjects data using Cyberduck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cyberduck makes it very simple to manage your data. Once you've connected to
DreamObjects, simply click and drag files and folders to and from Cyberduck.

    *When uploading or downloading files, a transfer window appears:*

    .. figure:: images/cyberduck/cyberduck_transfer.png

.. meta::
    :labels: cyberduck
