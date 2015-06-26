"""
Test suite for mixpy.google_subpkg subpackage
"""

__author__ = 'mdelpozobanos'

import pytest
from mixpy import google_subpkg


# The following is an attribute definition
@pytest.fixture(scope='class')
def foo_obj():
    return google_subpkg.GClass()


class TestGClass():
    """Class to test the mixpy.google_subpkg.GClass class"""

    def test_main(self):
        """Allocation"""
        obj = google_subpkg.GClass('this')
        assert(isinstance(obj, google_subpkg.GClass))

    def test_foo(self, foo_obj):
        """Method foo"""
        assert(foo_obj.foo(2, 2) == 4)

    def test_foo_args(self, foo_obj):
        """Bad arg detection"""
        with pytest.raises(TypeError):
            foo_obj.foo(2, 'a')


# Test the main file
from mixpy.google_subpkg import main


def test_main_foo():
    """String describing the test"""
    assert(main.g_function(1, 2) == 3)