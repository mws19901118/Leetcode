class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        visited = set()                                    #Store vivisted substrings.
        result = 0                                         #Initialize result.
        def backtracking(index: int) -> None:              #Backtracking at each index of s.
            nonlocal result
            if index == len(s):                            #If reaches the end, update result if length of visited is greater.
                result = max(result, len(visited))
            for i in range(index + 1, len(s) + 1):         #Traverse from index + 1to len(s), inclusive.
                if s[index:i] in visited:                  #If s[index:i] is visited, skip.
                    continue
                visited.add(s[index:i])                    #Add s[index:i] to visited.
                backtracking(i)                            #Keep backtracking at i.
                visited.remove(s[index:i])                 #Remove s[index:i] from visited.
        backtracking(0)                                    #Start backtracking at 0.
        return result
