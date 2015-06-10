#!/usr/bin/env python

from distutils.core import setup

setup(name='MethylTools',
      version='0.1',
      description='Helper tools for dealing with Illumina 450k methylation data.',
      author='Andrew Gross',
      author_email='the.andrew.gross@gmail.com',
      url='http://andy-gross.flavors.me',
      package_dir = {'': 'Notebooks'},
      packages=['MethylTools'],
      package_data = {'': ['*.ipynb', 'Data/*.csv']}
     )
