How Will My DreamCompute Bill Change?
=====================================

We’re ending the DreamCompute *beta* program and launching a brand new way to
bill for DreamCompute!

Throughout the beta test we heard your concerns about wanting more flexibility
for taking advantage of the resources provided by your plan. We also heard that
you liked predictable monthly bills. We've found a way to address both concerns
with the introduction of predictable hourly billing.

The new hourly billing system starts once you opt-in, and will transition you
from a pre-paid plan, to only paying for what you use. Depending on your usage
of DreamCompute, your bill may be higher or lower.

Additionally, we're adding a new, faster DreamCompute cluster called US-East-2.
It’s twice as fast as US-East-1, and powered by speedy Intel Xeon X5 processors,
all-SSD storage, and hardware accelerated virtual networking.


**How does hourly billing work?**

Once enabled, we’ll bill you for each virtual server per hour of usage. If a
virtual server runs for 25 days in a billing period, it will be charged a flat
monthly fee for that period.


**When is a virtual server considered running?**

Billing stops for a virtual server once it is deleted/terminated.


**What are the hourly prices?**

Since US-East 2 is so much faster than US-East 1, virtual servers in each
cluster have different prices.

US-East 1
---------

<<<<<<< HEAD
+-------------+--------+------+--------------+---------------+
| Flavor Name | Memory | vCPU | Hourly Price | Monthly Price |
+=============+========+======+==============+===============+
| subsonic    |  1 GB  |   1  |    $0.0075   |      $4.50    |
+-------------+--------+------+--------------+---------------+
| supersonic  |  2 GB  |   1  |    $0.015    |      $9.00    |
+-------------+--------+------+--------------+---------------+
| lightspeed  |  4 GB  |   2  |    $0.03     |     $18.00    |
+-------------+--------+------+--------------+---------------+
| warpseed    |  8 GB  |   4  |    $0.06     |     $36.00    |
+-------------+--------+------+--------------+---------------+
| hyperspeed  | 16 GB  |   8  |    $0.12     |     $72.00    |
+-------------+--------+------+--------------+---------------+
| ridiculous  | 32 GB  |  16  |    $0.24     |    $144.00    |
+-------------+--------+------+--------------+---------------+
| ludicrous   | 64 GB  |  32  |    $0.48     |    $288.00    |
+-------------+--------+------+--------------+---------------+
=======
+------------------------------------------------------------+
| Flavor Name | Memory | vCPU | Hourly Price | Monthly Price |
+============================================================+
| subsonic    |  1 GB  |   1  |    $0.0075   |      $4.50    |
+------------------------------------------------------------+
| supersonic  |  2 GB  |   1  |    $0.015    |      $9.00    |
+------------------------------------------------------------+
| lightspeed  |  4 GB  |   2  |    $0.03     |     $18.00    |
+------------------------------------------------------------+
| warpseed    |  8 GB  |   4  |    $0.06     |     $36.00    |
+------------------------------------------------------------+
| hyperspeed  | 16 GB  |   8  |    $0.12     |     $72.00    |
+------------------------------------------------------------+
| ridiculous  | 32 GB  |  16  |    $0.24     |    $144.00    |
+------------------------------------------------------------+
| ludicrous   | 64 GB  |  32  |    $0.48     |    $288.00    |
+------------------------------------------------------------+
>>>>>>> 859988f24ff23dced4303812b32f6fa87ae6ac83


US-East 2
---------

<<<<<<< HEAD
+----------------+--------+------+--------------+---------------+
|  Flavor Name   | Memory | vCPU | Hourly Price | Monthly Price |
+================+========+======+==============+===============+
| gp1.semisonic  | 512 MB |   1  |    $0.0075   |      $4.50    |
+----------------+--------+------+--------------+---------------+
| gp1.subsonic   |  1 GB  |   1  |    $0.01     |      $6.00    |
+----------------+--------+------+--------------+---------------+
| gp1.supersonic |  2 GB  |   1  |    $0.02     |     $12.00    |
+----------------+--------+------+--------------+---------------+
| gp1.lightspeed |  4 GB  |   2  |    $0.04     |     $24.00    |
+----------------+--------+------+--------------+---------------+
| gp1.warpseed   |  8 GB  |   4  |    $0.08     |     $48.00    |
+----------------+--------+------+--------------+---------------+
| gp1.hyperspeed | 16 GB  |   8  |    $0.16     |     $96.00    |
+----------------+--------+------+--------------+---------------+
=======
+---------------------------------------------------------------+
|  Flavor Name   | Memory | vCPU | Hourly Price | Monthly Price |
+===============================================================+
| gp1.semisonic  | 512 MB |   1  |    $0.0075   |      $4.50    |
+---------------------------------------------------------------+
| gp1.subsonic   |  1 GB  |   1  |    $0.01     |      $6.00    |
+---------------------------------------------------------------+
| gp1.supersonic |  2 GB  |   1  |    $0.02     |      $9.00    |
+---------------------------------------------------------------+
| gp1.lightspeed |  4 GB  |   2  |    $0.04     |     $18.00    |
+---------------------------------------------------------------+
| gp1.warpseed   |  8 GB  |   4  |    $0.08     |     $36.00    |
+---------------------------------------------------------------+
| gp1.hyperspeed | 16 GB  |   8  |    $0.16     |     $72.00    |
+---------------------------------------------------------------+
>>>>>>> 859988f24ff23dced4303812b32f6fa87ae6ac83


**How much do IPs cost?**

We have made a change in US-East 2 so that virtual servers receive a public
IPv4 and IPv6 address by default. The best part is that there is no additional
charge!

Once the new hourly pricing is activated, the price for a floating IP in
US-East 1 will change from $5.95 to only $1 per month.


**How much does block storage cost?**

Each DreamCompute cluster includes 100 GB of block storage at no charge. You
can adjust your monthly allotment of block storage by purchasing additional
100GB chunks.

Monthly pricing for the 100 GB chunks varies by cluster since US-East 1 uses
traditional hard drives while US-East 2 uses SSDs. In US-East 1 it is
$5.00/month and in US-East 2 it is $10.00/month.

Pricing for block storage is based on the total monthly allotment rather than
the amount used.


**Do I have to switch to hourly billing now?**

No, but you cannot access US-East 2 until you have activated hourly billing.


**What happened to private networks in US-East 2?**

Based on the feedback we received during the beta period, we have implemented
default public networking. That means that virtual servers launched in
US-East 2 are automatically assigned public IPv4 and IPv6 addresses at no
additional charge.

Private networking is coming soon to US-East 2 with improvements based on the
feedback we received. We will allow you to add multiple networks at $5 each
per month. Let us know if you’d like to trial this feature in US-East 2 at no
charge!

.. meta::
  :labels: dreamcompute faq billing
