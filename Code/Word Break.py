class Solution:
    def DFS(self, s: str, wordDict: List[str], cache: dict) -> bool:
        if s == "":                                                                                     #If s is empty, return true.
            return True
        if s in cache:                                                                                  #If s in cache, return its value.
            return cache[s]
        cache[s] = any(s[:len(w)] == w and self.DFS(s[len(w):], wordDict, cache) for w in wordDict)     #DFS to find if there is any valid word break and update cache.
        return cache[s]
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.DFS(s, wordDict, {})                                                                #DFS with cache.
