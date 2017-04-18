# Releasing

[zest.releaser](http://zestreleaser.readthedocs.io/en/latest/) is used for releasing this package.

To release, invoke the following command from your virtual environment.

```bash
fullrelease
```


## Updating READMEs

`README.rst` is the canonical README file in reStructuredText format for use on PyPI. Edit this file to update both READMEs.

`README.md` is the markdown version. It is generated via [pandoc](http://pandoc.org/) with the following command.

```
pandoc --from=rst --to=markdown --output=README.md README.rst
```
