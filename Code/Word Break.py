class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        cache = {"":True}                                               #buffer strings which have been processed
        def WB(s):
            if s in cache:
                return cache[s]
            for i in xrange(len(s)):                                    #judge whether the first part of string is in the dict and whether the other part is made up of strings in the dict成
                if s[:i+1] in dict and WB(s[i+1:])==True:
                    cache[s]=True                                       #process buffer
                    return True
            cache[s]=False                                              #provess buffer
            return False
        return WB(s)                                                    #solve the problem in a recursion method
