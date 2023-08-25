#!/usr/bin/env python

import os
import sys
import coverage

from pathlib import Path

import mytemplate

def print_and_abort(msg):
    """
    """
    # TODO: Add in colors
    print()
    print(msg)
    print()
    sys.exit(1)

def main():
    """
    """
    #####----- IDENTIFY DIRECTORIES & FILES
    pwd = Path.cwd()
    repo_root = Path(__file__).resolve().parents[2]

    pkg_root = repo_root.joinpath("mytemplate_pypkg")
    if not pkg_root.is_dir():
        print_and_abort(f"{pkg_root} does not exist or is not a directory")

    src_root = pkg_root.joinpath("src", "mytemplate")
    if not src_root.is_dir():
        print_and_abort(f"{src_root} does not exist or is not a directory")

    config_file = repo_root.joinpath(".coveragerc")
    if not config_file.is_file():
        print_and_abort(f"{config_file} is not a file or does not exist")

    # Use hopefully unique name to avoid clashes with other coverage runs
    data_file = pkg_root.joinpath(".coverage_mytemplate")
    if data_file.exists():
        print(f"WARNING: Deleting pre-existing coverage output file {data_file}")

    #####----- RUN FROM ROOT OF REPO
    # When coverage.py runs on this repository when the package is installed in
    # develop mode, it uses the filenames of the source files rather than the
    # symlinks.  As a result, the output file has a mixture of files inside and
    # outside the python package in the local clone, which confuses Coveralls.
    #
    # I have found by brute force experimentation that running from the root of
    # the repo asking coverage to use relative paths yields a coverage file that
    # does not confuse Coveralls.
    os.chdir(repo_root)

    # TODO: Write our own .coveragerc and delete when finished.  We do this
    # because this setting is not part of instantiating a Coverage object.

    #####----- COLLECT COVERAGE USING INSTALLED PACKAGE
    cov = coverage.Coverage(config_file=config_file, data_file=data_file)
    cov.erase()
    with cov.collect():
        mytemplate.test()
    cov.save()

    os.chdir(pwd)

    return 0

if __name__ == "__main__":
    sys.exit(main())

