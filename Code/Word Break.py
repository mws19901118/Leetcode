class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache                                                                                        #Cache result.
        def dp(index: int) -> bool:                                                                   #DP to find if s[index:] can be break.
            if index == len(s):                                                                       #If index reaches the end of s, we find a break so return true.
                return True
            return any(s[index:index + len(x)] == x and dp(index + len(x)) for x in wordDict)         #For any word x in wordDict, if s[index:index + len(x)] is x and s[index + len(x):] can be break, then s[index:] can be break. 

        return dp(0)                                                                                  #Return dp(0).
