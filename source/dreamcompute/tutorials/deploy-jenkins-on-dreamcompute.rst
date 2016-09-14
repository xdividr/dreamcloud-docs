=====================================
How to deploy Jenkins on DreamCompute
=====================================

Jenkins is software that provides testing for continuous integration. It can be
used to test branches of code in a version control repo.

Setting up a server
~~~~~~~~~~~~~~~~~~~

The first step to deploying Jenkins is to launch a server to run it on. For
example in this tutorial, an Ubuntu Xenial server is used. Read `How to launch
and manage servers with the DreamCompute dashboard
<https://help.dreamhost.com/hc/en-us/articles/215912848-How-to-launch-and-manage-servers-with-the-DreamCompute-dashboard>`__
for information on how to do this.
You also need to expose port 8080 to incoming traffic,
as that is blocked by default. Read `How to configure access and security for
DreamCompute instances
<https://help.dreamhost.com/hc/en-us/articles/215912838-How-to-configure-access-and-security-for-DreamCompute-instances>`__
for information on how to do this.

Installing Jenkins
~~~~~~~~~~~~~~~~~~

Installing Jenkins is very simple on Ubuntu Xenial:

.. code:: bash

    sudo apt update
    sudo apt install jenkins

Now Jenkins is installed.

Setting up an HTTPS proxy
~~~~~~~~~~~~~~~~~~~~~~~~~

Now that you have Jenkins running and installed, the next step should be to set
up a https proxy so you can access Jenkins over an HTTPS connection, which is
more secure. This can be achieved with either NGINX or Apache. We will use
NGINX for this tutorial.

Installing NGINX
----------------

Installing NGINX is also very simple:

.. code:: bash

    sudo apt install nginx

Setting up SSL with NGINX using LetsEncrypt
-------------------------------------------

The next step is to get SSL certs and configure NGINX to use those certs.
Follow our tutorial for doing that `here <222252847>`_

Setting up a proxy to Jenkins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we want to configure NGINX so that it listens on port 80 and 443 and
redirects http requests to port 443 so that they use https instead and then
proxy 443 to Jenkins.

In order to do this you must edit your /etc/nginx/sites-available file to look
like the following:

.. code::

    server {
        listen 80 default;
        server_name jenkins.example.com;
        rewrite ^ https://$server_name$request_uri? permanent;
    }

    server {
        listen 443 default ssl;
        server_name jenkins.example.com;

        ssl_certificate /etc/letsencrypt/live/jenkins.example.com/cert.pem;
        ssl_certificate_key /etc/letsencrypt/live/jenkins.example.com/privkey.pem;

        ssl_session_timeout  5m;
        ssl_protocols  SSLv3 TLSv1;
        ssl_ciphers HIGH:!ADH:!MD5;
        ssl_prefer_server_ciphers on;

        location / {
            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-Proto https;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_redirect http:// https://;

            add_header Pragma "no-cache";

            proxy_pass http://127.0.0.1:8080;
        }
    }

Then restart the NGINX service to load the new configuration:

.. code::

    systemctl restart nginx

.. meta::
    :labels: nginx jenkins letsencrypt
