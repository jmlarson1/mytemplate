A template python package for exploring what tools I want and how to use them.

## Installation Instructions

#### Generic installations

#### Site-specific instructions

Installations can be tested by running 
```
$ python
>>> import mytemplate
>>> mytemplate.__version__
'1.0.1'
>>> mytemplate.test()
```

Install the Default Developer Environment
=========================================
* Let `/path/to/python` be the python that you would like to use to build your
  developer virtual environments.
* Setup a functioning version of `tox`
```
$ deactivate
$ /path/to/python --version
$ /path/to/python -m venv $HOME/.toxbaseQ
$ ./.toxbase/bin/pip list
$ ./.toxbase/bin/python -m pip install --upgrade pip
$ ./.toxbase/bin/pip install --upgrade setuptools
$ ./.toxbase/bin/pip install tox
$ ./.toxbase/bin/tox --version
```
* Put `tox` into path for use across all development environments that we might
  have on our system.  In the following, please replace `.bash_profile` with the
  appropriate shell configuration file.
```
$ mkdir $HOME/local/bin
$ ln -s $HOME/.toxbase/bin/tox $HOME/local/bin/tox
$ vi $HOME/.bash_profile (add $HOME/local/bin to PATH)
$ source $HOME/.bash_profile
$ which tox
$ tox --version
```

