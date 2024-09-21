class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []                          #Initialize result.
        def dfs(prefix: int) -> None:        #DFS.
            for i in range(10):              #Traverse from 0 to 9.
                curr = prefix * 10 + i       #Append current digit to the end of prefix.
                if 0 < curr <= n:            #If curr is within the range [1, n], append curr to result and keep dfs.
                    result.append(curr)
                    dfs(curr)
        dfs(0)                               #Start DFS at 0.
        return result
