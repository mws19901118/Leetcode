class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not k:                                                            #If k is 0, directlu return 0.
            return 0
        lastSeenIndex = {}                                                   #Store the last seen index of each seen character in dictionary.
        length, left = 0, -1                                                 #Initialize max length and the left bound(not inclusive) of sliding window.
        for i, x in enumerate(s):                                            #Traverse s.
            if x not in lastSeenIndex and len(lastSeenIndex) == k:           #If x is not seen but the dictionary already has k elements, find the smallest index stored in dictionary and update left.
                left = min(lastSeenIndex.values())
                lastSeenIndex.pop(s[left])                                   #Pop the dictionary for key s[left].
            lastSeenIndex[x] = i                                             #Update the last seen index of x.
            length = max(length, i - left)                                   #Update length if it's smaller than current substring s[left + 1:i + 1].
        return length
