class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        for i in range(1, n // 2 + 1):        #For i in [i, n // 2], append i and -i to result so they will consolidate.
            result.append(i)
            result.append(-i)
        if n & 1:                             #If n is odd, append 0 to result.
            result.append(0)
        return result
