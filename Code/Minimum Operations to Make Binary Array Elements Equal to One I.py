class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0                                        #Initialize count.
        for i in range(len(nums) - 2):                   #Traverse from index 0 to len(nums) - 3.
            if not nums[i]:                              #If nums[i] is 0, flip nums[i], nums[i + 1] and nums[i + 2] then increase count.
                for j in range(i, i + 3):
                    nums[j] = 1 - nums[j]
                count += 1
        return count if nums[-1] and nums[-2] else -1    #If last 2 numbers are 1, then all the array is 1 so return count; otherwise return -1.
