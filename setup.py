#!/usr/bin/env python3
# vim:set ff=unix expandtab ts=4 sw=4:
from setuptools import setup, find_packages
def readme():
    with open('README.md') as f:
        return f.read()

setup(name='toxTest',
        version='1.0',
        description='explore tox ',
        long_description=readme(),#avoid duplication 
        author='Markus Müller',
        author_email='mamueller@bgc-jena.mpg.de',
        packages=find_packages(), #find all packages (multifile modules) recursively
        classifiers = [
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: POSIX :: Linux",
        "Topic :: Education "
        ],
        # setuptools should not be bothered with explicit versions, those will be specified in
        # for pip in  requirements.txt
        install_requires=[
            "sympy",
        ],
        # to hopefully make RTD work
        include_package_data=True,
        zip_safe=False)

