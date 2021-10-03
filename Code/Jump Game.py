class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, reach = 0, 0                         #Initialize a pointer at 0 and the farthest reachable index.
        while i <= reach:                       #Traverse nums while can reach index i.
            reach = max(reach, i + nums[i])     #Update reach if we can reach farther from current index.
            if reach >= len(nums) - 1:          #If we can reach the end, return true.
                return True
            i += 1                              #Move i to next.
        return False                            #Return false cause we cannot reach the end.
