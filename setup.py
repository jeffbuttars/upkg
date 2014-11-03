#!/usr/bin/env python
# encoding: utf-8

import os
from setuptools import setup, find_packages

def read(fname):
    res = ""
    with open(os.path.join(os.path.dirname(__file__), fname), 'r') as fd:
        res = fd.read()
    return res


setup(name='upkg',
      version='0.1.5',
      description="Package Yourself",
      url='https://github.com/jeffbuttars/upkg',
      long_description=read('README.md'),
      author="Jeff Buttars",
      author_email="jeff@jeffbuttars.com",
      packages=find_packages(exclude=['tests*']),
      license='GPLv2',
      # package_dir={'pkgs': 'pkgs'},
      # install_requires=[
      #     'tornado',
      # ],
      entry_points = {
          'console_scripts': [
              'upkg = upkg.upkg:main',
          ],
      },
      data_files=[
          # ('/etc/init.d', ['']),
      ],
      )
