class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i = 0                                                                    #Starting from 0, find the end of the strictly increasing subarray.
        while i + 1 < len(nums) and nums[i + 1] > nums[i]:
            i += 1
        if i == 0 or i >= len(nums) - 2:                                         #If no such subarray or it doesn't leave enough space for the rest of trionic array, return false.
            return False
        j = i                                                                    #Starting from i, find the end of the strictly decreasing subarray.
        while j + 1 < len(nums) and nums[j + 1] < nums[j]:
            j += 1
        if j == i or j >= len(nums) - 1:                                         #If no such subarray or it doesn't leave enough space for the rest of trionic array, return false.
            return False
        return all(nums[k] > nums[k - 1] for k in range(j + 1, len(nums)))       #Return if the rest of the list is an increasing subarray.
