class Solution:
    def canCross(self, stones: List[int]) -> bool:
        indexes = {x: i for i, x in enumerate(stones)}                                                                          #Store the indexes for each stone.

        @cache                                                                                                                  #Cache result.
        def dp(i: int, k: int) -> bool:                                                                                         #Determine whether frog can cross river if frog jumped k units to stones[i].
            if i == len(stones) - 1:                                                                                            #If i == len(stones) - 1, the frog has already crossed river.
                return True
            return any(j > 0 and (stones[i] + j) in indexes and dp(indexes[stones[i] + j], j) for j in [k - 1, k, k + 1])       #Traverse k - 1, k, k + 1 units to jump forward, if any j is greater than 0 and stones[i] + j is a stone and dp(indexes[stones[i] + j], j) is true, then return true.
        
        return dp(0, 0)                                                                                                         #Return dp(0, 0) that frog is at stones[0] with 0 units jumped.
