class Solution:
    def update(self, dp: defaultdict, newdp: defaultdict, target: int, newColor: int, cost: int) -> None:
        for (color, count) in dp:                                                                             #Traverse each color and count combination in dp.
            newCount = count + (color != newColor)                                                            #Only when color is same with newColor, we don't increase count.
            if newCount <= target:                                                                            #If newCount is no greater than target, update newdp[(newColor, newCount)] to dp[(color, count)] + cost if the sum is smaller than current value.
                newdp[(newColor, newCount)] = min(newdp[(newColor, newCount)], dp[(color, count)] + cost)
                
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = {(-1, 0) : 0}                                                                                    #Initialize dp to be the min cost so far of each color of current house and neighborhood count so far combination; before traverse start, default value is 0 for (0, 0), meaning no cost for no color and no neighborhood.
        for i, h in enumerate(houses):                                                                        #Traverse houses.
            newdp = defaultdict(lambda:1000001)                                                               #Initialize the dp for current house; 1000001 is greater than max cost.
            if h:                                                                                             #If current house is painted, update newdp with current color and no cost.
                self.update(dp, newdp, target, h, 0)
            else:                                                                                             #Otherwise, try to paint house in each color and update newdp with corresponding cost.
                for j in range(1, n + 1):
                    self.update(dp, newdp, target, j, cost[i][j - 1])
            dp = newdp                                                                                        #Replace dp with newdp.
        minCost = min(dp[(i, target)] for i in range(1, n + 1))                                               #Calculate the overall minCost.
        return minCost if minCost != 1000001 else -1                                                          #If it's 1000001, there is no possible solution then return -1; otherwise, return minCost.


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @cache                                                                                                                                      #Cache dp result.
        def dp(house, color, count):                                                                                                                #Calculate the min cost from the beginning to current house with it's painted to color and count neighborhood so far.
            if house < 0:                                                                                                                           #If house is smaller than 0, backward dp has passed the beginning.
                return float('inf') if count else 0                                                                                                 #There cannot be neighborhood before beginning, so return 0 if count is 0 otherwise return float('inf').
            if count <= 0 or (houses[house] != 0 and houses[house] != color):                                                                       #If during dp, count is smaller than or equal to 0, or current house is already painted but not given color, it's invalid, so return float('inf').
                return float('inf')
            return min(dp(house - 1, c, count - (c != color)) for c in range(1, n + 1)) + (0 if houses[house] else cost[house][color - 1])          #Return the min value of next backward dp plus the cost of current house(0 if already painted and cost[house][color - 1] if not).

        result = min(dp(len(houses) - 1, c, target) for c in range(1, n + 1))                                                                       #Calculate the overall minCost.
        return -1 if result == float('inf') else result                                                                                             #If it's float('inf'), there is no possible solution then return -1; otherwise, return minCost.
