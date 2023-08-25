"""
"""

from importlib.metadata import version

__version__ = version("mytemplate2")

from .compute import compute

#####----- Python unittest-based test framework
# Used for automatic test discovery
from .load_tests import load_tests

# Allow users to run full test suite as mytemplate2.test()
from .test import test
