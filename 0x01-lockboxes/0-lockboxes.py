#!/usr/bin/python3
def canUnlockAll(boxes):
    # Create a set to store the keys we have
    keys = set([0])

    # Iterate while we have keys
    while keys:
        # Take a key from the set
        key = keys.pop()

        # If the key corresponds to a box
        if key < len(boxes):
            # Open the box and add the keys to our set
            keys.update(boxes[key])

            # Empty the box
            boxes[key] = []

    # Check if all boxes are empty (i.e., all boxes have been opened)
    return all(not box for box in boxes)

