class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        indexes = {}                                    #Store the indexes of last occurrence of each character.
        left, result = -1, 0                            #Initialize left bound of sliding window(not inclusive) and result.
        for i, x in enumerate(s):                       #Traverse s.
            indexes[x] = i                              #Set indexes[x] to i.
            if len(indexes) > 2:                        #If the length of indexes is greater than 2, pop the least index in indexes.values() and move left to it.
                left = min(indexes.values())
                indexes.pop(s[left])
            result = max(result, i - left)              #Update result if i - left is larger.
        return result
