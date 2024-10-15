#!/usr/bin/python3


def sieve_of_eratosthenes(max_num):
    """Generate a list of booleans representing
    prime status of numbers up to max_num."""
    is_prime = [True] * (max_num + 1)
    p = 2
    while (p * p <= max_num):
        if (is_prime[p]) is True:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime numbers
    return is_prime


def isWinner(x, nums):
    """Determine the winner of the game."""
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    is_prime = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = sum(is_prime[1:n+1])
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
