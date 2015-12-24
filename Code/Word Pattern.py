class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')                                                                        #Split str.
        if len(words) != len(pattern):                                                                #If words and pattern have differenct length, return false.
            return False
        wordtopattern = {}                                                                            #Map word to pattern.
        patterntoword = {}                                                                            #Map pattern to word.
        for i in range(len(words)):
            if words[i] not in wordtopattern and pattern[i] not in patterntoword:                     #If current word and pattern are both new, add the 1 to 1 map relation of word and pattern.
                wordtopattern[words[i]] = pattern[i]
                patterntoword[pattern[i]] = words[i]
            elif words[i] in wordtopattern and pattern[i] in patterntoword:                           #If current word and pattern is a 1 to 1 map relation, continue; otherwise, return false.
                if pattern[i] == wordtopattern[words[i]] and words[i] == patterntoword[pattern[i]]:
                    continue
                else:
                    return False
            else:
                return False
        return True
