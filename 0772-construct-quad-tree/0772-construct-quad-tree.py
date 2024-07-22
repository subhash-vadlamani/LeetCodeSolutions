"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        grid_dimension = len(grid)
        grid_start_value = grid[0][0]
        grid_is_same = True
        if grid_start_value:
            value = True
        else:
            value = False

        if grid_dimension == 1:
            return Node(val = value, isLeaf=True, topLeft = None, topRight = None, bottomLeft = None, bottomRight = None)

        for i in range(0, grid_dimension):
            for j in range(0, grid_dimension):
                current_grid_value = grid[i][j]

                if current_grid_value != grid_start_value:
                    grid_is_same = False
                    break
            if not grid_is_same:
                break
        if grid_is_same:
            return Node(val = value, isLeaf=True, topLeft = None, topRight = None, bottomLeft = None, bottomRight = None)
        else:
            new_grid_dimension = grid_dimension//2
            topLeftGrid = [row[:new_grid_dimension] for row in grid[:new_grid_dimension]]
            topRightGrid = [row[new_grid_dimension:] for row in grid[:new_grid_dimension]]
            bottomLeftGrid = [row[:new_grid_dimension] for row in grid[new_grid_dimension:]]
            bottomRightGrid = [row[new_grid_dimension:] for row in grid[new_grid_dimension:]]

            topLeft = self.construct(topLeftGrid)
            topRight = self.construct(topRightGrid)
            bottomLeft = self.construct(bottomLeftGrid)
            bottomRight = self.construct(bottomRightGrid)

            # topLeft = self.construct(grid[:grid_dimension//2][:grid_dimension//2])
            # topRight = self.construct(grid[:grid_dimension//2][grid_dimension//2:])
            # bottomLeft = self.construct(grid[grid_dimension//2:][:grid_dimension//2])
            # bottomRight = self.construct(grid[grid_dimension//2:][grid_dimension//2:])

            return Node(val = value, isLeaf=False, topLeft = topLeft, topRight = topRight, bottomLeft = bottomLeft, bottomRight = bottomRight)
        