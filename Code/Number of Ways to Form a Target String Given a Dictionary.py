class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        division = 10 ** 9 + 7                                                                            #Division is 10 ** 9 + 7.
        count = [Counter(x) for x in zip(*words)]                                                         #Count the characters at each index of 

        @cache                                                                                            #Cache result.
        def dp(i: int, j: int) -> int:                                                                    #Calculate the number of ways to form target[i:] using all w[j:] for the w in words.
            if i == len(target):                                                                          #If i reaches the end of target, return 1 because we found a valid way.
                return 1
            if len(count) - j < len(target) - i:                                                          #If len(count) - j < len(target) - i, return 0 because there aren't enough characters.
                return 0
            return (dp(i, j + 1) + count[j][target[i]] * dp(i + 1, j + 1)) % division                     #So, we have 2 options now. First is to skip'current j, so the value is dp(i, j + 1). Second is to use characters at j, so the value is count[j][target[i]] * dp(i + 1, j + 1). Sum these 2 up and return modulo.
            
        return dp(0, 0)                                                                                   #Return dp(0, 0).
