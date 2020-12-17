class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        countAB = defaultdict(int)
        result = 0
        for a in A:                                 #Count the sum of a + b for a in A and b in B.
            for b in B:
                countAB[a + b] += 1
        for c in C:                                 #For each c in C and d in D, add countAB[
            for d in D:
                result += countAB[-(c + d)]         #Add the count of -(c + d) in countAB to result.
        return result
