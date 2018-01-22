# toxTest
Example project to explore the tox tool for our buildbot setup
The purpose of this repository is to create a tox.ini that checks our production code against 
1. different virtual environments that differ in the amount of version pinning
1. different versions of the python interpreter.

The python source code of the package is the minimun needed to mock a real package to be tested.

