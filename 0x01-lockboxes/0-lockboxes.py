#!/usr/bin/python3
"""
This module calculates if lockboxes
can be opened.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of list): List of lists, where each list contains
                              keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = set()
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()
        if current_box not in opened:
            opened.add(current_box)
            for key in boxes[current_box]:
                if key < n and key not in opened:
                    stack.append(key)

    return len(opened) == n
