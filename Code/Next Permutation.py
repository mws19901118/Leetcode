class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i >= 1 and nums[i] <= nums[i - 1]:                                #Search from end to find the first element i which violate the non-ascending order from i to the end, i.e. nums[i] > nums[i - 1].
            i -= 1
        if i > 0:                                                               #If found, find the first element nums[j] which is greater than nums[i - 1] from behind.
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i - 1]:
                j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]                         #Swap nums[i - 1] and nums[j], now nums[i:] is still in non-ascending order.
        for j in range((len(nums) - i) // 2):                                   #Reverse nums[i:]
            nums[i + j], nums[-(j + 1)] = nums[-(j + 1)], nums[i + j]
