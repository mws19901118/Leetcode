class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l - 1):
            a = max(nums[i], nums[i + 1])             #Find the max value between nums[i] and nums[i + 1].
            b = min(nums[i], nums[i + 1])             #Find the min value between nums[i] and nums[i + 1].
            if i % 2 == 0:                            #If nums[i] should not be larger than nums[i + 1], set nums[i] to be b and nums[i + 1] to be a.
                nums[i] = b
                nums[i + 1] = a
            else:                                     #If nums[i] should not be smaller than nums[i + 1], set nums[i] to be a and nums[i + 1] to be b.
                nums[i] = a
                nums[i + 1] = b
