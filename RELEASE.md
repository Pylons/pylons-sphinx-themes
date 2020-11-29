# Releasing

[zest.releaser](https://zestreleaser.readthedocs.io/en/latest/) is used for releasing this package.

To release:

1.  Edit CHANGES.txt replacing "Nothing changed yet." with your changes, and commit.

2.  Invoke the following command from your virtual environment.

    ```bash
    fullrelease
    ```

3.  Finally cut a new release from the new tag on [GitHub](https://github.com/Pylons/pylons-sphinx-themes/releases).


## Updating READMEs

`README.rst` is the canonical README file in reStructuredText format for use on PyPI. Edit this file to update both READMEs.

`README.md` is the markdown version. It is generated via [pandoc](https://pandoc.org/) with the following command.

```
pandoc --from=rst --to=markdown --output=README.md README.rst
```
