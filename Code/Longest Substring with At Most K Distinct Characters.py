class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        lastSeenIndex = {}                                                   #Store the last seen index of each seen character in dictionary.
        length, left = 0, -1                                                 #Initialize max length and the left bound(not inclusive) of sliding window.
        for i, x in enumerate(s):                                            #Traverse s.
            lastSeenIndex[x] = i                                             #Update the last seen index of x.
            if len(lastSeenIndex) > k:                                       #If the dictionary has more than k elements, find the smallest index stored in dictionary and update left.
                left = min(lastSeenIndex.values())
                lastSeenIndex.pop(s[left])                                   #Pop the dictionary for key s[left].
            length = max(length, i - left)                                   #Update length if it's smaller than current substring s[left + 1:i + 1].
        return length
