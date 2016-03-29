How does hourly billing work?
-----------------------------

We bill you for each virtual server per hour of usage until
reaching the monthly price, at which the cost is capped for the month.

When is a virtual server considered running?
--------------------------------------------

Billing stops for a virtual server once it is deleted/terminated.

What are the hourly prices?
---------------------------

Opting into predictable hourly billing will allow you to access both
DreamCompute clusters. Since US-East 2 is so much faster than US-East 1, virtual
servers in each cluster have different prices.

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

US-East 2
~~~~~~~~~

Twice as fast as the original, powered by Intel Xeon E5 series processors, all-
SSD storage, and hardware accelerated public networking. Sizes range from 512MB
to 16GB.

+----------------+--------+------+--------------+-------------------+
|  Flavor Name   | Memory | vCPU | Hourly Price | Max Monthly Price |
+================+========+======+==============+===================+
| gp1.semisonic  | 512 MB |   1  |    $0.0075   |        $4.50      |
+----------------+--------+------+--------------+-------------------+
| gp1.subsonic   |  1 GB  |   1  |    $0.01     |        $6.00      |
+----------------+--------+------+--------------+-------------------+
| gp1.supersonic |  2 GB  |   1  |    $0.02     |       $12.00      |
+----------------+--------+------+--------------+-------------------+
| gp1.lightspeed |  4 GB  |   2  |    $0.04     |       $24.00      |
+----------------+--------+------+--------------+-------------------+
| gp1.warpseed   |  8 GB  |   4  |    $0.08     |       $48.00      |
+----------------+--------+------+--------------+-------------------+
| gp1.hyperspeed | 16 GB  |   8  |    $0.16     |       $96.00      |
+----------------+--------+------+--------------+-------------------+


How much do IPs cost?
---------------------

We have made a change in US-East 2 so that virtual servers receive a public
IPv4 and IPv6 address by default. The best part is that there is no
additional charge!

Once the new hourly pricing is activated, the price for a floating IP in
US-East 1 will change from $5.95 to only $1 per month.

How much does block storage cost?
---------------------------------

Each DreamCompute cluster includes 100 GB of block storage at no charge. You
can adjust your monthly allotment of block storage by purchasing additional
100GB chunks.

Monthly pricing for the 100 GB chunks varies by cluster since US-East 1 uses
traditional hard drives while US-East 2 uses SSDs. In US-East 1 it is
$5.00/month and in US-East 2 it is $10.00/month.

Pricing for block storage is based on the total monthly allotment rather than
the amount used.

What happened to private networks in US-East 2?
-----------------------------------------------

Based on the feedback we received during the beta period, we have implemented
default public networking. That means that virtual servers launched in
US-East 2 are automatically assigned public IPv4 and IPv6 addresses at no
additional charge.

Private networking is coming soon to US-East 2 with improvements based on the
feedback we received. We will allow you to add multiple networks at $5 each
per month. Let us know if you'd like to trial this feature in US-East 2 at no
charge!
