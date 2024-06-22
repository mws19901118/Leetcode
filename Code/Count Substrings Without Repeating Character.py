class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        result, left = 0, 0                              #Initialize the result and left boundary of sliding window.
        indexes = {}                                     #Store the last index of each character.
        for i, x in enumerate(s):                        #Traverse s.
            if x in indexes:                             #If current character is already seen, update left to the greater of current left and indexes[x] + 1.
                left = max(left, indexes[x] + 1)
            indexes[x] = i                               #Update indexes[x].
            result += i - left + 1                       #There are i - left + 1 substrings in the sliding window that ends at current character.
        return result
