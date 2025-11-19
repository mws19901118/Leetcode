class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)            #Store numbers in a set.
        while original in s:     #Iterate while original is in s.
            original *= 2        #Multiply original by 2.
        return original
