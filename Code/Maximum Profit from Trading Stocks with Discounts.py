class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adjacentList = defaultdict(list)                                                                               #Initialize and populate the adjacent list.
        for u, v in hierarchy:
            adjacentList[u - 1].append(v - 1)
        
        def dfs(u: int):                                                                                               #DFS to calculate the max profit of current node and its subtree.
            cost, discountCost = present[u], present[u] // 2                                                           #Initialize cost and discount cost at current node.
            dp = [[0] * (budget + 1), [0] * (budget + 1)]                                                              #Initialize dp, dp[0][x] and dp[1][x] is the max profit given budget x with or without parent purchasing stock repsectively. 
            childProfit = [[0] * (budget + 1), [0] * (budget + 1)]                                                     #Initialize childProfit, childProfit[0][x] and childProfit[1][x] is the max profit made from all the children of current node with or without discount available respectively.
            estimate = cost

            for v in adjacentList[u]:                                                                                  #Traverse each child of current node.
                childDP, childEstimate = dfs(v)                                                                        #Get the DFS result of child.
                estimate += childEstimate                                                                              #Update estimate, which is the budget upper bound of current node and it subtree.
                for i in reversed(range(budget + 1)):                                                                  #Traverse budget backwards.
                    for j in range(min(childEstimate, i) + 1):                                                         #Traverse min(childEstimate, i) to update child profit in a 0-1 knapsack fashion.
                        if i - j >= 0:
                            childProfit[0][i] = max(childProfit[0][i], childProfit[0][i - j] + childDP[0][j])
                            childProfit[1][i] = max(childProfit[1][i], childProfit[1][i - j] + childDP[1][j])

            for i in range(budget + 1):                                                                                #Traverse budget again.
                dp[0][i], dp[1][i] = childProfit[0][i], childProfit[0][i]                                              #Populate dp[0][i] and dp[1][i] with the children profit not buying at current node thus no discount for children.
                if i >= discountCost:                                                                                  #If we can buy with discount cost at current node, update dp[1][i] if the profit of children buying with discount at budget i - discountCost plus the current node profit is higher.
                    dp[1][i] = max(childProfit[0][i], childProfit[1][i - discountCost] + future[u] - discountCost)
                if i >= cost:                                                                                          #If we can buy with cost at current node, update dp[0][i] if the profit of children buying with discount at budget i - cost plus the current node profit is higher.
                    dp[0][i] = max(childProfit[0][i], childProfit[1][i - cost] + future[u] - cost)

            return dp, estimate                                                                                        #Return the dp 2D array and estimate.

        return dfs(0)[0][0][budget]                                                                                    #Return dfs(0)[0][0][budget] because the CEO cannot buy with discount.
