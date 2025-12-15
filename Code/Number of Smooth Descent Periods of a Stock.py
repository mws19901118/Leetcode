class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        i, result = 0, 0                                                    #Initialize i to traverse prices and result.
        while i < len(prices):                                              #Traverse prices.
            j = i + 1
            while j < len(prices) and prices[j] == prices[j - 1] - 1:       #Find the longest smooth desend period starting at i.
                j += 1
            result += (1 + j - i) * (j - i) // 2                            #Totoal number of smooth descend periods in this subarray is (1 + j - i) * (j - i) // 2.
            i = j                                                           #Move i to j.
        return result
        
