#!/usr/bin/python3


"""
Module for determining the fewest number of coins needed to meet a given total.
"""


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins = sorted(coins, reverse=True)
    change = 0

    # Iterate through each coin
    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            # Use as many of this coin as possible
            change += total // coin
            total %= coin

    # If total is 0, return the number of coins used, otherwise return -1
    return change if total == 0 else -1
