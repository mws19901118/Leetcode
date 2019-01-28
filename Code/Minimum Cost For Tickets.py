class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        def dp(days, costs):
            if len(days) == 0:                                            #If no days left, return 0.
                return 0
            if days[0] in cache:                                          #Read from cache if there is.
                return cache[days[0]]
            minCost = costs[0] + dp(days[1:], costs)                      #DP case 1: buy 1-day pass today.
            index = 1
            while index < len(days) and days[index] - days[0] < 7:        #Find the first travel day after 7 days.
                index += 1
            minCost = min(minCost, costs[1] + dp(days[index:], costs))    #DP case 2: buy 7-day pass today.
            while index < len(days) and days[index] - days[0] < 30:       #Find the first travel day after 30 days.
                index += 1
            minCost = min(minCost, costs[2] + dp(days[index:], costs))    #DP case 3: buy 30-day pass today.
            cache[days[0]] = minCost                                      #Write to cache.
            return minCost
        
        cache = {}                                                        #Cache the result by starting day.
        return dp(days, costs)
