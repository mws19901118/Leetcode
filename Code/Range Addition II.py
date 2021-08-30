class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minX, minY = m, n
        for x, y in ops:                              #Traverse ops.
            minX, minY = min(minX, x), min(minY, y)   #Get minX and minY.
        return minX * minY                            #Return minX * minY.
