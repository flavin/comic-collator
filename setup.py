#!/usr/bin/env python
from os import path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="comic-collator",
    version="0.1",
    description="collate image files and concat images ready to print.",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Francisco Lavin",
    packages=["comiccollator"],
    install_requires=["Pillow"],
    scripts=[],
    test_suite="tests",
    entry_points={
          'console_scripts': [
              'comiccollator = comiccollator.__main__:main'
          ]
      },
)
