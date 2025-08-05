class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = set()                              #Store used baskets.
        for i, x in enumerate(fruits):            #Traverse fruits.
            for j, y in enumerate(baskets):       #Traverse baskets.
                if j not in used and y >= x:      #If current basket is not used and its capacity is greater than or equal to current fruit, mark current basket as used and stop inner loop.
                    used.add(j)
                    break
        return len(baskets) - len(used)           #Return the count of baskets not in used.
