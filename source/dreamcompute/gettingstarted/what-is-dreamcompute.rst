====================
What is DreamCompute
====================

DreamHost's DreamCompute is a cloud computing service that provides scalable
compute resources for developers and entrepreneurs. DreamCompute is based on
OpenStack and designed for scalability, resiliency, and security.

With DreamCompute you can select the amount of compute resources and storage
resources needed and define your own virtual networks.


Service Highlights
~~~~~~~~~~~~~~~~~~

OpenStack
---------

DreamCompute is powered by OpenStack which is a widely adopted, open source
cloud computing platform. It is used by both public cloud hosting companies,
like DreamHost, and for private internal clouds as well.

.. figure:: images/OpenStack.png
    :align: center
    :alt: OpenStack
    :figclass: align-center

Compute
-------

DreamCompute provides virtual servers through the use of the
`KVM hypervisor <http://www.linux-kvm.org/>`_. Virtual machines (VMs) can be
started by creating an Instance using the DreamCompute dashboard. Each instance
is based on a Flavor. Flavors define the amount of resources allocated to the
VM in terms of vCPUs, memory, and boot volume size. DreamCompute provides
Flavors small enough for companies just starting out to large ones for
companies with greater computing needs.

Network
-------

Networking services for DreamCompute are delivered through OpenStack's
`Neutron service <http://wiki.openstack.org/Neutron>`_, coupled with
DreamHost's own `Akanda <https://github.com/openstack/astara>`_ project which
has been picked up by OpenStack and renamed Astara.

Another component to DreamCompute networking is the open source Akanda project
developed by DreamHost. Akanda serves as a network traffic router (OSI Layer 3)
for virtual networks created in DreamCompute. Akanda allows virtual networks to
be configured to talk to each other, to LANs, to WANs or to the Internet.

The combination of Neutron, and Akanda bring a level of network flexibility
and security that sets DreamCompute apart from the competition.

Storage
-------

Storage in DreamCompute is implemented with `Ceph <http://ceph.com/>`_. Ceph
is a massively scalable, distributed, redundant storage technology that can
be delivered using standard server hardware. OpenStack's
`Cinder <http://wiki.openstack.org/Cinder>`_ project integrates with Ceph for
block storage using Ceph's RADOS Block Device (RBD) software.

Ceph is software created by DreamHost founder Sage Weil and has been under
development inside DreamHost for several years. Ceph has been open source
since its inception, and in early 2012, a new company called `Inktank
<http://www.inktank.com/>`_ was spun out of DreamHost to support and continue
development of the technology. Inktank was then acquired by Red Hat in April
2014.

Ceph is also the foundation for DreamHost's cloud storage service
`DreamObjects`_.

Dashboard
---------

The DreamCompute dashboard is built with OpenStack's
`Horizon <http://wiki.openstack.org/Horizon>`_ project. The dashboard provides a
user interface for interacting with DreamCompute's three main services:
Compute, Networking, and Storage.  Functions such as launching an instance,
creating storage volumes, and configuring a virtual network, as well as
creating and managing snapshots of both a running instance and storage volumes,
can all be done in the dashboard.

Automation APIs
---------------

OpenStack, and therefore DreamCompute, has a whole host of APIs that can be
used for system automation. More about OpenStack APIs can be found here:
http://docs.openstack.org/api

.. _DreamObjects: https://dreamhost.com/cloud/storage

.. meta::
    :labels: nova glance keystone akanda neutron network dashboard
             horizon quota billing
