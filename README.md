This repository is an [MCVE](https://stackoverflow.com/help/mcve)
for the following issues:
- https://github.com/JonathonReinhart/scuba/issues/77
- https://github.com/JonathonReinhart/staticx/issues/22

## Open issues
- https://github.com/pypa/setuptools/issues/1064

## Problem statement

**When `python setup.py sdist bdist_wheel` is invoked from a clean starting
point, data files (identified in `package_data`), which are generated during
setup.py hooks, will not be included in the wheel.**

- From a clean starting point (`git clean -fdx`) (primarily removes
  `mkpkg/generated_data`):
   - `python setup.py bdist_wheel` - OK
   - `python setup.py sdist` then `python setup.py bdist_wheel` - OK
   - `python setup.py sdist bdist_wheel` - BROKEN

## Steps to reproduce

First:
- Run `git clean -fdx` -- remove any generated files
- Run `python setup.py sdist bdist_wheel`
- Observe only the following line in the output:
   - `copying build/lib/mypkg/__init__.py -> build/bdist.linux-x86_64/wheel/mypkg`
- Run `unzip -l dist/mypkg-1.2.3-py2-none-any.whl`
   - Observe that `mypkg/generated_data` is **missing** from the wheel

Now that `mypkg/generated_data` is present:
- Run `python setup.py sdist bdist_wheel` again
- Observe the following lines in the output:
    - `copying build/lib/mypkg/generated_data -> build/bdist.linux-x86_64/wheel/mypkg`
    - `copying build/lib/mypkg/__init__.py -> build/bdist.linux-x86_64/wheel/mypkg`
- Run `unzip -l dist/mypkg-1.2.3-py2-none-any.whl`
   - Observe that `mypkg/generated_data` is **now present** in the wheel

Clean the directory, and run other variations of `sdist` and `bdist_wheel` (as
mentioned above) and observe that the problem does not manifest.

## Workarounds that do *not* work
- Hooking `build_py` instead of `build`
