r"""*Trivial fixture tests for* ``sphobjinv``.

``sphobjinv`` is a toolkit for manipulation and inspection of
Sphinx |objects.inv| files.

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    20 Mar 2019

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


import pytest

pytestmark = pytest.mark.fixture


def test_info_fixture(misc_info):
    assert True in misc_info.byte_lines


def test_populate_scratch(misc_info, scratch_path):
    scr_base = misc_info.FNames.INIT_FNAME_BASE.value

    for ext in [_.value for _ in misc_info.Extensions]:
        assert (scratch_path / "{}{}".format(scr_base, ext)).is_file(), ext


def test_sphinx_load(res_path, sphinx_load_test):
    sphinx_load_test(res_path / "objects_attrs.inv")


def test_cli_invoke(run_cmdline_test):
    # Test execution with nothing on the CLI should print help and exit ok.
    run_cmdline_test([])


def test_decomp_comp_fixture(misc_info, decomp_cmp_test):
    # This basically an identity check; tells 'cmp' to compare
    # the reference decompressed file with itself.
    decomp_cmp_test(misc_info.res_decomp_path)
