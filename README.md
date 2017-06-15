This repository is an [MCVE](https://stackoverflow.com/help/mcve)
for the following issues:
- https://github.com/JonathonReinhart/scuba/issues/77
- https://github.com/JonathonReinhart/staticx/issues/22

The problem is this:

**When `python setup.py sdist bdist_wheel` is invoked from a clean starting point, data files (identified in `package_data`), which are generated during setup.py hooks, will not be included in the wheel.**

- From a clean starting point (`git clean -fdx`) (primarily removes `mkpkg/generated_data`):
   - `python setup.py bdist_wheel` - OK
   - `python setup.py sdist` then `python setup.py bdist_wheel` - OK
   - `python setup.py sdist bdist_wheel` - BROKEN
