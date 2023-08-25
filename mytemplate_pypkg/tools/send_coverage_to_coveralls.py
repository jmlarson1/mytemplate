#!/usr/bin/env python

import os
import sys

import subprocess as sbp

from pathlib import Path

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

    base_dir = "/home/runner/work/mytemplate/mytemplate/home/runner/work/mytemplate/mytemplate"

    os.chdir(repo_root)
    command = ["coveralls",
               "--service=github",
               f"--basedir={base_dir}"]
    sbp.run(command)
    sbp.run(["coveralls", "--finish"])
    os.chdir(pwd)

    return 0

if __name__ == "__main__":
    sys.exit(main())

