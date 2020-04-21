# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        d = binaryMatrix.dimensions()                   #Get dimensions.
        m, n = d[0], d[1]
        result = -1
        p = [0, n - 1]                                  #Start traversing from top right corner.
        while p[0] < m and p[1] >= 0:
            if binaryMatrix.get(p[0], p[1]) == 1:       #If current position is 1, update result and then move left.
                result = p[1]
                p[1] -= 1
            else:                                       #Otherwise move down.
                p[0] += 1
        return result                                   #Return result.
