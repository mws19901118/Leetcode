class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        downTwo, downOne = 0, cost[0]                                       #Initalize the min cost to stand on down 2 steps and down 1 step, respectively.
        cost.append(0)                                                      #Add a virtual step at the top of the floor with cost 0.
        for i in range(1, len(cost)):                                       #Traverse the cost from 2nd step.
            downTwo, downOne = downOne, min(downOne, downTwo) + cost[i]     #New downOne = min(downOne, downTwo) + cost[i]; while new downTwo = downOne.
        return downOne                                                      #Return downOne.
