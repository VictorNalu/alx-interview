#!/usr/bin/python3
"""
This module contains the function island_perimeter
which calculates the perimeter of an island
represented in a 2D grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D grid where 0 represents water
                                    and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:  # Land found
                # Start with 4 sides for a single land cell
                perimeter += 4

                # Check for neighboring land cells
                # and reduce perimeter accordingly
                if i > 0 and grid[i - 1][j] == 1:  # Land above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Land to the left
                    perimeter -= 2

    return perimeter
