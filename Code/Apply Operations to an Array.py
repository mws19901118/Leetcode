class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):        #Traverse from 0 to n - 1 and apply operations.
            if nums[i] == nums[i + 1]:
                nums[i] <<= 1
                nums[i + 1] = 0
        index = 0
        for x in nums:                        #Shift non zero numbers towards left.
            if x:
                nums[index] = x
                index += 1
        for i in range(index, len(nums)):     #Set the rest of list to 0.
            nums[i] = 0
        return nums
