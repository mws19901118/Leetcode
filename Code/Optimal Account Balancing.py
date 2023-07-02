class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = collections.defaultdict(int)                                    #Initialize final balances for each person.
        for x, y, amount in transactions:                                         #Traverse transcations and update balance.
            balance[x] += amount
            balance[y] -= amount
        
        unsettled = [amount for amount in balance.values() if amount]             #Filter out unsettled balances.

        @cache                                                                    #Cache result.                        
        def dfs(mask: int) -> int:                                                #DFS to find the max number of subgroups whose balance can be settled in current group.
            if not mask:                                                          #If mask is 0, means no balance in current group, return 0.
                return 0
            balanceSum, result = 0, 0                                             #Initialize balance sum of current group and result.          
            for i in range(len(unsettled)):                                       #Traverse all unsettled balance.
                currentMask = 1 << i                                              #Calculate mask for current balance.
                if mask & currentMask:                                            #If mask & currentMask, current balance is in current group.
                    balanceSum += unsettled[i]                                    #Add its balance to balanceSum.
                    result = max(result, dfs(mask ^ currentMask))                 #Keep DFS to calculate the result of removing current balance from current group and update result.

            return result + (balanceSum == 0)                                     #If balanceSum is 0, increase 1 to result and return because current group is already settled and removing a non zero balance will break it so the removed balance must belongs to a settled subgroup.
        
        return len(unsettled) - dfs((1 << len(unsettled)) - 1)                    #The reason is that a settled group x balances needs x - 1 transactions to settle, so overall minimum transactions needed is the length of unsettled balance substract DFS result of all balances in one group.
