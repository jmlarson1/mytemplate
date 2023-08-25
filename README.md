## Repository Status

|             | Badges |
|:-----------:|:------:|
| General     | ![GitHub](https://img.shields.io/github/license/jared321/mytemplate) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) |
| Test Status | ![GitHub Action CI](https://github.com/jared321/mytemplate/actions/workflows/github-action-ci.yml/badge.svg) [![Coverage Status](https://coveralls.io/repos/github/jared321/mytemplate/badge.svg?branch=main)](https://coveralls.io/github/jared321/mytemplate?branch=main) |

## General Information
This repository is a template and testbed for setting up new repositories in the
[POptUS organization](https://github.com/POptUS).  A concrete example of such a repository is
[IBCDFO](https://github.com/POptUS/IBCDFO/tree/main), which groups together similar optimization tools.
All such repositories should satisify the following requirements

* Each distinct tool to be included in the repository shall (e.g., [subA](https://github.com/jared321/mytemplate/tree/main/subA),
  [subB](https://github.com/jared321/mytemplate/tree/main/subB)) be included in the root of the repository in a folder named after the
  tool.
* Each implementation of a tool shall be included in a dedicated folder in the
  tool's main folder with its name adhering to the convention
  * `m` - for MATLAB implementations (e.g., [subA/m](https://github.com/jared321/mytemplate/tree/main/subA/m))
  * `py` - for Python implementations (e.g., [subA/py](https://github.com/jared321/mytemplate/tree/main/subA/py))
* This repository shall be setup so that it can host as many python packages as
  desired (e.g., [mytemplate_pypkg](https://github.com/jared321/mytemplate/tree/main/mytemplate_pypkg) and
  [mytemplate2_pypkg](https://github.com/jared321/mytemplate/tree/main/mytemplate2_pypkg)).  The python code
  to be included in a package shall __not__ be developed directly within the
  python package's folder hierarchy, but rather in accord with the above
  requirements.  Inclusion within the package shall be accomplished by symlinks
  (e.g., [mytemplate_pypkg/src/mytemplate/subA](https://github.com/jared321/mytemplate/blob/main/mytemplate_pypkg/src/mytemplate/subA)).
* All python packages shall be structured in accord with the [src-layout](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout),
  with tests in the package (e.g., [mytemplate_pypkg/src/mytemplate/tests](https://github.com/jared321/mytemplate/tree/main/mytemplate_pypkg/src/mytemplate/tests) and
  [mytemplate_pypkg/src/mytemplate/subA/tests](https://github.com/jared321/mytemplate/tree/main/subA/py/tests))
* All python packages shall provide access to their version ([semantic versioning](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/?highlight=version#semantic-versioning-preferred))
  information via the command `<package>.__version__`.  See discussion
  [here](https://packaging.python.org/guides/single-sourcing-package-version/#single-sourcing-the-version) for options.
  In this repo we use a dedicated [VERSION](https://github.com/jared321/mytemplate/blob/main/mytemplate_pypkg/VERSION) file coupled with
  [setup.py](https://github.com/jared321/mytemplate/blob/main/mytemplate_pypkg/setup.py)
  and [`__init__.py`](https://github.com/jared321/mytemplate/blob/main/mytemplate_pypkg/src/mytemplate/__init__.py). 
* All python packages shall have integrated automatic unit testing that can be
  run within python via the command `<package>.test()` so that actual installations can be tested and test results can be recorded in jupyter notebooks for traceability.
* Users of the code in the repository shall be able to use the code correctly by
  cloning the repository and setting appropriate path variables correctly based
  on the languages of each tool that they plan to use.
* All public python packages shall be uploaded to [PyPi](https://pypi.org) so that users can choose
  to use the code via installation with pip and without having to clone the repository.
* The repository shall be setup so that all tests in the repository regardless
  of language can be run via a [GitHub CI Action](https://github.com/jared321/mytemplate/blob/main/.github/workflows/github-action-ci.yml)
  and potentially through private build servers.
* The repository shall be setup so that coverage of all code in python packages
  can be determined as a single coverage result with coverage results published as
  [GitHub Action artifacts](https://github.com/jared321/mytemplate/actions/runs/5979755793).
  and via coverage web server interfaces (e.g., [Coveralls](https://coveralls.io/github/jared321/mytemplate)).
* The repository shall be setup so that tested distributions of all python packages are available as
  [GitHub Action artifacts](https://github.com/jared321/mytemplate/actions/runs/5979755793).

## Developer Information
The python packages in this repository and the management of coverage reports
for the full repository are managed with [tox](https://tox.wiki/en/latest/index.html),
which can be used for CI work.  However, the same `tox` setups can be used by developers
if so desired.  This can be useful since `tox` will automatically setup and manage dedicated virtual
environments for the developer.  The following guide can be used to setup `tox` on
an individual platform and is based on the a [webinar](https://www.youtube.com/watch?v=PrAyvH-tm8E)
by Oliver Bestwalter.  I appreciate his solution as there is no need to activate any virtual environment in order to use `tox`.

Developers that would like to use `tox` should learn about the tool so that, in
particular, they understand the difference between running `tox` and `tox -r`.

Create a python virtual environment based on a desired python dedicated to
hosting `tox`
```
$ cd
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
`README.md` in the root folder of each package (e.g.,
[mytemplate_pypkg](https://github.com/jared321/mytemplate/blob/main/mytemplate_pypkg/README.md)).

## Using `tox` for Global Coverage Tasks
The python environments setup and managed at the root level of this repository are for working globally
with all coverage results generated independently by testing individual code units in the repository.
In particular, it can be used to combine these into a single file for generating global coverage reports.
As such, this is a `tox` tool layer that requires advanced manual effort.  Its primary use is with CI for
[automated report generation](https://github.com/jared321/mytemplate/blob/main/.github/workflows/github-action-ci.yml).

To use this layer, learn about and setup `tox` as described above.

No work will be carried out by default with the calls `tox` and `tox -r`.

The following commands can be run from the directory that contains this file.
* `tox -r -e aggregate -- <coverage files>`
  * Combine all given `coverage.py` coverage files into the file `.coverage`
  * For best results, none of the given files should be named `.coverage`
  * Preserve the original coverage files
* `tox -r -e report`
  * It is intended that this be run after or with `aggregate`
  * Generate a report and an HTML report for the aggregated coverage results
* `tox -r -e coveralls`
  * This is likely only useful for CI solutions
  * It is intended that this be run after or with `aggregate`
  * Send the aggegrated coverage report to Coveralls

Additionally, you can run any combination of the above such as
```
tox -r -e report,coveralls,aggregate -- <coverage files>
```
Note that `tox` will correctly and automatically run `aggregrate` before the others.

## Adding a New Python Package
* Add all subpackage implementations to the root of the repo in accord with the above requirements (e.g., [subA](https://github.com/jared321/mytemplate/tree/main/subA))
* Create a new python package in the root of the repo by copying [mytemplate_pypkg](https://github.com/jared321/mytemplate/tree/main/mytemplate_pypkg)
* Set `VERSION` to the desired starting version
* Rewrite the `README.md` file for the new package
* Adapt the contents of `tox.ini` to the new package
* Adapt the contents of `setup.py` to the new package
* Add in all subpackage implementations as symlinks in the correct subdirectory
* Incorporate the package into the [GitHub CI Action](https://github.com/jared321/mytemplate/blob/main/.github/workflows/github-action-ci.yml)
* Commit, push, and check associated GitHub CI Action log to see if constructed and integrated correctly
