#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program reverses a list order."""


def flip_keys(to_flip):
    """This function loops through a list and reverses the order.

    Args:
        to_flip(list): List of values.

    Returns:
        to_flip(list): List of reverse order to_flip.

    Example:
        >>> flip_keys([(1, 2, 3), 'blerg'])
        [(3, 2, 1), 'grelb']
    """

    counter = 0
    for values in to_flip:
        to_flip[counter] = values[::-1]
        counter += 1

    return to_flip
