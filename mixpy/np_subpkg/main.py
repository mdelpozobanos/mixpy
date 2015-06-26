"""
=======
main.py
=======

This is the main file of a sub-package within the root package
"""


def np_function(var1, var2, long_var_name='hi'):
    """This function does nothing.

    Parameters
    ----------
    var1 : array_like
        This is a type.
    var2 : int
        This is another var.
    Long_variable_name : {'hi', 'ho'}, optional
        Choices in brackets, default first when optional.

    Returns
    -------
    describe : type
        Explanation

    See Also
    --------
    template.template.FooClass : A class example

    """
    print(long_var_name)
    return var1 - var2


class NPClass:
    """
    This is a class

    Parameters
    ----------
    long_variable_name : {'hi', 'ho'}, optional
        Choices in brackets, default first when optional.

    Attributes
    ----------
    var1 : float
        This is an attribute
    """

    long_var_name = None

    def __init__(self, long_var_name='hi'):
        self.long_var_name = long_var_name

    def foo(self, var1, var2):
        """This method does something.

        Parameters
        ----------
        var1 : array_like
            This is a type.
        var2 : int
            This is another var.

        Returns
        -------
        describe : type
            Explanation

        See Also
        --------
        g_function : A function example

        """
        return np_function(var1, var2, self.long_var_name)