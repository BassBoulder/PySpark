"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining"""
    
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_bake_time                   

PREPERATION_TIME = 2

def preparation_time_in_minutes(number_of_layers):
    """Calculate the elapsed cooking time"""

    return PREPERATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate elapsed time"""
    total_preparation_time = number_of_layers * 2
    total_elapsed_time = total_preparation_time + elapsed_bake_time

    return total_elapsed_time
