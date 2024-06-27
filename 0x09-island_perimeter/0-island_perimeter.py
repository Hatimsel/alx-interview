#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    def is_water_or_outside(i, j):
        """Determines if the surface is water or ground"""
        return i < 0 or j < 0 or i >= len(grid) or\
            j >= len(grid[0]) or grid[i][j] == 0

    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if is_water_or_outside(i-1, j):
                    perimeter += 1
                if is_water_or_outside(i+1, j):
                    perimeter += 1
                if is_water_or_outside(i, j-1):
                    perimeter += 1
                if is_water_or_outside(i, j+1):
                    perimeter += 1

    return perimeter
