import os
import inspect
from typing import Callable

DEBUG_FUNCTION = True


def str_debug(v):
    """ Handling the case where a function has no string method (for example an imported c++ function)."""
    try:
        return str(v)
    except:
        return "no_str_method"


def display_parameters(func: Callable):
    """
    Decorator to display function input parameters
    :param func: function
    """
    def wrapper_display_function(*args, **kwargs):
        if DEBUG_FUNCTION:
            name = "{}.{}".format(os.path.splitext(os.path.basename(inspect.getfile(func)))[0], func.__name__)
            str_args = ", ".join([str_debug(v) for v in args] +
                                 [str(k) + "=" + str_debug(v) for k, v in kwargs.items()])
            print("*** Execution of: {}({})".format(name, str_args))
        return func(*args, **kwargs)
    return wrapper_display_function


if __name__ == "__main__":
    @display_parameters
    def a(v1, v2, v3=10, v4=18):
        pass

    a(2, v2="t", v3=12)
