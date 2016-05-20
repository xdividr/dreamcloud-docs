================================
How to Use Arq with DreamObjects
================================

Overview
~~~~~~~~

.. figure:: images/Arq-icon.png

`Arq <https://www.arqbackup.com>`_ is a Mac and Windows app that allows you to
make online backups that support DreamObjects. Arq backups are encrypted with
a password before they're uploaded so your data is protected.

The installation and configuration of Arq varies depending on the operating
system.  Click your operating system below to jump to the proper instructions.

    * `Windows <#connecting-with-arq-on-windows>`_
    * `Mac <#connecting-with-arq-on-mac>`_

Connecting with Arq on Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Launch Arq.  When launching Arq for the first time, you are prompted to
   choose your backup destination type.  Click the 'Other S3-Compatible
   Service' option, and then click **continue**.

.. figure:: images/Arq-1-win.png

2. For the S3-Compatible Server URL, enter the hostname
   'https://objects-us-west-1.dream.io'. Next ensure that the signature version
   defaults to 'Signature Version 2', and then fill in the access and secret
   keys with the values from the DreamHost panel.  Click **continue** to
   advance to the next step.  Visit the following article for further
   information about finding your DreamObjects keys:

    * `DreamObjects Keys`_

.. figure:: images/Arq-2-win.png

3. Arq will prompt you to enter a new bucket name, or select an existing
   bucket.  Choose the option you want and enter a name if necessary, then
   click **Add** to complete.

.. figure:: images/Arq-3-win.png

4. After your bucket is configured, Arq will ask if you want to setup a new
   backup schedule, or to restore files from this bucket (which requires
   existing backups in your bucket).  Click **Set Up Backups**.

.. figure:: images/Arq-4-win.png

5. Create an encrypted password for your backup which allows additional
   security for the backup created.

.. figure:: images/Arq-5-win.png

6. After you enter an encrypted password, be sure to write down the password
   you created and store it somewhere safe.

.. figure:: images/Arq-6-win.png

7. On Windows systems, Arq defaults to backing up the entire C: drive
   excluding only the Recycle Bin and the pagefile.sys file.

.. figure:: images/Arq-7-win.png

8. To add or remove files or folders, click the **Edit backup suggestions**
   button, which will allow you to customize the selection.

    *Arq is now configured to backup your data:*

.. figure:: images/Arq-8-win.png

Connecting with Arq on Mac
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Launch Arq.  When launching Arq for the first time, you are prompted to
   choose your backup destination type.  Select 'DreamObjects' from the
   drop-down list.  Fields to enter the access and secret keys will appear
   as well as a button to open the DreamHost panel to find your keys.  Enter
   your desired keys.  Visit the following article for further information:

    * `DreamObjects Keys`_

.. figure:: images/Arq-1-mac.png

2. After you enter the DreamObjects access Key and secret Key, enter a new
   bucket name or select an existing bucket from the drop down list.

.. figure:: images/Arq-2-mac.png

3. After your bucket is configured, Arq will ask if you want to setup a new
   backup schedule, or to restore files from this bucket (which requires
   existing backups in your bucket).  Click **Set Up Backups**.

.. figure:: images/Arq-3-mac.png

4. Create an encrypted password for your backup which allows additional
   security for the backup created.

.. figure:: images/Arq-4-mac.png

5. After you enter an encrypted password, be sure to write down the password
   you created and store it somewhere safe.

.. figure:: images/Arq-5-mac.png

6. On Mac systems, Arq defaults to backing up the /Users directory, excluding
   files it knows are unnecessary like cache and page files.

.. figure:: images/Arq-6-mac.png

7. To add or remove files or folders, click the **Edit backup suggestions**
   button, which will allow you to customize the selection.

    *Arq is now configured to backup your data:*

.. figure:: images/Arq-7-mac.png

.. _DreamObjects Keys: 215986357-What-are-Keys-in-DreamObjects-and-How-Do-You-Use-Them-

.. meta::
    :labels: arq windows mac backup
