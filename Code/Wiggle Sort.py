class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            if (nums[i + 1] < nums[i] and not i & 1) or (nums[i + 1] > nums[i] and i & 1):    #If i is even and nums[i] > nums[i + 1] or i is odd and nums[i] < nums[i + 1], swap nums[i] and nums[i + 1].
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
