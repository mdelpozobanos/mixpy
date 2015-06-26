"""
=======
main.py
=======

This is a sub-module within the module
"""


def g_function(var1, var2, long_var_name='hi'):
    """This function does something.

    Args:
        var1 (array_like): This is a type.
        var2 (int): This is another var.
        long_variable_name ({'hi', 'ho'}, optional): Choices in brackets,
            default first when optional.

    Returns:
        describe (type): Explanation

    See Also:
        template.template.FooClass : A class example

    """
    print(long_var_name)
    return var1 + var2


class GClass:
    """
    This is a class

    Attributes:
        long_var_name (str): This is an attribute.
    """

    long_var_name = None

    def __init__(self, long_var_name='hi'):
        """
        Note that the __init__ method can be documented either here or at the
        class level docstring. Just pick one and don't mix them.

        Args:
            long_variable_name ({'hi', 'ho'}, optional) Choices in brackets,
                default first when optional.
        """
        self.long_var_name = long_var_name

    def foo(self, var1, var2):
        """This method does something.

        Args:
            var1 (array_like): This is a type.
            var2 (int): This is another var.

        Returns:
            describe (type): Explanation

        See Also:
            g_function: A function example

        """
        return g_function(var1, var2, self.long_var_name)