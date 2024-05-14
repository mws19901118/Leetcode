# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()          #Get the dimensions.
        result = -1
        x, y = 0, cols - 1                              #Start traversing from top right corner.
        while x < rows and y >= 0:
            if binaryMatrix.get(x, y):                  #If current position is 1, update result and then move left.
                result = y
                y -= 1
            else:                                       #Otherwise move down.
                x += 1
        return result                                   #Return result.
