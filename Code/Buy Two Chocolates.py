class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        smallest, secondSmallest = inf, inf
        for x in prices:                                                                                      #Find the smallest and second smallest prices.
            if x < smallest:
                secondSmallest = smallest
                smallest = x
            elif x < secondSmallest:
                secondSmallest = x
        return money if smallest + secondSmallest > money else (money - smallest - secondSmallest)            #If the sum of smallest and second smallest is greater than money, it is impossible to buy 2 chocolates so return money as we buy nothing; otherwise, buy the 2 chocolates and return the remain.
