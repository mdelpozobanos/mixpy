#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_mixpy
----------------------------------

Tests for `mixpy` module.
"""

import pytest
from mixpy import mixpy


def test_foo():
    """String describing the test"""
    assert(mixpy.foo(1, 2) == 2)


# The following is an attribute definition
@pytest.fixture(scope='class')
def foo_obj():
    return mixpy.Foo(mixpy.foo)


class TestFoo():
    """Class to test the mixpy.Foo class"""

    def test_main(self):
        """Allocation"""
        mixpy.Foo(mixpy.foo)

    def test_foo(self, foo_obj):
        """Method foo"""
        assert(foo_obj.foo(2, 2) == 4)

    def test_foo_args(self, foo_obj):
        """Bad arg detection"""
        with pytest.raises(TypeError):
            foo_obj.foo(2, 'a')