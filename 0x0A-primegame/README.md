# Prime Game

## Overview

This project involves a competitive game scenario between two players, Maria and Ben, who take turns removing prime numbers and their multiples from a set of consecutive integers. The objective is to determine the winner of the game based on optimal play strategies.

## Game Rules

- The game is played in multiple rounds.
- In each round, players are given a set of consecutive integers starting from 1 up to and including `n`.
- Maria always goes first.
- Players take turns choosing a prime number from the set and removing that number and its multiples.
- The player who cannot make a move loses the game.

## Requirements

- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS
- **Python Version**: 3.4.3
- **Style Guide**: PEP 8 (version 1.7.x)
- All files must end with a new line and be executable.
- A `README.md` file is mandatory at the root of the project folder.

## Implementation

The solution leverages the following concepts:

- **Prime Numbers**: Efficient identification of prime numbers within a range.
- **Sieve of Eratosthenes**: An algorithm to find all prime numbers up to a given limit.
- **Game Theory**: Understanding optimal play strategies and win conditions.
- **Dynamic Programming/Memoization**: Optimizing calculations for multiple game rounds.

## Function Prototype

```python
def isWinner(x, nums):
    """
    Determine the winner of the game.

    Parameters:
    x (int): The number of rounds.
    nums (list): An array of integers representing the upper limit of each round.

    Returns:
    str: The name of the player that won the most rounds, or None if the winner cannot be determined.
    """

