class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:                                                                  #If s is empty, return itself.
            return s
        result = []
        count, j = 0, 0                                                            #Count the diff of '1' against '0' and initialize the start of current special binary substring.
        for i, x in enumerate(s):                                                  #Traverse s.
            count += 1 if s[i] == '1' else -1                                      #Update count.
            if not count:                                                          #If count is 0, we reaches the end of current special binary substring.
                result.append('1' + self.makeLargestSpecial(s[j + 1:i]) + '0')     #Recursively get the largest special binary string in s[j + 1:i], then wrap it between an '1' and '0'(to prevent infinite recursion). Next, append it to result. s[j + 1:i] is guaranteed to be a special binary string; otherwise, count will reach 0 before i.
                j = i + 1                                                          #Move j to i + 1.
        return ''.join(sorted(result, reverse = True))                             #Sort result in desending order and join together then return.
