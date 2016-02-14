class Solution(object):
    def backtracking(self, dict, s):
        if s in dict:                                                                       #If s is in dict, return dict[s].
            return dict[s]
        elif s[::-1] in dict:                                                               #If s[::-1](the reverse string of s) is in dict, return dict[s[::-1]].
            return dict[s[::-1]]
        result = False                                                                      #Store current result.
        for i in range(len(s) - 1):
            if s[i:i + 2] == '++':                                                          #For every possible '++', flip it to '--' and backtrack the new string.
                result = result or not self.backtracking(dict, s[:i] + '--' + s[i + 2:])    #If the other person can not win on one of such strings, we can win on s.
        dict[s] = result                                                                    #Store the result in dict.
        return result
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {}
        return self.backtracking(dict, s)                                                   #Backtrack.
