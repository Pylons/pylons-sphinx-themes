Pylons Sphinx Themes
====================

This repository is a Python package that contains Sphinx themes for Pylons related projects. This project is based on `Pylons Sphinx Theme <https://github.com/Pylons/pylons_sphinx_theme>`_ (singular), but uses a package implementation instead of git submodules and manual steps.

To use a theme in your Sphinx documentation, follow this guide.


Edit your project's ``setup.py``
--------------------------------
#. Add ``pylons-sphinx-themes`` to your project's requirements in its ``setup.py``. Here's an example from Pyramid.

   .. code-block:: python

       docs_extras = [
           'Sphinx >= 1.3.1', # Read The Docs minimum version
           'docutils',
           'repoze.sphinx.autointerface',
           'pylons-sphinx-themes',
           ]


Edit your Sphinx's ``conf.py``
------------------------------
#. Near the top, add the following.

   .. code-block:: python

       import pylons_sphinx_themes

#. Activate the theme.

   .. code-block:: python

       html_theme = 'pyramid'
       html_theme_path = pylons_sphinx_themes.get_html_themes_path()

#. If you were previously using the git submodule method to use the Pylons theme, then comment or delete the block of code under the following statement.

   .. code-block:: python

       # Add and use Pylons theme
       if 'sphinx-build' in ' '.join(sys.argv):  # protect against dumb importers

#. (Optional) Set a canonical root URL. The URL points to the root of the documentation, and requires a trailing slash.

   .. code-block:: python

       html_theme_options = dict(
           canonical_url='http://the_root_domain/latest/docs/'
       )


Undo git submodule method
-------------------------
If you were previously using the git submodule method to use the Pylons theme, then perform the following additional steps.

#. Remove ``.gitmodules``.

   .. code-block:: bash

       cd <your_project_directory>
       git rm .gitmodules

#. Deinitialize the submodule.

   .. code-block:: bash

       cd docs/_themes
       git submodule deinit .

#. Remove the submodule's directory.

   .. code-block:: bash

       cd ..
       git rm _themes/

#. Edit your Sphinx's ``Makefile``. The following is an `example diff <https://github.com/Pylons/pyramid/pull/1636/files>`_ from Pyramid.

   .. code-block:: diff

       -html: themes
       +html:
       # ...
       -htmlhelp: themes
       +htmlhelp:
       #...
       -themes:
       -    cd ..; git submodule update --init --recursive; cd docs;


Update ``tox.ini``
------------------
If you use tox, you can specify dependencies for building your docs either in your ``setup.py`` (preferred) or in your ``tox.ini`` (duplicitous). See the `example from Pyramid <https://github.com/Pylons/pyramid/blob/master/setup.py#L58-L64>`_.

.. code-block:: ini

    docs_extras = [
        'Sphinx >= 1.3.1',
        'docutils',
        'repoze.sphinx.autointerface',
        'pylons_sphinx_latesturl',
        'pylons-sphinx-themes',
        ]

    # ...

    extras_require = {
        'testing':testing_extras,
        'docs':docs_extras,
        },

Otherwise you can repeat yourself and edit your ``tox.ini``. The following example is from `waitress <https://github.com/Pylons/waitress/blob/master/tox.ini#L28>`_.

.. code-block:: ini

    deps =
        Sphinx
        repoze.sphinx.autointerface
        pylons-sphinx-themes


Update Read the Docs configuration
----------------------------------
If you specify package requirements for Read the Docs, specify dependencies in your ``rtd.txt``. You can either name them explicitly, which might be duplicitous:

.. code-block:: text

    pylons-sphinx-themes

or you can rely on your ``setup.py`` configuration, specifying dependencies in only one place, by simply using this in your ``rtd.txt``.

.. code-block:: text

    -e .[docs]


Available themes
----------------

- **pylons** - the generic Pylons Project documentation theme
- **pyramid** - the specific Pyramid documentation theme
- **pylonsfw** - the specific Pylons Framework documentation theme
