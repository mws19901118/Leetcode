class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        lastReach=0                                         #Record the max index last step can reach.
        currentReach=0                                      #Record the max index current step can reach.
        steps=0
        i=0                                                 #Record current index.
        while currentReach<len(nums)-1:
            while i<=lastReach:                             #Only consider the incresement between current step and last step.
                currentReach=max(currentReach,i+nums[i])    #Update currentReach.
                i+=1                                        
            if currentReach==lastReach:                     #If current step can't reach further than last step, return -1.
                return -1
            else:
                steps+=1
                lastReach=currentReach                      #Set lastReach as currentReach.
        return steps
