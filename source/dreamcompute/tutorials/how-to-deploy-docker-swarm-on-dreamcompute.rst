==========================================
How to deploy Docker Swarm on DreamCompute
==========================================

In this tutorial we're going to use docker machine to deploy servers on
DreamCompute, then use them to create a Docker Swarm cluster.

What is Docker Swarm?
~~~~~~~~~~~~~~~~~~~~~

Docker Swarm is a way to build a cluster of Docker hosts. This allows you to
have a single host that you give containers to run (the manager), which will
then distribute the containers across the cluster to balance the load. We will
be deploying a 3 node docker cluster in this tutorial, one manager and 2
workers.

Installing Docker
~~~~~~~~~~~~~~~~~

Before we can deploy a Docker Swarm, we must first get all the pieces required
to do that, including docker, and docker machine. I will assume you are on
Ubuntu (although this should work with most Debian based distros).

.. code::

    apt-get install docker.io

This will install the docker engine. Next we must install docker machine, which
will be used to launch servers on DreamCompute.

.. code::

    mkdir ~/bin
    curl -L https://github.com/docker/machine/releases/download/v0.7.0/docker-machine-`uname -s`-`uname -m` > ~/bin/docker-machine && \
    chmod +x ~/bin/docker-machine

This will create a "bin" directory in your homedirectory if it does not exist,
then download the version 0.7.0 of docker machine and put the binary in
~/bin/docker-machine.

Create a security group for the swarm servers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The docker swarm servers will try and talk to eachother over some ports so we
need to open them up. The 2 that will need to be opened are 3376 and 2376 for
TCP. I will not explain how to do that here, but refer to `our guide on doing
that <215912838>`_

Deploying servers for the swarm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we must deploy some servers so that we can use them in the swarm, I'm going
to deploy 3 Ubuntu Trusty servers. First, source your RC file that has all of
your authentication for DreamCompute. Then run the following commands.

.. code::

    docker-machine create -d openstack --openstack-flavor-id 100 \
        --openstack-image-name Ubuntu-14.04 --openstack-net-name public \
        --openstack-ssh-user dhc-user --openstack-sec-groups swarm swarm-manager

    docker-machine create -d openstack --openstack-flavor-id 100 \
        --openstack-image-name Ubuntu-14.04 --openstack-net-name public \
        --openstack-ssh-user dhc-user --openstack-sec-groups swarm swarm-agent1

    docker-machine create -d openstack --openstack-flavor-id 100 \
        --openstack-image-name Ubuntu-14.04 --openstack-net-name public \
        --openstack-ssh-user dhc-user --openstack-sec-groups swarm swarm-agent2

Adding the servers to the swarm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So now we have 3 servers deployed on DreamCompute and we can start adding the
servers to the Docker Swarm. The first step is to connect to the swarm-manager
create the swarm. Do this with the following commands.

.. code::

    eval $(docker-manager env swarm-manager)

This connects your local docker to the docker engine that is running on
swarm-manager, so the docker commands you run locally will actually be run on
the swarm-manager, cool right?

.. code::

    docker run --rm swarm create

This creates a swarm on the swarm-manager server. The last line of output from
that command is the "discovery token" of the swarm, copy it and put it in a
file, you will need it later.

Now we must tell the manager to act as the manager of the swarm we just
created. We can do that with the following command.

.. code::

    docker run -d -p 3376:3376 -t -v \
        /var/lib/boot2docker:/certs:ro swarm manage -H 0.0.0.0:3376 --tlsverify \
        --tlscacert=/certs/ca.pem --tlscert=/certs/server.pem \
        --tlskey=/certs/server-key.pem token://<cluster_id>

Adding workers to the swarm
~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have the swarm manager running now, but we dont have any workers for it to
run the containers on. We'll add them to the swarm now.

.. meta::
    :labels: docker docker-machine
