class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0                                    #Initialize index to put current number.
        for x in nums:                               #Traverse nums.
            if x != 0:                               #If current number is not 0, put it on index and move forward index.
                nums[index] = x
                index += 1
        for i in range(index, len(nums)):            #Set all number in nums[index:] to 0.
            nums[i] = 0
