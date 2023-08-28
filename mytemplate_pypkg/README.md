A template python package for building in dedicated python functionality as well as combining subA and subB tools,
which we are assume share some important commonality, via symlinks.  A concrete example of this package is
[ibcdfo_pypkg](https://github.com/POptUS/IBCDFO/tree/main/ibcdfo_pypkg).

## Installation Instructions
There should be at least three options for installing this package.

#### pip install via [PyPi](https://pypi.org)
This is the preferred method for users who prefer pip installations over direct use of local clones.
* __NOTE__: This package is not in PyPi and, therefore, this method cannot be executed
* Setup the python environment that will use the package (e.g., [virtual environments](https://docs.python.org/3/library/venv.html))
* Update `pip`, `setuptools`, and `wheel` if necessary and desired
```
$ which python
$ python --version
$ which pip
$ pip --version
$ pip install --upgrade mytemplate
$ pip list
```

#### pip install via downloaded [GitHub action artifacts](https://github.com/jared321/mytemplate/actions/runs/5979755793)
This method might be useful to developers for testing/debugging or power users who would like to use a specific version of the package not available through `pypi`.
* Click on the [GitHub Action](https://github.com/jared321/mytemplate/actions) associated with the commit whose package version is to be installed
* Download the artifacts of the python package to install
* Extract the artifact and confirm that it contains distributions (`*.tar.gz` is a [source distribution](https://packaging.python.org/en/latest/flow/#the-source-distribution-sdist); `*.whl` is a [pre-built distribution](https://packaging.python.org/en/latest/flow/#the-built-distributions-wheels)) and choose which to install
```
$ pip install --upgrade </path/to/distribution to install>
$ pip list
```

#### Manual source distribution installation via [setuptools](https://setuptools.pypa.io/en/latest/index.html)
This method might be useful for developers.
* `cd /path/to/mytemplate_pypkg`
* Test manually with python or `tox`
```
$ python setup.py sdist
$ python install --upgrade dist/mytemplate-<version>.tar.gz
$ pip list
```

#### Installation Testing
Installations can be tested by running 
```
$ python
>>> import mytemplate
>>> mytemplate.__version__
'1.0.1'
>>> mytemplate.test()
    ...
$ python -m pydoc mytemplate
```

## Development with `tox`
Learn about and setup `tox` as described in the [main README](https://github.com/jared321/mytemplate/blob/main/README.md).

If the environment variable `COVERAGE_FILE` is set, then this is the coverage
file that will be used with all associated work.  If it is not specified, then
the coverage file is `.coverage_mytemplate`.

The following commands can be run from the directory that contains this file.
* `tox -r -e coverage`
  * Execute the full test suite for the package and save coverage results to the coverage file
  * The test runs the package code in the local clone rather than code installed into python so that coverage results accessed through web services such as Coveralls are clean and straightforward
* `tox -r -e nocoverage`
  * Execute the full test suite for the package using the code installed into python
* `tox -r -e subA`
  * Execute the test suite for the subA subpackage only using the code installed into python
* `tox -r -e subB`
  * Execute the test suite for the subB subpackage only using the code installed into python
* `tox -r -e report`
  * It is intended that this be run after or with coverage
  * Generate a report and an HTML report for the package's full test suite
* `tox -r -e check`
  * This is likely only useful for developers working on a local clone
  * This task should never call any tools that automatically __alter__ files
  * Run several checks on the code to report possible issues
* `tox -r -e format`
  * This is likely only useful for developers working on a local clone
  * Apply `black` to all files in the package for cleaning/standardization who want to diff the changes made by `black` before committing
  * This should __never__ be included as default `tox` work since it could alter uncommitted code under active development
* `tox -r -e testdeploy`
  * This is likely only useful for developers working on a local clone
  * Create source and wheel distributions and upload to TestPyPi for testing
  * This will require manually entering account information
  * __NOTE__: Developers should remove their `dist` directory before running
    this command to ensure that they only send the latest and greatest
    distributions rather than a potential mix of versions.

In the interest of aiding developers, running `tox` or `tox -r` will only carry out the nocoverage work.
Additionally, you can run any combination of the above such as `tox -r -e report,coverage`.

## Manual Developer Testing
It is possible to test manually outside of `tox`, which could be useful for
testing at the level of a single test.

The following example shows how to run only `TestCompareA` in `mytemplate.subA`
```
$ cd /path/to/package
$ tox -r -e nocoverage
$ . ./.tox/nocoverage/bin/activate
$ which python
$ python --version
$ pip list
$ python -m unittest mytemplate.subA.test.TestCompareA
```

