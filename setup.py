from setuptools import setup
import uribuilder

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='uribuilder',
    version=uribuilder.__version__,
    packages=['uribuilder',],
    long_description=long_description,
    long_description_type="text/markdown"
)
