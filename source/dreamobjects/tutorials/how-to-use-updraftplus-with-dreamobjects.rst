========================================
How to Use UpdraftPlus with DreamObjects
========================================

Overview
--------

`UpdraftPlus <http://updraftplus.com>`_ brings reliable, easy-to-use backups,
restores and site copies (clones/migrations) to your WordPress site.

Installation and Configuration of Backups
-----------------------------------------

#. Log into your WordPress site.

    .. figure:: images/01_UpdraftPlus.png

#. In the left menu, choose 'Plugins > Add New'.
#. Search for 'UpdraftPlus'. Once found click the **Install Now** button.

    .. figure:: images/02_UpdraftPlus.png

#. On the main 'Plugins' page, click the 'Settings' link under the plugin.

    .. figure:: images/03_UpdraftPlus.png

#. On the main page for the plugin, click the 'Settings' tab.

    Configure UpdraftPlus to backup your files and database on the intervals you
    prefer.

    If you would like to use an encryption phrase, click the link to purchase the
    paid version.

    .. figure:: images/04_UpdraftPlus.png

#. Scroll down on the same settings page to the section titled 'Copyin Your
   Backup To Remote Storage'.
#. Choose DreamObjects from the 'remote storage' dropdown, then enter your
   DreamObjects keys and existing DreamObjects bucket name.
#. Click the **Test DreamObjects Settings** button to ensure the connection
   works.

That's it. You'll now have backups of your WordPress site stored in
DreamObjects.

Restore a backup
----------------

    .. figure:: images/05_UpdraftPlus.png

#. On the main UpdraftPlus plugin page, click the **Restore** button.

    .. figure:: images/06_UpdraftPlus.png

#. Press the **Restore** button to the right of a backup to restore the
   site.

.. meta::
    :labels: backup
