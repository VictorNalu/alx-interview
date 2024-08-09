#!/usr/bin/python3
"""
This module calculate n pascal triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the last row of the triangle
        new_row = [1]  # Start the new row with 1
        for j in range(1, i):
            # Compute the value by summing the two values above it
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # End the row with 1
        triangle.append(new_row)

    return triangle
