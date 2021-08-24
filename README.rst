pgbackup
========

CLI interface for backup of remote PostgreSQL DB to either local storage or S3.

Preparing the Developmnet
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone the git repo:  ``git clone git@github.com:thehackadmin/pgbackup``
3. ``cd`` into the cloned repo.
4. Fetch development dependencies:  ``make install``
5. Activate python virtualenv:  ``pipenv shell``

Usage
-----

Pass in:
 - the full DB URL that is to be backed up
 - the storage driver
 - the destination

S3 example w/ bucket name:

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

Local example:

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql

Running Tests
-------------

Run tests locally using ``make`` if the virtualenv is active:

::

    $ make

If the virtualenv is not active then:

::

    $ pipenv run make

