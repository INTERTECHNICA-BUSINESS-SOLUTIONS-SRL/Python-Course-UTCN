"""This module allows calculation of minimum and maximum values 
from a collection of values.

It exports the min_value function for calculation of minimum values and 
max_value function for calculation of the maximum value.
"""

# define a series of non-standard variables private to the module
_VERSION = 1
_SUBVERSION = 0
_RELEASE_DATE = "01/08/2023"

def min_value(values):
    """Retrieves the minimal value from a collection of values
    """

    # initialize data
    current_min_value = None

    # determine the minimum value
    for value in values :
        if current_min_value is None :
            current_min_value = value
        elif current_min_value > value :
            current_min_value = value

    return current_min_value

def max_value(values):
    """Retrieves the maximal value from a collection of values
    """

    # initialize data
    current_max_value = None

    # determine the maximum value
    for value in values :
        if current_max_value is None :
            current_max_value = value
        elif current_max_value < value :
            current_max_value = value

    return current_max_value