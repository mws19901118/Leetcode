class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        numeral=['M', 'D', 'C', 'L', 'X', 'V', 'I']
        if not s:
            return 0
        for c in numeral:
            try:
                i = s.index(c)                                                          #Search for M, D, C, L, X, V and I in order. Get the index of first appearance of a certain character in s.
            except ValueError:
                i = -1                                                                  #If not found, catch the ValueError and set i to be -1.
            finally:
                if i != -1:
                    return -self.romanToInt(s[:i]) + d[c] + self.romanToInt(s[i+1:])    #Return its value minus the value of Romen numeral between that character plus the value of Romen numeral after that character.
