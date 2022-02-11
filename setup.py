#!/usr/bin/env python3
#

import os
from setuptools import setup


def read(fname):
    """Read a file and return the content"""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="bot",
    version="0.0.1",
    author="Seburath",
    author_email="t.me/seburath",
    description=("Template Bot"),
    license="MIT",
    keywords="bot",
    url="http://github.com/seburath/template-bot",
    packages=["bot"],  # , "tests"],
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
    ],
)
