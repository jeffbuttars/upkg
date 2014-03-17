#!/usr/bin/env python
# encoding: utf-8

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#read()


setup(name='upkg',
      version='0.1.4',
      description="Package Yourself",
      url='https://github.com/jeffbuttars/upkg',
      long_description=read('README'),
      author="Jeff Buttars",
      author_email="jeff@jeffbuttars.com",
      packages=find_packages(exclude=['tests*']),
      license='GPLv2',
      package_dir={'pkgs': 'pkgs'},
      install_requires=[
          'tornado',
      ],
      data_files=[
          # ('/etc/init.d', ['']),
      ],
      )
