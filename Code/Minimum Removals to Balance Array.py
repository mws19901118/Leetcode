class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()                                        #Sort nums.
        result = inf
        j = 0                                              #Initialize a pointer.
        for i, x in enumerate(nums):                       #Traverse nums.
            while j < len(nums) and nums[j] <= x * k:      #Suppose x is current min value, move j to the right until it reaches the end of nums[j] is greter than x * k.
                j += 1
            result = min(result, i + len(nums) - j)        #Now, we need to remove first i elements and last len(nums) - j elements.
        return result
