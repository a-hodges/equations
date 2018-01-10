#!/usr/bin/env python3

from distutils.core import setup

setup(name='equations',
      version='1.0.0',
      description='Python extensible math parser for evaluating arbitrary expressions',
      url='https://github.com/b-hodges/equations',
      author='Brian Hodges',
      license='MIT',
      keywords='equations expressions math parsing solving',
      install_requires=['six'],
      python_requires='>=2.6, ~=3.3',
      packages=['equations'])
