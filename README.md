Repository Status
=================

|             | Badges |
|:-----------:|:------:|
| Test Status | ![GitHub Action CI](https://github.com/jared321/mytemplate/actions/workflows/github-action-ci.yml/badge.svg) [![Coverage Status](https://coveralls.io/repos/github/jared321/mytemplate/badge.svg?branch=main)](https://coveralls.io/github/jared321/mytemplate?branch=main) |

General Information
===================

This repository is a template and testbed for setting up new repositories in the
POptUS organization.  All such repositories should satisify the following
requirements

* Each distinct tool to be included in the repository shall (e.g., `subA`,
  `subB`) be included in the root of the repository in a folder named after the
  tool.
* Each implementation of a tool shall be included in a dedicated folder in the
  tool's main folder with its name adhering to the convention
  * `m` - for MATLAB implementations
  * `py` - for Python implementations
* This repository shall be setup so that it can host as many python packages as
  desired (e.g., `mytemplate_pypkg` and `mytemplate2_pypkg`).  The python code
  to be included in a package shall *not* be developed directly within the
  python package's folder hierarchy, but rather in accord with the above
  requirements.  Inclusion within the pacakge shall be accomplished by symlinks
  (e.g., `mytemplate_pypkg/src/mytemplate/subA`).
* All python packages shall be structured in accord with the src-layout, but
  with tests in the package (e.g., `mytemplate_pypkg/src/mytemplate/tests`)
* All python packages shall provide access to their version (semantic
  versioning) information via the command `<pacakge>.__version__`.
* All python packages shall have integrated automatic unit testing that can be
  run within python via the command `<pacakge>.test()`.
* Users of the code in the repository shall be able to use the code correctly by
  cloning the repository and setting appropriate path variables correctly based
  on the languages of each tool that they plan to use.
* All public python packages shall be uploaded to PyPi so that users can choose
  to use the code without having to clone the repository.
* The repository shall be setup so that all tests in the repository regardless
  of language can be run via a GitHub CI Action and potentially through an
  private build servers.
* The repository shall be setup so that coverage of all code in python packages
  can be determined as a single coverage result with coverage results published
  as GitHub Action artifacts and via coverage web server interfaces (e.g.,
  Coveralls).

Developer Information
=====================

The python packages in this repository and the management of coverage reports
for the full repository are managed with tox, which can be used for CI work.
However, the same tox setups can be used be developers if so desired.  This can
be useful since `tox` will automatically setup and manage dedicated virtual
environments for the developer.  The following guide can be used to setup tox on
an individual platform and is based on the XXX.

Developers that would like to use `tox` should learn about the tool so that, in
particular, they understand the difference between running `tox` and `tox -r`.

Create a python virtual environment based on a desired python dedicated to
hosting tox
```
$ deactivate
$ /path/to/desired/python --version
$ /path/to/desired/python -m venv $HOME/.toxbase
$ ./.toxbase/bin/pip list
$ ./.toxbase/bin/python -m pip install --upgrade pip
$ ./.toxbase/bin/pip install --upgrade setuptools
$ ./.toxbase/bin/pip install tox
$ ./.toxbase/bin/tox --version
```

Setup `tox` in `PATH` for use across all development environments that we might
have on our system. In the following, please replace `.bash_profile` with the
appropriate shell configuration file.
```
$ mkdir $HOME/local/bin
$ ln -s $HOME/.toxbase/bin/tox $HOME/local/bin/tox
$ vi $HOME/.bash_profile (add $HOME/local/bin to PATH)
$ source $HOME/.bash_profile
$ which tox
$ tox --version
```

For information on using `tox` with a particular python package refer to the
`README.md` in the root folder of each package.

Using `tox` for Global Coverage Tasks
=====================================
