class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days = divmod(n, 7)                                                                            #Get the number of weeks and days in week for n.
        return (28 + 28 + (weeks - 1) * 7) * weeks // 2 + (1 + weeks + weeks + days) * days // 2              #The first full week will save 28 dallars and each full week after will save 7 more dollars. The last non-full week will start with 1 + weeks and ends at weeks + days. So both are arithmetic array and easy to calculate.
