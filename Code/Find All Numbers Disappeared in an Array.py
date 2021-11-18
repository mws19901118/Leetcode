class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):                                          #Traverse nums.
            while nums[i] != nums[nums[i] - 1]:                             #While current number does not equal to the numebr whose index is current number - 1, swap the 2 numbers.
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [i + 1 for i, x in enumerate(nums) if x != i + 1]            #Return the index plus 1 at which the number is not index plus 1. 
