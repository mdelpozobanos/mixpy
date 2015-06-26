# -*- coding: utf-8 -*-

"""
===============================
mixpy.py
===============================

This is the main file from the mixpy package.
A couple of silly functions and classes are defined here as examples.

"""


def foo(var1, var2, long_var_name='hi'):
    """Description of the function

    Bla bla bla. I can be like this the whole day.

    :param var1: This is a type.
    :type var1: float
    :param var2: This is another var.
    :type var2: int
    :param long_var_name: Choices in brackets, default first when optional.
    :type long_var_name: {'hi', 'ho'}, optional

    :returns: Explanation. This is var1 - var2
    :rtype: float

    """
    print(long_var_name)
    return var1*var2


class Foo:
    """This class does something... or maybe not

    :param core: Function
    :type core: function

    """

    core = None
    """This is an attribute documented in the code. How cool is that?"""

    def __init__(self, core=foo):
        self.core = core

    def foo(self, var1, var2):
        """This method does something.

        :param var1: array_like
            This is a type.
        :param var2: int
            This is another var.

        :returns: Explanation
        :rtype: float
        """
        if not isinstance(var1, int):
            raise TypeError
        if not isinstance(var2, int):
            raise TypeError
        return self.core(var1, var2)