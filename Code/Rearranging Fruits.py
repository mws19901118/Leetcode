class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count = Counter()                                                    #Count each cost's offset from being consolidated by 2 baskets.
        min_v = min(min(basket1), min(basket2))                              #Calculate the min cost in both baskets.
        for x in basket1:                                                    #Traverse basket1 and increase the count of each cost.
            count[x] += 1
        for x in basket2:                                                    #Traverse basket2 and decrease the count of each cost.
            count[x] -= 1
        swap = []                                                            #Store the costs need to be swapped.
        for x, c in count.items():                                           #Traverse count.
            if c % 2:                                                        #If current cost has an odd offset, it cannot be evenly distributed, so return -1.
                return -1
            swap.extend([x] * (abs(c) // 2))                                 #Add half of the absolute value of count of the cost to swap.
        swap.sort()                                                          #Sort swap.
        return sum(min(2 * min_v, x) for x in swap[:len(swap) // 2])         #Swap a cost in the first half with a cost in the second half to minimize total costs. Also, can use the min cost as a medium(swap twice using the min cost) to further reduce cost.
