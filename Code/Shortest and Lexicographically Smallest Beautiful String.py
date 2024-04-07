class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        result = ""                                                                                                            #Initialize result.
        indexes = []                                                                                                           #Store indexes.
        for i, x in enumerate(s):                                                                                              #Traverse s.
            if x != "1":                                                                                                       #If x is not '1', skip.
                continue
            indexes.append(i)                                                                                                  #Append i to indxees.
            if len(indexes) >= k:                                                                                              #If there are at least k indexes, we have a candidate.
                candidate = s[indexes[-k]:i + 1]                                                                               #s[indexes[-k]:i + 1] is a substring with exact k '1's that ends at current i.
                if not result or len(result) > len(candidate) or (len(result) == len(candidate) and result > candidate):       #If result is empty or candidate is smaller or candidate has same length with result but is lexicographically smaller, replace result with candidate.
                    result = candidate
        return result
