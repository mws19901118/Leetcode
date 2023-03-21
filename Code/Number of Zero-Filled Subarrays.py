class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i = 0
        count = 0
        while i < len(nums):                            #Traverse nums using 2 pointers.
            if nums[i] != 0:                            #If nums[i] is not 0, increase i and continue.
                i += 1
                continue
            j = i                                       #Find the max lengh of current zero-filled subarray.
            while j < len(nums) and nums[j] == 0:
                j += 1
            count += (j - i) * (j - i + 1) // 2         #Calculate total subarrays with in currey zero-filled subarry and increase count.
            i = j
        return count
