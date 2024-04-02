class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbiddenSet = set(forbidden)                                    #Put all forbidden strings in a set.
        max_forbidden = max(len(x) for x in forbidden)                   #Find the max length of a forbidden string.
        left, right = 0, 1                                               #Initialize the sliding window of word[left:right].
        result = 0
        while right <= len(word):                                        #Iterate while right <= len(word).
            valid = True                                                 #Suppose current word[left:right] is valud.
            for i in range(max(left, right - max_forbidden), right):     #Enumerate each position before right so that word[i:right] is a substring of word[left:right] and not exceeds the max length of forbidden word. 
                if word[i:right] in forbiddenSet:                        #If word[i:right] is in forbiddenSet, word[left:right] is not valid so set the valid flag to false and move left to i + 1.
                    left = i + 1
                    valid = False
                    break
            if valid:                                                    #If valid flag is still true, update result if necessar and move forward right. So, basically invalid substring only occurs as a suffix.
                result = max(result, right - left)
                right += 1
        return result
