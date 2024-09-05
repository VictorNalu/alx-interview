#!/usr/bin/python3
"""
Utf8
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Iterate over each integer (byte) in the data list
    for byte in data:
        # Get the last 8 bits (byte) of the integer
        byte = byte & 0xFF

        if num_bytes == 0:
            # Check how many bytes the UTF-8 character is supposed to be
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7):  # If it starts with 1 but doesn't match
                return False
        else:
            # The following bytes must start with 10xxxxxx
            if not (byte >> 6 == 0b10):
                return False
            num_bytes -= 1

    # If we finish checking all bytes and num_bytes is not 0, it's invalid
    return num_bytes == 0
