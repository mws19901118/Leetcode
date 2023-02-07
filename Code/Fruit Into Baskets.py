class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}                                                        #Store the last seen index of each fruit in basket.
        start, result = -1, 0                                               #Initialize the start(not inclusive) of sliding window and result.
        for i, x in enumerate(fruits):                                      #Traverse fruits.
            if len(baskets) == 2 and x not in baskets:                      #If already 2 types of fruits in basket and x is not one of them, we need to remove one fruit from basket.
                [x1, x2] = baskets.keys()                                   #Get the 2 fruit types.
                drop = x1 if baskets[x1] < baskets[x2] else x2              #Find the one whose last seen index is smaller.
                start = baskets[drop]                                       #Update start to the last seen index.
                baskets.pop(drop)                                           #Remove the fruit from basket.
            baskets[x] = i                                                  #Update the last seen index of fruit x.
            result = max(result, i - start)                                 #Update result if i - start is greater than current result.
        return result
