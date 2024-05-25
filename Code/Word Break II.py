class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @cache                                                                    #Cache result.
        def dp(index: int) -> List[str]:                                          #Find all the sentences for s[index:].
            if index == len(s):                                                   #If reaches the end of s, return a list with only one empty string.
                return [""]
            result = []
            for i in range(index + 1, len(s) + 1):                                #Traverse all possible places to break strubg,
                if s[index:i] in wordSet:                                         #If s[index:i] is a valid word, we can break at i.
                    nextResult = dp(i)                                            #Get all the sentences for s[i:].
                    for x in nextResult:                                          #Concatenate each sentence after s[index:i] with correct delimiter and append it to result.
                        split = "" if x == "" else " "
                        result.append(s[index:i] + split + x)
            return result
        wordSet = set(wordDict)                                                   #Store valid words in set.
        return dp(0)                                                              #Return the result of dp[0].
