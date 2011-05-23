
Introduction
============

The ``plonetheme.unilluminated`` package uses the *theming & packaging* features
available in `plone.app.theming`_ to make the `CSS Templates`_ theme `Unilluminated`_ easily
available in `Plone 4.1`_.


Installation
------------

Currently, only installation via Python package (and buildout) is supported. But an installable zip file is in development. 

Buildout
~~~~~~~~

Add ``plonetheme.unilluminated`` to your ``plone.recipe.zope2instance`` section's *eggs* parameter e.g.::

    [instance]
    eggs =
        Plone
        …
        plonetheme.unilluminated

Zip file
~~~~~~~~

XXX Coming soon

Configuration
-------------

Once you have installed the package, you must configure it in Plone.

Add Plone site
~~~~~~~~~~~~~~

Install Plone 4.1 and create a Plone site (if you have not already) with Diazo theming configured.

.. image:: https://github.com/aclark4life/plonetheme.unilluminated/raw/master/screenshot2.png


Select theme
~~~~~~~~~~~~

Select and enable the theme from the Diazo control panel.

.. image:: https://github.com/aclark4life/plonetheme.unilluminated/raw/master/screenshot3.png

That's it!

You should see (without the calendar):

.. image:: https://github.com/aclark4life/plonetheme.unilluminated/raw/master/screenshot.png

Help
----

Obviously there is more work to be done. If you want to help, pull requests accepted! Some ideas:

* Fix zip file (currently getting a traceback from lxml, even with zip files from w/p.a.theming tests)
* Add a diazo rule to import Plone editing styles
* Configure styles to use portal_css
* Add quick installer support

License
-------

The author is not a "license guy", but the Unilluminated theme is distributed via CC 3.0 license [1]_ and this package is GPL version 2 (assuming that makes sense).

.. _`Unilluminated`: http://www.freecsstemplates.org/preview/unilluminated/
.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`Plone 4.1`: http://pypi.python.org/pypi/Plone/4.1rc2
.. _`CSS Templates`: http://www.freecsstemplates.org/

.. [1] http://www.freecsstemplates.org/license/
