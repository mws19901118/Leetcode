#BFS solution
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        level = {0}                                                               #Use a set to store value of coin combinations in current level.
        seen = {0}                                                                #Store values which have already occurred.
        step = 0                                                                  #Record the number of coins.
        while level:
            if amount in level:                                                   #If amount is in current level, return step.
                return step
            level = {a+c for a in level for c in coins if a+c <= amount} - seen   #The values in next level are every value in current level plus every value of coins if the result is smaller than amount. Rule out the values which have already occurred.
            seen |= level                                                         #Update the values which have already occurred.
            step += 1                                                             #Increase step by 1.
        return -1                                                                 #If can't find amount, return -1.

#DP solution
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1] * (amount + 1)                                                  #Store the least coins needed to get this value(from 0 to amount), initially -1.
        dp[0] = 0                                                                 #To get 0, you don't need any coins.
        for x in range(amount):                                                   #Start traverse from 0.
            if dp[x] == 0:                                                        #If it is -1, we can't get this value by any combinations. so continue.
                continue
            for c in coins:                                                       #Check every sum of current value and coins.
                if x + c > amount:                                                #If the new sum is larger than amount, continue.
                    continue
                if dp[x + c] < 0 or dp[x + c] > dp[x] + 1:                        #If the new sum hasn't been seen before or it's number of coins is larger than current number of coins plus 1, set it to current number of coins plus 1.
                    dp[x + c] = dp[x] + 1
        return dp[amount]                                                         #Return the number of coins of amount.
