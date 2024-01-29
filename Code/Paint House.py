class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [[0, 0, 0]]                                                                                                                #Initialize dp of min cost to paint houses so far.
        for x in costs:                                                                                                                 #Traverse costs.
            dp.append([x[0] + min(dp[-1][1], dp[-1][2]), x[1] + min(dp[-1][0], dp[-1][2]), x[2] + min(dp[-1][0], dp[-1][1])])           #For each color, the cost is paint current house this color plus the min cost of the other 2 colors in previous dp. 
        return min(dp[-1])                                                                                                              #Return the min(dp[-1])
