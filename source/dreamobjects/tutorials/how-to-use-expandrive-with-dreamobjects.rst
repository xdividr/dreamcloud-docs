=======================================
How to Use ExpanDrive with DreamObjects
=======================================

Overview
~~~~~~~~

`ExpanDrive <https://www.expandrive.com/expandrive>`_ is an app that allows
you to connect to DreamObjects just like a USB drive. It is available for both
Mac_ and Windows_ and allows you to access DreamObjects from any application on
your computer. Before you begin, you'll need to create a `bucket`_ on the
`(Panel > 'Cloud Services' > DreamObjects'
<https://panel.dreamhost.com/index.cgi?tree=cloud.objects&>`_) page.

.. _Mac:

|mac32| Mac version
--------------------

1. `Download the latest release for Mac
   <https://www.expandrive.com/expandrive>`_.
2. Launch ExpanDrive and select the DreamObjects drive type.

    .. figure:: images/expandrive/01_Expandrive_MAC.png

3. Enter the following:
    * **Server:** objects-us-west-1.dream.io
    * **Access Key ID:** Your DreamObjects Access Key
    * **Secret Access Key:** Your DreamObjects Secret Key

    .. figure:: images/expandrive/02_Expandrive_MAC.png

    * Visit the `DreamObjects keys`_ article for details on finding your keys.

4. Click the **Connect** button.

    .. figure:: images/expandrive/03_Expandrive_MAC.png

5. You may see a window the first time you connect asking for you to enter you
   Mac user's password. Enter it and click **OK**. This only needs to be done
   the first time you connect.

    .. figure:: images/expandrive/04_Expandrive_MAC.png

    *The Finder window on your computer opens with your DreamObjects bucket*

6. DreamObjects will now show as a mounted drive. You can see it visible in
   the sidebar. You'll also see it in open and save dialogs in your
   applications letting you easily access your DreamObjects data.

.. _Windows:

|windows32| Windows version
---------------------------

1. `Download the latest release for Windows
   <https://www.expandrive.com/expandrive>`_.
2. Launch ExpanDrive and select the DreamObjects drive type.

    .. figure:: images/expandrive/01_Expandrive.png

3. Enter the following:
    * **Server:** objects-us-west-1.dream.io
    * **Access Key ID:** Your DreamObjects Access Key
    * **Secret Access Key:** Your DreamObjects Secret Key

    .. figure:: images/expandrive/02_Expandrive.png

    * Visit the `DreamObjects keys`_ article for details on finding your keys.

4. Click the **Save** button.

    .. figure:: images/expandrive/03_Expandrive.png

5. Click the arrow icon to the right of the 'DreamObjects' option.

    .. figure:: images/expandrive/04_Expandrive.png

    *An explorer window on your computer opens with your DreamObjects bucket*

6. Your DreamObjects data is now accessible as a mounted drive letting you
   easily access your DreamObjects data.

.. |mac32| image:: images/mac32.png

.. |windows32| image:: images/windows32.png

.. _DreamObjects keys: 215986357-What-are-Keys-in-DreamObjects-and-How-Do-You-Use-Them-

.. _bucket: 215321178-What-are-Buckets-in-DreamObjects-and-How-Do-You-Use-Them-

.. meta::
    :labels: expandrive
