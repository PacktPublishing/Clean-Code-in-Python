from setuptools import find_packages, setup

with open("README.rst", "r") as longdesc:
    long_description = longdesc.read()


install_requires = ["sanic"]

setup(
    name="web",
    description="Library with helpers for the web-related functionality",
    long_description=long_description,
    author="Dev team",
    version="0.1.0",
    packages=find_packages(where="src/"),
    package_dir={"": "src"},
    install_requires=install_requires,
)
