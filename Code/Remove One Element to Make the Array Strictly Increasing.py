class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        last, removed = nums[0], False                                              #Initialize last number to be nums[0] and a flag determine if an element has been removed.
        for i in range(1, len(nums)):                                               #Traverse the reset of nums.
            if nums[i] > last:                                                      #If nums[i] is greater than last, array is still strictly increasing, so update last and continue.
                last = nums[i]
                continue
            if removed:                                                             #If already removed one element, return false because we cannot remove anymore.
                return False
            last = nums[i] if i < 2 or nums[i] > nums[i - 2] else nums[i - 1]       #If i < 2 or nums[i] > nums[i - 2], remove nums[i]; otherwise remove nums[i - 1].
            removed = True                                                          #Set removed to true.
        return True                                                                 #Return true at the end.
