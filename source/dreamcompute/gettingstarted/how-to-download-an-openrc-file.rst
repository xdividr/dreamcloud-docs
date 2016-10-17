=============================================
How to download your DreamCompute openrc file
=============================================

.. Note::

    The instructions in this article will work on Linux and MacOS, they may
    work in Bash on Windows, but that has not been tested.

What is an openrc file?
~~~~~~~~~~~~~~~~~~~~~~~

An openrc file is a small bash script that sets environment variables so that
OpenStack command line tools know how to communicate with DreamCompute.

How do I download my openrc file?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can find your openrc file in the DreamCompute Dashboard by navigating to
Compute > Access & Security > Api Access > Download OpenStack RC File. You can
also click this link to download it.
https://iad2.dreamcompute.com/project/access_and_security/api_access/openrc/

How do I use my openrc file?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The way to run the openrc file is to use the command `source`:

.. code-block:: console

    [user@localhost]$ source /path/to/openrcfile.sh

Type in the password you use for the DreamCompute Dashboard when it asks
for it. Now all the environment variables necessary should be set to use the
command line clients.

.. meta::
    :labels: authentication openrc
