#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages


setup(name='upkg',
      version='0.1.0',
      description="Package Yourself",
      long_description=(open('README.md').read()),
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
