How Will My DreamCompute Bill Change?
=====================================

We're ending the DreamCompute *beta* program and launching a brand new way to
bill for DreamCompute!

Throughout the beta test we heard your concerns about wanting more flexibility
for taking advantage of the resources provided by your plan. We also heard that
you liked predictable monthly bills. We've found a way to address both concerns
with the introduction of predictable hourly billing.

The new hourly billing system starts once you opt-in, and will transition you
from a pre-paid plan, to only paying for what you use. Depending on your usage
of DreamCompute, your bill may be higher or lower.

Additionally, we're adding a new, faster DreamCompute cluster called US-East 2.
It's twice as fast as US-East 1, and powered by speedy Intel Xeon E5 processors,
all-SSD storage, and hardware accelerated virtual networking.

.. include:: common/billing-faq.rst
    :end-before: .. US-East 2

US-East 1
~~~~~~~~~

The original DreamCompute cluster is outfitted with AMD Opteron 6200 series
processors, traditional hard drives and private networking. Sizes range from
1GB to 64GB.

+-------------+--------+------+--------------+-------------------+
| Flavor Name | Memory | vCPU | Hourly Price | Max Monthly Price |
+=============+========+======+==============+===================+
| subsonic    |  1 GB  |   1  |    $0.0075   |        $4.50      |
+-------------+--------+------+--------------+-------------------+
| supersonic  |  2 GB  |   1  |    $0.015    |        $9.00      |
+-------------+--------+------+--------------+-------------------+
| lightspeed  |  4 GB  |   2  |    $0.03     |       $18.00      |
+-------------+--------+------+--------------+-------------------+
| warpseed    |  8 GB  |   4  |    $0.06     |       $36.00      |
+-------------+--------+------+--------------+-------------------+
| hyperspeed  | 16 GB  |   8  |    $0.12     |       $72.00      |
+-------------+--------+------+--------------+-------------------+
| ridiculous  | 32 GB  |  16  |    $0.24     |      $144.00      |
+-------------+--------+------+--------------+-------------------+
| ludicrous   | 64 GB  |  32  |    $0.48     |      $288.00      |
+-------------+--------+------+--------------+-------------------+

.. include:: common/billing-faq.rst
    :start-after: .. US-East 2

Do I have to switch to hourly billing now?
------------------------------------------

You can wait and stay on the old billing plan, but you cannot access
the faster US-East 2 zone until you have activated hourly billing.

How do I get started?
---------------------

You can activate predictable hourly billing and gain access to the new, faster
DreamCompute cluster from the `DreamHost Control Panel`_.

.. _DreamHost Control Panel: https://panel.dreamhost.com/dreamcompute

.. meta::
  :labels: dreamcompute faq billing
