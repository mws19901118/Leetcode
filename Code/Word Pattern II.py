class Solution(object):
    def backtrack(self,pattern, str, patterntoword, wordtopattern):
        l = len(pattern)
        n = len(str)
        if l == 0 and n == 0:                                                                     #If both str and pattern reach the end, we find a bijection and return true.
            return True
        if l == 0 and n != 0:                                                                     #If pattern reach the end while str doesn't, it's invalid, so return false.
            return False
        if pattern[0] in patterntoword:                                                           #If the first character of pattern has already in the patterntoword dict, get the corresponding word.
            t = patterntoword[pattern[0]]
            if str[:len(t)] != t:                                                                 #If str doesn't begin with t, it's invalid and return false. 
                return False
            else:                                                                                 #If str begins with t, keep backtracking on the remainning str and pattern.
                return self.backtrack(pattern[1:], str[len(t):], patterntoword, wordtopattern)
        else:                                                                                     #Otherwise, check every possible word for current pattern.
            for i in range(n - len(pattern) + 1):                                                 #Leave enough space to following patterns.
                if str[:i + 1] not in wordtopattern:                                              #The word should not be mapped to another pattern before.
                    patterntoword[pattern[0]] = str[:i + 1]                                       #Add current word to patterntoword according to current pattern.
                    wordtopattern[str[:i + 1]] = pattern[0]                                       #Add current pattern to wordtopattern according to current word.
                    r = self.backtrack(pattern[1:], str[i + 1:], patterntoword, wordtopattern)    #Keep backtracking.
                    del patterntoword[pattern[0]]                                                 #Restore patterntoword.
                    del wordtopattern[str[:i + 1]]                                                #Restore wordtopattern.
                    if r is True:                                                                 #If find a bijection, return true.
                        return r
            return False                                                                          #If can't find a bijection, return false.
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        patterntoword = {}                                                                      #Map word to pattern.
        wordtopattern = {}                                                                      #Map pattern to word.
        return self.backtrack(pattern, str, patterntoword, wordtopattern)                       #Backtracking.
