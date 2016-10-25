Installing Ansible
~~~~~~~~~~~~~~~~~~

In order to install Ansible, you need a few dependencies first, python2,
python-virtualenv, and python-pip. In order to install those, run the
following.

.. code-block:: console

    [user@localhost] sudo apt-get install -y python2 python-virtualenv \
        python-pip

Type in your password for sudo (If you have one). It then will download some
packages and install them. Next we need to install Shade and Ansible in a
virtual environment, Shade is a library that Ansible uses to talk to OpenStack.
In order to do that, run the following.

.. code-block:: console

    [user@localhost] virtualenv -p /usr/bin/python2 venv && source \
        venv/bin/activate && pip install ansible && pip install shade

Now you have Shade installed and are ready to start writing Ansible
playbooks.

Whenever you want to use Ansible or Shade, you will have to activate the
virtual environment that they are in as they are not installed system wide.
The way you do that is by running:

.. code::

    [user@localhost] source venv/bin/activate
    (venv)[user@localhost]

In order to deactivate the virtual environment, run the following:

.. code::

    (venv)[user@localhost] deactivate
    [user@localhost]
