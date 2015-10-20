class Solution:
    def find(self, s, char):                    #Get the index of first appearance of a certain character in s; return -1 if not found.
        index=-1
        for i in range(len(s)):
            if s[i]==char:
                index=i
                break
        return index
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):                    
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        numeral=['M', 'D', 'C', 'L', 'X', 'V', 'I']
        n=len(s)
        if n==0:
            return 0
        for c in numeral:
            i=self.find(s,c)                                                    #Search for M, D, C, L, X, V and I in order
            if i!=-1:
                return -self.romanToInt(s[:i])+dict[c]+self.romanToInt(s[i+1:]) #Return its value minus the value of Romen numeral between that character plus the value of Romen numeral after that character.

