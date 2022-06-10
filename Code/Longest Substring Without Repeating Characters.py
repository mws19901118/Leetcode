class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, result = -1, 0                                               #Initialize the index of start, not included in substring, of substring and result.
        visited = {}                                                        #Store the last seen index of visited characters.
        for i, x in enumerate(s):                                           #Traverse s.
            start = max(start, visited[x] if x in visited else -1)          #Update start to be the larger one of current value and visited[x] if x is in visited.
            visited[x] = i                                                  #Update the last seen index of s.
            result = max(result, i - start)                                 #Update result.
        return result                                                       #Return result.
