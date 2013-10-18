#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages


setup(name='pkgs',
      version='1.0.0',
      description="Package Manage Yourself",
      author="Jeff Buttars",
      author_email="jeff@jeffbuttars.com",
      packages=find_packages(),
      license='GPLv2',
      package_dir={'pkgs': 'pkgs'},
      install_requires=[
          'tornado',
      ],
      data_files=[
          # ('/etc/init.d', ['']),
      ],
     )
