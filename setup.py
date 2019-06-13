from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

setup(
    name="maas-uservice",
    version="0.1.0",
    description="Math as a micro-service",
    long_description="",
    url="https://github.com/b2wads/maas",
    # Author details
    author="Dalton Barreto",
    author_email="daltonmatos@gmail.com",
    license="MIT",
    classifiers=["Programming Language :: Python :: 3.7"],
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=[],
    entry_points={},
)
