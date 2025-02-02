class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 0                                                                                  #Find the first index i that is valid and nums[i] > nums[i + 1].
        while i + 1 < len(nums) and nums[i + 1] >= nums[i]:
            i += 1
        return all(nums[j] <= nums[(j + 1) % len(nums)] for j in range(i + 1, len(nums)))      #Check if the rest of array is sorted and also the last number is not greater than the first number.
