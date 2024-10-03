#!/usr/bin/python3


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of coin denominations.
        total (int): The total amount to make change for.

    Returns:
        int: Fewest number of coins needed to meet the total
    """
    if total <= 0:
        return 0

    # Initialize a dp array with total+1 values
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
