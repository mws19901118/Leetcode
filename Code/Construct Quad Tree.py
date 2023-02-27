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
        mask = (1 << len(grid)) - 1                                                                                                                                                                     #Create a bit mask of all 1 for the length of n.
        binaryGrid = []                                                                                                                                                                                 #Initialize the grid in binary int format.
        for row in grid:                                                                                                                                                                                #Convert each row to its binary int.
            binary = 0
            for x in row:
                binary = (binary | x) << 1
            binaryGrid.append(binary >> 1)
        
        def build(binaryGrid: List[int], n: int, mask: int) -> 'Node':                                                                                                                                  #Build a quad tree node for a given grid in binary int format.
            value = all(x == mask for x in binaryGrid)                                                                                                                                                  #Check if all values are 1 in grid.
            isLeaf = value or all(not x for x in binaryGrid)                                                                                                                                            #Grid is leaf node if all values are 1 or all values are 0.
            if isLeaf:                                                                                                                                                                                  #If grid is leaf, instentiate the quad tree leaf node and return.
                return Node(value, isLeaf, None, None, None, None)
                
            topLeft, topRight, bottomLeft, bottomRight = [], [], [], []                                                                                                                                 #Intialize the sub grid for top left, top right, bottom left and bottom right.
            nextSize = n // 2                                                                                                                                                                           #Get the size of next level grid.
            nextMask = mask >> nextSize                                                                                                                                                                 #Compute the all 1 mask for next level.
            for i, x in enumerate(binaryGrid):                                                                                                                                                          #Traverse current grid.
                if i < half:                                                                                                                                                                            #If i is of top half, split the binary and append to top left grid and top right grid respectively.
                    topLeft.append(x >> nextSize)
                    topRight.append(x & nextMask)
                else:                                                                                                                                                                                   #Otherwise, split the binary and append to bottom left grid and bottom right grid respectively.
                    bottomLeft.append(x >> nextSize)
                    bottomRight.append(x & nextMask)
            return Node(value, isLeaf, build(topLeft, nextSize, nextMask), build(topRight, nextSize, nextMask), build(bottomLeft, nextSize, nextMask), build(bottomRight, nextSize, nextMask))          #Build 4 children nodes respectively and build current node with 4 children then return.

        return build(binaryGrid, len(grid), mask)                                                                                                                                                       #Return the result of building quad tree from top level.
