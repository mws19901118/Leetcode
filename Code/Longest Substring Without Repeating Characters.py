class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftBound, maxLength = -1, 0                                #Initialize the left bound(not included) of substring to be -1 and max length to be 0.
        lastSeenIndex = {}                                          #Store the index of each character seen last time in current substring sliding window.
        for i, x in enumerate(s):                                   #Traverse s.
            if x in lastSeenIndex:                                  #if x is already seen, the index of last seen x becomes new left bound.
                newLeftBound = lastSeenIndex[x]
                for k in range(leftBound + 1, newLeftBound + 1):    #Remove all characters from left bound to new left bound.
                    del lastSeenIndex[s[k]]
                leftBound = newLeftBound                            #Update left bound.
            lastSeenIndex[x] = i                                    #Add current index of x to the dictionary.
            maxLength = max(maxLength, i - leftBound)               #Update max length if necessary using current substring sliding window length, which is i - leftbound.
        return maxLength
