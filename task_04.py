#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program uses a function to loop through a tuple or list."""


def process_data(data):
    """This function loops through the data and calculates sum and average of a
    tuple.

    Args:
        data(): List or tuple of integers.

    Returns:
        total, average(tuple): Tuple of total and average

    Example:
        >>> process_data([1, 2, 3])
        (6, 2.0)
    """

    total = 0
    for values in data:
        total += values
        average = total/float(len(data))

    return total, average
