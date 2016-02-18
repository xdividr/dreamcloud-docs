=================================================
How to signup to DreamCompute and other questions
=================================================

How do I sign up to DreamCompute?
---------------------------------

If you've already got a DreamHost account then you can sign up from your
`Control Panel <http://panel.dreamhost.com/dreamcompute>`_. If not, sign up
from `DreamCompute page <http://www.dreamhost.com/cloud/dreamcompute>`_.

How much does DreamCompute cost?
--------------------------------

DreamCompute has a very simple and predictable pricing plan: you only
pay for what you use, with a maximum monthly expense. No more
confusing invoices or bills, and no surprise at the end of the month.
For example, if all you need is a small size machine (1 CPU, 1Gb RAM)
for 5 hours a month, you’ll pay 5 cents. If you use that for more than
25 days in a month, you’ll only pay a maximum of $6. Monthly prices
are the same either you use virtual machines in February or in July.

+-------------------------------------------------------+
| vMemory   | vCPU  | Hourly Price  | Max Monthly Price |
+-------------------------------------------------------+
|   512mb   |   1   |   $ 0.0075    |   $4.50           |
+-------------------------------------------------------+
|   1GB     |   1   |   $ 0.01      |   $6              |
+-------------------------------------------------------+
|   2GB     |   1   |   $ 0.02      |   $12             |
+-------------------------------------------------------+
|   4GB     |   2   |   $ 0.04      |   $24             |
+-------------------------------------------------------+
|   8GB     |   4   |   $ 0.08      |   $48             |
+-------------------------------------------------------+
|   16GB    |   8   |   $ 0.16      |   $96             |
+-------------------------------------------------------+

With any of our DreamCompute plans, you can easily create virtual machines,
block devices and networks using the DreamCompute Dashboard, or via OpenStack
APIs and command-line tools.

What are the limits to the amount of resources I can get?
---------------------------------------------------------

Since customers pay DreamCompute resources (RAM and vCPUs) by the
hour, you can use as many as you like. In order to prevent abuse, the
default maximum amounts per customer are set as follows:

 - CPU: 32 cores
 - RAM: 64 GB
 - Instances: 32

These limits can be overridden to allow for specific needs. Please
contact FIXME.

How much does it cost to store in DreamCompute?
-----------------------------------------------

For a limited time, each new customer of DreamCompute will have a
maximum amount of 10 volumes with 100Gb maximum each. When prices will
change, you'll be notified.

How much does it cost to transfer data in and out of DreamCompute?
------------------------------------------------------------------

For a limited time, data transfer is free inbound and outbound of
DreamCompute virtual machines. When prices will change, you'll be
notified.

How much does it cost to have IP addresses in DreamCompute?
-----------------------------------------------------------

Every DreamCompute instance boots with a public IPv6 address, free of
charge. Since IPv4 are getting harder to find, DreamCompute offers
only one floating IPv4 address for free in each DreamCompute region.
If you need more IPv4 addresses you can buy more at an additional cost
of $1 per IPv4 address.

How much does it cost to keep snapshots of DreamCompute instances?
------------------------------------------------------------------

You can keep up to 10 snapshots of your running instances for free.

How can I transfer my account from DreamCompute Beta?
-----------------------------------------------------

If you signed up for DreamCompute Beta and want to use the new
DreamCompute hour-based billing, you'll have to migrate your instances
and images to the new cluster. FIXME:NEW_PAGE_TO_EXPLAIN_MIGRATION


Where are the data centers located?
-----------------------------------

DreamHost cloud services are currently located in the United States, but
accessible from anywhere globally.  DreamCompute is located in our
Ashburn, Virginia (US-East) datacenter, and DreamObjects is located in our
Irvine, California (US-West) datacenter.

Will DreamCompute scale?
------------------------

Yes. You can scale your apps both vertically and horizontally, by creating VMs
with additional resources, or by spinning up additional VMs to handle similar
or diverse infrastructure workloads (e.g. creating multiple load balancers, or
separating web servers and databases). The unique networking features in
DreamCompute enable developers and operations teams to design sophisticated
n-tier architectures, with many VMs.

Can I scale my disk volume on a running instance?
-------------------------------------------------

You can scale your disk volumes that are in use if you use
`LVM <http://tldp.org/HOWTO/LVM-HOWTO/>`_ (Logical Volume Manager). We recommend
using LVM when mounting your disk volumes for this reason. LVM allows you to
continually add more disk space without any service interruption.  If you don't
use LVM you would need to mount another (larger) volume, then copy your data
from the old to the new volume.

Can I scale my CPU or memory on a running instance?
---------------------------------------------------

If you wish to add more memory or vCPU capacity to an instance, you will need
to start a new larger instance.  First, take a snapshot of your current
instance, then start a new larger instance based on that snapshot.

Is my data backed up?
---------------------

Short answer: it depends on what you mean by 'my data' and most likely
the answer is ``no``. While our systems are based on highly scalable,
redundant, and self-healing storage technology, we don't keep copies
of your volumes and your virtual machines snapshots. If for any
reason you delete or break them, we have no way to recover an older version.

What our storage backend Ceph is designed for is to deliver extreme
durability of data, by creating and managing replicas of your data
that are intelligently distributed across zones in our data centers.
The system automatically detects potential corruption of data or
potential failure or degradation of any storage node, and immediately
creates new replicas from redundant data copies, delivering
enterprise-grade durability. Those are security and safety measures
and don't constitute a back up in practical terms.

.. _DreamObjects: https://dreamhost.com/cloud/storage

.. meta::
    :labels: nova glance keystone akanda neutron network dashboard
             horizon quota billing
