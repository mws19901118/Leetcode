class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:                                                                             #Get n and k.
        n, k = len(costs), len(costs[0])
        minCost = [[0 for _ in range(k)]] + [[float('inf') for _ in range(k)] for _ in range(n)]                                    #Initialize a minCost matrix; minCost[i + 1][j] means the min cost so far until painting house i with color j. It has a dummy first row representing a virtual house.
        firstMinCost, secondMinCost = 0, 0                                                                                          #Initialize the min cost and second min cost of painting previous house.
        for i in range(1, n + 1):                                                                                                   #Traverse houses.
            newFirstMinCost, newSecondMinCost = float('inf'), float('inf')                                                          #Initialize the min cost and second min cost of painting current house.
            for j in range(k):                                                                                                      #Traverse each color.
                minCost[i][j] = (secondMinCost if minCost[i - 1][j] == firstMinCost else firstMinCost) + costs[i - 1][j]            #If minCost[i - 1][j] == firstMinCost, we cannot paint current house with same color, so use secondMinCost; otherwise use firstMinCost. Then plus costs[i - 1][j] to paint color j. 
                if minCost[i][j] <= newFirstMinCost:                                                                                #Update newFirstMinCost if necessary.
                    newSecondMinCost = newFirstMinCost
                    newFirstMinCost = minCost[i][j]
                elif minCost[i][j] <= newSecondMinCost:                                                                             #Update newSecondMinCost if necessary.
                    newSecondMinCost = minCost[i][j]
            firstMinCost, secondMinCost = newFirstMinCost, newSecondMinCost                                                         #Replace firstMinCost and secondMinCost with newFirstMinCost and newSecondMinCost to go to next house.
        return firstMinCost                                                                                                         #Return firstMinCost as it is the min cost of painting last house.
