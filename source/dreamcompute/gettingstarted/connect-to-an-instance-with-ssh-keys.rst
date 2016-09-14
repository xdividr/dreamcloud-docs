======================================
Connect to your instance with ssh keys
======================================

Once you have your SSH key created and imported into
the dashboard, you can go ahead and create your
instances.  Please make sure to select the keypair you
wish to use on the "Access & Security" tab of the
instance creation screen.  For ssh to work it is
required that port 22 is open in your selected
security group in the DreamCompute
`Access & Security - Security Group <https://dashboard.dreamcompute.com/project/access_and_security/?tab=access_security_tabs__security_groups_tab>`_
dashboard.

Using Windows
-------------

A common program for ssh on windows is
`PuTTY <http://www.chiark.greenend.org.uk/~sgtatham/putty/?>`_
or `putty-nd <http://sourceforge.net/projects/putty-nd/>`_
.  PuTTY requires that you convert your
private key into a .ppk file before it can be used to
connect via ssh.  To do this, open up the PuTTY Key
Generator (puttygen.exe), click the Conversions menu
then "Import Key".  Browse to the folder that contains
the \*.pem file you downloaded from the DreamCompute
dashboard, or the private key you created outside the
Dashboard.  You can give the key a name in the "Key
comment" field, and when finished click the "Save
private key" button to save it into a .ppk file.

Now you can open PuTTY and navigate to the Connection
-> SSH -> Auth setting page to click the "browse"
button near the "Private key file for authentication"
field.  Select the .ppk file you generated and then
click open.  You can now navigate to the "Session"
setting page, and enter the username of your image
into the host name field, followed by the IP address
of your server.

The default username for each image is:

.. include:: common/usernames.rst

Using Mac & Linux
-----------------

On Unix based systems, the ssh key will need to be setup
first.  There are several ways to do this:

* Configure as your main key
    * Copy the key or .pem file to your home directory,
      to the ~/.ssh/id_rsa file.

* Configure as an alternative key
    * Copy the key or .pem file to a safe place, and then edit
      your ~/.ssh/config file to specify that connections to
      that specific host will use this alternate key.

    .. code-block:: bash

        Host IPADDRESS
        IdentityFile ~/path/to/key

.. code-block:: bash

    $ ssh user@IPADDRESS
    Welcome to Ubuntu 12.04.2 LTS (GNU/Linux
    3.5.0-23-generic x86_64)
    user@example:~$

* No configuration, specifying the key on the command line
    * Connect via ssh -i ~/path/to/key user@IPADDRESS

.. meta::
    :labels: ssh key mac linux windows
