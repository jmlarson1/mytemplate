from pathlib import Path


def load_tests(loader, suite, pattern):
    """
    This function implements the load_tests protocol of the python unittest
    package.  In particular, it adds to the given suite all tests for the subB
    sub-package.

    Developers and users can run tests using this indirectly via
                         python -m unittest
    to run as part of the package's full suite or via
                         python -m unittest mytemplate.subB
    to run alone.

    Parameters:
        loader - the unittest.TestLoader instance doing the loading
        suite - test suite being built at the time of call to this function
        pattern - ignored
    """
    start_dir = str(Path(__file__).resolve().parent.joinpath("tests"))

    print(f"Discover tests in {start_dir}")

    pkg_tests = loader.discover(start_dir=start_dir, pattern="Test*.py")
    suite.addTests(pkg_tests)

    return suite
