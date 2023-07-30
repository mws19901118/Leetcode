class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache                                                                                          #Cache result.
        def dp(left: int, right: int) -> int:                                                           #DP to calculate the number of turns needed to transform to s[left:right + 1] from a same length string which is only made of s[right].
            result = right - left                                                                       #Initialize result.
            firstNonRightCharacterIndex = -1                                                            #Initialize the first index of character not equal to s[right].   
            for i in range(left, right):                                                                #Traverse s[left:right].
                if s[i] != s[right] and firstNonRightCharacterIndex == -1:                              #If s[i] is the first character not equal to s[right], set firstNonRightCharacterIndex to i.
                    firstNonRightCharacterIndex = i
                if firstNonRightCharacterIndex != -1:                                                   #If there is any character not equal to s[right], we can divide s[left:right + 1] at i.
                    result = min(result, 1 + dp(firstNonRightCharacterIndex, i) + dp(i + 1, right))     #First part is s[firstNonRightCharacterIndex:i + 1] and second part is s[i + 1:right], then calculate turns needed respectively. Since for s[firstNonRightCharacterIndex:i + 1], we need to print s[i] first, so the overall result is 1 + dp(firstNonRightCharacterIndex, i) + dp(i + 1, right).
            if firstNonRightCharacterIndex == -1:                                                       #If there is no character not equal to s[right], we don't need to print anything, s[eft:right + 1] is just s[right] repeat left - right + 1 times.
                result = 0
            return result                                                                               #Return result.

        return dp(0, len(s) - 1) + 1                                                                    #Return dp(0, len(s) - 1) + 1, which means first print a same length string with s[-1] then transform to s.
