class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer, i = 0, 0                                       #Initialize pointer and i.
        while i < len(nums):                                    #Traverse nums.
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:         #Find the end of duplicate of current number.
                j += 1
            nums[pointer] = nums[i]                             #Set nums[pointer] to current number.
            pointer += 1                                        #Increase pointer.
            i = j                                               #Move i forward.
        return pointer                                          #Return pointer.
