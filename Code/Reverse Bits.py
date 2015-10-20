class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b=bin(n)                            #Transfrom decimal number to binary number(as a string).
        ans=""                              
        for i in range(32-len(b)+2):        #Eliminate the first 2 characters "0b" and add leading zeros to make the whole number 32 bits.
            ans=ans+"0"
        ans=ans+b[2:]
        ans=ans[::-1]                       #Awesome code to reverse the string.
        ans=int(ans,2)                      #Transform binary number(as a string) to decimal number.
        return ans
