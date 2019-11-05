#!/usr/bin/env python

from os.path import join, dirname, abspath
from setuptools import setup
import sys

CURDIR = dirname(abspath(__file__))
with open(join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

if sys.version_info.major >= 3:
    filename=join(CURDIR, 'AvroLibrary', 'version.py')
    exec(compile(open(filename).read(), filename, 'exec'))
    REQUIREMENTS.append('avro-python3')
else:
    execfile(join(CURDIR, 'AvroLibrary', 'version.py'))

DESCRIPTION = """
Avro support for Robot Framework.
"""[1:-1]

setup(name         = 'robotframework-avrolibrary',
      version      =  VERSION,
      description  = 'Avro library for Robot Framework',
      long_description = DESCRIPTION,
      author       = 'Marcin Mierzejewski',
      author_email = '<mmierz@gmail.com>',
      url          = 'https://github.com/s4int/robotframework-AvroLibrary',
      license      = 'Apache License 2.0',
      keywords     = 'robotframework testing avro kafka',
      platforms    = 'any',
      classifiers  = [
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 3",
          "Topic :: Software Development :: Testing",
          "Framework :: Robot Framework",
          "Framework :: Robot Framework :: Library",
      ],
      install_requires = REQUIREMENTS,
      packages    = ['AvroLibrary'],
      )
