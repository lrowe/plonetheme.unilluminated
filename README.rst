
Introduction
============

The ``plonetheme.unilluminated`` package uses the *theming & packaging* features
available in `plone.app.theming`_ to make the `CSS Templates`_ theme `Unilluminated`_ easily
available in `Plone 4.1`_.

.. image:: https://github.com/aclark4life/plonetheme.unilluminated/raw/master/screenshot.png

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

.. _`Unilluminated`: http://www.freecsstemplates.org/preview/unilluminated/
.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`Plone 4.1`: http://pypi.python.org/pypi/Plone/4.1rc2
.. _`CSS Templates`: http://www.freecsstemplates.org/
