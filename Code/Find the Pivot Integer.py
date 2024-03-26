class Solution:
    def pivotInteger(self, n: int) -> int:
        totalSum = n * (n + 1) // 2                                                      #Calculate the total sum from 1 to n.
        return int(sqrt(totalSum)) if sqrt(totalSum) == ceil(sqrt(totalSum)) else -1     #If x is the pivot integer, then (1 + x) * x // 2 == (totalSum + x) // 2.
                                                                                         #It basically means that x, if exists, has to be the integer square root of totalSum.
