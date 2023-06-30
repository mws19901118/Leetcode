class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(int)                                                                          #Store the taller pod height by the diff of 2 heights.
        dp[0] = 0                                                                                      #Initially, both height is 0 so diff is 0.
        for r in rods:                                                                                 #Traverse rods.
            new_dp = dp.copy()                                                                         #Copy current key values in dp.
            for diff, taller in dp.items():                                                            #Traverse key values in dp.
                new_dp[diff + r] = max(new_dp[diff + r], taller + r)                                   #Add current rod to the taller then update new_dp[diff + r].
                new_dp[abs(diff - r)] = max(new_dp[abs(diff - r)], taller, taller + r - diff)          #Add current rod to the shorter then update new_dp[abs(diff - r)]. The new taller after adding current rod to shorter is still taller if diff >= r, taller + r - diff if diff < r. 
            dp = new_dp                                                                                #Replace dp with new_dp.
        return dp[0]                                                                                   #Return dp[0] where 2 heights are balanced.
