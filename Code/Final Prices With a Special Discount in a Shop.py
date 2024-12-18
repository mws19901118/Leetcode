class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack, result = [], prices.copy()              #Initialize stack and result.
        for i, x in enumerate(prices):                 #Traverse prices.
            while stack and prices[stack[-1]] >= x:    #While stack is not empty and the price on the index on top of the stack is greater than or equal to current price, pop stack and decrease its price in result by current price.
                result[stack.pop()] -= x
            stack.append(i)                            #Append current index to stack.
        return result
