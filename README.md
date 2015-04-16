Pylons Sphinx Themes
====================

This repository is a Python package that contains Sphinx themes for Pylons
related projects. This project is based on
[Pylons Sphinx Theme](https://github.com/Pylons/pylons_sphinx_theme)
(singular), but uses a package implementation instead of git submodules and
manual steps.

To use a theme in your Sphinx documentation, follow this guide.

Edit your project's ``setup.py``
--------------------------------
1. Add ``pylons-sphinx-themes`` to your project's requirements in its
``setup.py``. Here's an example from Pyramid.

    ```python
    docs_extras = [
       'Sphinx >= 1.2.3',
       'docutils',
       'repoze.sphinx.autointerface',
       'pylons-sphinx-themes >= 0.3',
       ]
    ```

Edit your Sphinx's ``conf.py``
------------------------------
1. Near the top, add the following.

    ```python
    import pylons_sphinx_themes
    ```

2. Activate the theme.

    ```python
    html_theme = 'pyramid'
    html_theme_path = pylons_sphinx_themes.get_html_themes_path()
    ```

3. If you were previously using the git submodule method to use the Pylons
theme, then comment or delete the block of code under the following
statement.

    ```python
    # Add and use Pylons theme
    if 'sphinx-build' in ' '.join(sys.argv):  # protect against dumb importers
    ...
    ```

4. (Optional) Set a canonical root URL.

    ```python
    html_theme_options = dict(
        canonical_url='http://the_root_domain/latest/docs/'
    )
    ```

   The URL points to the root of the documentation, and requires a trailing
   slash.

Undo git submodule method
-------------------------
If you were previously using the git submodule method to use the Pylons theme,
then perform the following additional steps.

1. Remove ``.gitmodules``.

    ```bash
    cd <your_project_directory>
    git rm .gitmodules
    ```
2. Deinitialize the submodule.

    ```bash
    cd docs/_themes
    git submodule deinit .
    ```

3. Remove the submodule's directory.

    ```bash
    cd ..
    git rm _themes/
    ```

4. Edit your Sphinx's ``Makefile``. The following is an
   [example diff](https://github.com/Pylons/pyramid/pull/1636/files)
   from Pyramid.

    ```
    -html: themes
    +html:
    ...
    -htmlhelp: themes
    +htmlhelp:
    ...
    -themes:
    -	cd ..; git submodule update --init --recursive; cd docs;
    ```

Update Read the Docs configuration
----------------------------------
Add this package to your ``rtd.txt``.

```
pylons-sphinx-themes
```

Available themes
----------------

- **pylons** - the generic Pylons Project documentation theme
- **pyramid** - the specific Pyramid documentation theme
- **pylonsfw** - the specific Pylons Framework documentation theme
