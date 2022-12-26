class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0                               #Initialize the farthest reachable index.
        for i, x in enumerate(nums):            #Traverse nums.
            if i > reach:                       #If current index is beyond reach, return false.
                return False
            reach = max(reach, i + nums[i])     #Update reach if we can reach farther from current index.
        return True                             #Return true after traverse.
