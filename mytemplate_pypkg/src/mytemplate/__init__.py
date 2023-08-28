"""
"""

try:
    from importlib.metadata import version
except ModuleNotFoundError:
    # Try backport
    from importlib_metadata import version

__version__ = version("mytemplate")

from .compute import compute

#####----- Python unittest-based test framework
# Used for automatic test discovery
from .load_tests import load_tests

# Allow users to run full test suite as mytemplate.test()
from .test import test
