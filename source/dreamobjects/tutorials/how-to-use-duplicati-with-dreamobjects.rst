======================================
How to Use Duplicati with DreamObjects
======================================

Overview
~~~~~~~~

.. figure:: images/duplicati.png

`Duplicati <http://www.duplicati.com>`_ is a free backup client that
securely stores encrypted, incremental, compressed backups on cloud-storage
services and remote-file servers. It works with Linux, Mac, and Windows.

Duplicati has built-in AES-256 encryption and backups can be signed using GNU
Privacy Guard. A built-in scheduler ensures that backups are always
up-to-date. The Duplicati project was inspired by `duplicity
<http://duplicity.nongnu.org>`_, and while similar, they are not compatible.

Setting up Duplicati with DreamObjects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Launch Duplicati.
    *The following options appear when first setting up Duplicati:*

    .. figure:: images/duplicati/01_Duplicati.png

2. Select the ‘Setup a new backup’ option.

    .. figure:: images/duplicati/02_Duplicati.png

3. Enter a backup name, and then click the **Next** button.

    .. figure:: images/duplicati/03_Duplicati.png

4. Select which type of files you wish to back up, and then click the **Next**
   button.

    .. figure:: images/duplicati/04_Duplicati.png

5. Enter the following:
    * **Protect the backups with this password** - This is optional but
      recommended
    * **Encryption method** – Select AES 256
    * **Use these settings on new backups** - Check this box to enable these
      settings for future backups

6. Click the **Next** button.

    .. figure:: images/duplicati/05_Duplicati.png

7. Select the 'Amazon S3 based' radio button, and then click the **Next**
   button.

    .. figure:: images/duplicati/06_Duplicati.png

8. Enter the following required DreamObjects credentials:
    * **S3 Servername** – objects-us-west-1.dream.io
    * **AWS Access ID and Secret Key** – Visit the `DreamObjects keys`_
      article for further details
    * **S3 Bucket name** – The name of your DreamObjects bucket

9. Click the **Next** button.

    .. figure:: images/duplicati/07_Duplicati.png

10. Select the desired Advanced settings, and then click the **Next** button.
     *A summary window appears where you can review details of the backup:*

    .. figure:: images/duplicati/08_Duplicati.png

11. Click the **Finish** button to save.

.. _DreamObjects keys: 215986357-What-are-Keys-in-DreamObjects-and-How-Do-You-Use-Them-

.. meta::
    :labels: duplicati
