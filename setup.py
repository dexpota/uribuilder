from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='uribuilder',
    version='0.1',
    packages=['uribuilder',],
    long_description=long_description,
    long_description_type="text/markdown"
)
