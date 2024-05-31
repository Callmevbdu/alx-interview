#!/usr/bin/python3
"""
a function that returns a list of lists of integers representing the Pascal’s
triangle of n.
"""
def pascal_triangle(n):
    triangle = []
    if n > 0:
        for i in range(1, n + 1):
            row = []
            lastRow = 1
            for y in range(1, i + 1):
                row.append(lastRow)
                lastRow = lastRow * (i - y) // y
            triangle.append(row)
    return triangle
