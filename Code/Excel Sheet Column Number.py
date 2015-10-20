class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        num=0
        n=len(s)
        for i in range(n):
            num+=(ord(s[i])-ord('A')+1)*26**(n-i-1)
        return num
