r"""*Test(s) to ensure full loading of flake8 extensions*.

``sphobjinv`` is a toolkit for manipulation and inspection of
Sphinx |objects.inv| files.

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    27 Apr 2019

**Copyright**
    \(c) Brian Skinn 2016-2019

**Source Repository**
    http://www.github.com/bskinn/sphobjinv

**Documentation**
    http://sphobjinv.readthedocs.io

**License**
    The MIT License; see |license_txt|_ for full license terms

**Members**

"""

import re
import subprocess as sp  # noqa: S404
import sys
from pathlib import Path

import pytest


@pytest.mark.skipif(
    sys.version_info < (3, 6),
    reason="Some flake8 extensions require Python 3.6 or later",
)
def test_flake8_version_output(subtests):
    """Confirm that all desired plugins actually report as loaded."""
    p_pkgname = re.compile("^[0-9a-z_-]+", re.I)
    plugins = Path("requirements-flake8.txt").read_text().splitlines()[1:]
    plugins = [p_pkgname.search(p).group(0) for p in plugins]

    # This is fragile if anything ends up not having a prefix that needs
    # stripping
    plugins = [p.partition("-")[-1] for p in plugins]

    flake8_ver_output = sp.check_output(  # noqa: S607,S603
        ["flake8", "--version"], universal_newlines=True
    )  # noqa: S607,S603

    for i, p in enumerate(plugins):
        with subtests.test(msg=p, i=i):
            assert p in flake8_ver_output