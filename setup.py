#!/usr/bin/env python

from os.path import join, dirname
from setuptools import setup
import sys
REQUIRES = ['robotframework >= 2.6.0', 'avro']
if sys.version_info.major>=3:
    filename=join(dirname(__file__), 'AvroLibrary', 'version.py')
    exec(compile(open(filename).read(),filename, 'exec'))
    REQUIRES.append('avro-python3')
else:
    execfile(join(dirname(__file__), 'AvroLibrary', 'version.py'))

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
          "Topic :: Software Development :: Testing"
      ],
      install_requires = REQUIRES,
      packages    = ['AvroLibrary'],
      )
