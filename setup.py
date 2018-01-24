#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='equations',
      version='1.0.0',
      description='Python extensible math parser for evaluating arbitrary expressions',
      url='https://github.com/b-hodges/equations',
      author='b-hodges',
      author_email="me@example.com",
      license='MIT',
      keywords='equations expressions math parsing solving',
      install_requires=['six ~= 1.11'],
      packages=find_packages())
