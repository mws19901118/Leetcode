class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ends = [0] * len(nums)                                          #Store the ends of special subarray starting at each index.
        i = 0
        while i < len(nums):                                            #Traverse nums.
            j = i + 1
            while j < len(nums) and nums[j] & 1 != nums[j - 1] & 1:     #Move forward j until nums[i:j] is not special.
                j += 1
            for k in range(i, j):                                       #So for all index in nums[i:j], the end of special array is j - 1.
                ends[k] = j - 1
            i = j                                                       #Move i to j.
        return [y <= ends[x] for x, y in queries]                       #For all queries x and y, result is true if y <= end[x].
