class Solution:
    def jump(self, nums: List[int]) -> int:
        lastReach, reach, count = -1, 0, 0                      #Initialize the max index previous step can reach, current step can reach and step count.
        while lastReach < reach and reach < len(nums) - 1:      #Traverse while can reach further.
            farReach = 0
            for i in range(lastReach + 1, reach + 1):           #Calculate the farest reach.
                farReach = max(farReach, i + nums[i])
            count += 1                                          #Increase count.
            lastReach, reach = reach, farReach                  #Set lastReach to be reach and reach to be farReach.
        return count                                            #Return count.
