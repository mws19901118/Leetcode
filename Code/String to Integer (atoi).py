class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()                                                                              #Remove leading whitespace.
        sign = 1
        if s and s[0] in "+-":                                                                      #Handle the case if the first character is sign.
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        i = 0
        while i < len(s) and s[i].isdigit():                                                        #Find the index of first non digit character. 
            i += 1
        return min(2 ** 31 - 1, max(- 2 ** 31, 0 if not s[:i] else sign * int(s[:i])))              #Convert s[:i] to int and make sure it not exceeds upper and lower bounds.
