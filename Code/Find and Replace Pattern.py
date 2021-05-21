class Solution:
    def matchPattern(self, word, pattern):
        map1, map2 = {}, {}                                                         #Use 2 maps to store the permutation between the letters in word and pattern.
        for x, y in zip(word, pattern):                                             #For each letters x, y in word and pattern respectively.
            if x not in map1 and y not in map2:                                     #If x, y both not in permutation, add the bijection of x and y to permutation.
                map1[x], map2[y] = y, x
            elif y not in map2 or x not in map1 or map1[x] != y or map2[y] != x:    #If only one of x or y is not in permutation or x and y do not form a bijection, return false.
                return False
        return True                                                                 #Return true.
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return [w for w in words if self.matchPattern(w, pattern)]                  #Return all the words that can match pattern.
