class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()            #Sort costs.
        count = 0               #Initialize count.
        for x in costs:         #Traverse costs.
            if x > coins:       #If x > coins, cannot buy anymore, so break.
                break
            coins -= x          #Buy current bar.
            count += 1          #Increase count.
        return count