class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        def BinaryToInt(a):                           #Convert binary number to decimal number.
            ans=0
            l=len(a)
            for i in range(l):
                ans+=int(a[i])*2**(l-1-i)
            return ans
        temp=bin(BinaryToInt(a)+BinaryToInt(b))
        return temp[2:]                               #Drop the first 2 charactors "0b".
