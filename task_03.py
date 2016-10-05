#! usr/bin/env python
# -*- coding: utf-8 -*-
"""Warmup Week3"""

import decimal


def lexicographics(to_analyze):
    """Calculate max, min and avg number of words.
    Args:
        to_analyze(str): Arg string to calculate length
    Returns:
        A tuple with max, min and average of a list of words.
    Example:
        >>> import task_03
        >>> task_03.lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        (5, 3, Decimal(4.0))
    """
    mylist = to_analyze.split('\n')
    stats = []
    for item in mylist:
        val = len(item.split())
        stats.append(val)
    return (max(stats), min(stats), sum(stats)/decimal.Decimal(len(stats)))
