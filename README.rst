Pylons Sphinx Themes
====================

This repository is a Python package that contains Sphinx themes for Pylons
related projects. This project is based on `Pylons Sphinx Theme
<https://github.com/Pylons/pylons_sphinx_theme>`_ (singular), but uses a
package implementation instead of git submodules and manual steps.

To use a theme in your Sphinx documentation, follow this guide.

Edit your Sphinx documentation's ``conf.py``
--------------------------------------------
1. Near the top, add the following.::

    import pylons_sphinx_themes

2. Activate the theme::

    html_theme = 'pyramid'
    html_theme_path = pylons_sphinx_themes.get_html_themes_path()

3. If you were previously using the git submodule method to use the Pylons
   theme, then comment or delete the block of code under the following
   statement::

    # Add and use Pylons theme
    if 'sphinx-build' in ' '.join(sys.argv):  # protect against dumb importers
    ...

4. (Optional) Set a canonical root URL::

    html_theme_options = dict(
        canonical_url='http://the_root_domain/latest/docs/'
    )
   
The URL points to the root of the documentation, and requires a trailing
slash.

The following themes exist.

- **pylons** - the generic Pylons Project documentation theme
- **pyramid** - the specific Pyramid documentation theme
- **pylonsfw** - the specific Pylons Framework documentation theme
