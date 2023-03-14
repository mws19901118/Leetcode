class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        result = 0
        i = 0
        while i < len(nums):                                                        #Traverse nums with 2 pointers.
            j = 1
            while i + j < len(nums) and nums[i + j] > nums[i + j - 1]:              #Find the a strictly increasing subarray as long as possible.
                j += 1
            result += (1 + j) * j // 2                                              #For a strictly increasing subarray of length j, there are total (1 + j) * j // 2 increasing subarrays.
            i += j
        return result
