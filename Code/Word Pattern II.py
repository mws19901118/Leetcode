class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        pToSMap, sToPMap = {}, {}                                                                                                                                                #Map pattern to word and vice versa.

        def backtracking(pIndex: int, sIndex: int):
            if sIndex == len(s) and pIndex == len(pattern):                                                                                                                      #If both pIndex and sIndex reach the end, we find a bijection and return true.
                return True
            if sIndex == len(s) or pIndex == len(pattern):                                                                                                                       #If only one of pIndex and sIndex reaches the end, it's invalid.
                return False
            if pattern[pIndex] in pToSMap:                                                                                                                                       #If the character on pIndex is seen, get the word from  pattern to word map.
                word = pToSMap[pattern[pIndex]]
                return backtracking(pIndex + 1, sIndex + len(word)) if sIndex + len(word) <= len(s) and s[sIndex:sIndex + len(word)] == word else False                          #If s[sIndex:sIndex + len(word)] is valid and equals word, the pattern matches word, so return the result of recursively moving forward; otherwise, return false as it is invalid.
            for i in range(sIndex, len(s)):                                                                                                                                      #Check every possible word for current pattern.
                word = s[sIndex:i + 1]
                if word in sToPMap:                                                                                                                                              #If word is already mapped, skip it.
                    continue
                pToSMap[pattern[pIndex]] = word                                                                                                                                  #Add current word to pattern to word map by current pattern.
                sToPMap[word] = pattern[pIndex]                                                                                                                                  #Add current pattern to word to pattern map by current word.
                if backtracking(pIndex + 1, sIndex + len(word)):                                                                                                                 #Move forward, if the result is true then return true.
                    return True
                sToPMap.pop(word)                                                                                                                                                #Restore word to pattern map.
                pToSMap.pop(pattern[pIndex])                                                                                                                                     #Restore pattern to word map.
            return False                                                                                                                                                         #If can't find a bijection, return false.

        return backtracking(0, 0)                                                                                                                                                #Return the result of backtracking at 0 and 0.
