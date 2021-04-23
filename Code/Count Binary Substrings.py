class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count, prevLength, currLength = 0, 0, 1             #Initialize the total count, previous consecutive binary substring length and current consecutive binary substring length.
        for i in range(1, len(s) + 1):                      #Traverse s.
            if i == len(s) or s[i - 1] != s[i]:             #If reaches the end or current character does not equal to previous character, add the mininum of prevLength and currLength to count.
                count += min(prevLength, currLength)
                prevLength, currLength = currLength, 1      #Also, refresh prevLength and currLength.
            else:                                           #Otherwise, increase currLength.
                currLength += 1
        return count                                        #Return count.
