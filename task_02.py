#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Warm up Task 02"""


def bool_to_str(bval):
    """Determine if the passed value is truthy or falsy.
    Args:
        bool_to_str(bool): Arg that is evaluated for truthiness or falsiness.
    Returns:
       Yes or No depending on truthiness or falsiness.
    Examples:
        >>> import task_02
        >>> task_02.bool_to_str(True)
        'Yes'
        >>> import task_02
        >>> task 02.bool_to_str('')
        'No'
    """
    mybool = ''
    if bval:
        mybool = 'Yes'
    else:
        mybool = 'No'
    return mybool
