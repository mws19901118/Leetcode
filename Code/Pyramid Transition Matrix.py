class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        patterns = defaultdict(list)                                                                                    #Initialize pattern graph.
        for p in allowed:                                                                                               #Traverse allowed and populate pattern graph.
            patterns[(p[0], p[1])].append(p[2])
        
        @cache                                                                                                          #Cache dfs result.
        def dfs(currentLevel: str, nextLevel: str) -> bool:                                                             #DFS with given current level and next level.
            if len(currentLevel) == 1 and len(nextLevel) == 0:                                                          #If current level only has 1 letter and next level is empty, dfs reaches the pyramid top, so return true.
                return True
            if len(currentLevel) <= 1:                                                                                  #If current level has no more than 1 letter, we have finished current level, keep dfs with next level as new current level.
                return dfs(nextLevel, "")
            return any(dfs(currentLevel[1:], nextLevel + x) for x in patterns[(currentLevel[0], currentLevel[1])])      #Enumerate each valid pattern for the first 2 letters of current level, and return true if any following dfs is true.

        return dfs(bottom, "")                                                                                          #Return the result of dfs starting from bottom.
