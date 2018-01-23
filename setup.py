#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='equations',
      version='1.0.0',
      description='Python extensible math parser for evaluating arbitrary expressions',
      url='https://github.com/b-hodges/equations',
      author='BHodges',
      license='MIT',
      keywords='equations expressions math parsing solving',
      install_requires=['six'],
      packages=find_packages())
