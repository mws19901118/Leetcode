class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        @cache                                                                    #Cache result.
        def hasRepeat(length: int) -> bool:                                       #Determine if s has repeat substrings at given length. 
            hash = 0                                                              #Initialize hash.
            for i in range(length):                                               #Convert s[:length] to a base26 number.
                hash = hash * 26 + ord(s[i]) - ord('a')
            hashSet = set([hash])                                                 #Store hash in set.
            for i in range(length, len(s)):                                       #Traverse s[length:].
                hash -= 26 ** (length - 1) * (ord(s[i - length]) - ord('a'))      #Calculate the rolling hash of s[i - length + 1:i + 1].
                hash *= 26
                hash += ord(s[i]) - ord('a')
                if hash in hashSet:                                               #If hash is already seen, return true because we found a repeat.
                    return True
                hashSet.add(hash)                                                 #Add hash to set.
            return False                                                          #Return false if no repeat found.

        start, end = 1, len(s) - 1                                                #Start binary search from 1 to len(s) - 1.
        while start <= end:
            mid = (start + end) // 2                                              #Calculate mid.
            if hasRepeat(mid) and not hasRepeat(mid + 1):                         #If s has repeat substrings at length mid but not at length mid + 1, then mid is the longest length.
                return mid
            elif hasRepeat(mid + 1):                                              #If s has repeat substrings at length mid + 1, then set start to mid + 1.
                start = mid + 1
            else:                                                                 #Otherwise, set end to mid - 1.
                end = mid - 1
        return 0                                                                  #If no repeat substring found, return 0.
