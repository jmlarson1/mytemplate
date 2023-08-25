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
$ pip install mytemplate
$ pip list
```

#### pip install via downloaded [GitHub action artifacts](https://github.com/jared321/mytemplate/actions/runs/5979755793)
This method might be useful to developers for testing/debugging or power users who would like to use a specific version of the package not available through `pypi`.
* Click on the [GitHub Action](https://github.com/jared321/mytemplate/actions) associated with the commit whose package version is to be installed
* Download the artifacts of the python package to install
* Extract the artifact and confirm that it contains distributions (`*.tar.gz` is a [source distribution](https://packaging.python.org/en/latest/flow/#the-source-distribution-sdist); `*.whl` is a [pre-built distribution](https://packaging.python.org/en/latest/flow/#the-built-distributions-wheels)) and choose which to install
* `pip install --upgrade </path/to/distribution to install>`

#### Manual source distribution installation via [setuptools](https://setuptools.pypa.io/en/latest/index.html)
This method might be useful for developers.
* `cd /path/to/mytemplate_pypkg`
* Test manually with python or `tox`
```
$ python setup.py sdist
$ python dist/mytemplate-<version>.tar.gz
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
