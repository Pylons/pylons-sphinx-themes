##############################################################################
#
# Copyright (c) 2015 Agendaless Consulting and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt. A copy of the license should accompany
# this distribution. THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################

import os

from setuptools import setup, find_packages

VERSION = '1.0.2'

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

requires = []

setup(name='pylons-sphinx-themes',
      version=VERSION,
      description='Sphinx themes for Pylons Project documentation.',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Sphinx :: Theme',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: Repoze Public License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Documentation',
          'Topic :: Documentation :: Sphinx',
          'Topic :: Software Development :: Documentation',
      ],
      keywords='pyramid pylons web sphinx documentation',
      author='Steve Piercy',
      author_email='pylons-discuss@googlegroups.com',
      url='https://pylonsproject.org',
      license='BSD-derived (http://www.repoze.org/LICENSE.txt)',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points=''
      )
