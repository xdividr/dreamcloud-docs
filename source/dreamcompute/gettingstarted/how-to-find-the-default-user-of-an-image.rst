========================================
How to find the default user of an image
========================================

`DreamCompute Dashboard <https://iad2.dreamcompute.com/project/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Navigate to Compute > Instances > Click on the name of your instance >
   Click on the Image Name of your instance
#. Look under the "Custom Properties" section for "default_user" (this will
   only work for ephemeral instances)

`DreamHost Cloud Control Panel <http://cloud.dreamhost.com/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Click on the instance name that you want to know the default user of.
#. Look under the "SSH Login" section for "**ssh $user@$ip**", the username is
   found before the "@" in that command.

The default user is the user you can use to login with the public key that you
added to your instance.

.. include:: common/usernames.rst

.. meta::
    :labels: images users
