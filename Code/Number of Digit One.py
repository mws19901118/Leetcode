class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        l=len(str(n))
        if l==1:                              #When n is a single digit, if n is 0, the result is 0; otherwise, the result is 1.
            if n==0:
                return 0
            else:
                return 1
        l=len(str(n))                         #Get the number of digits of n.
        q=n/(10**(l-1))                       #Get the number in the first digit.
        r=n%(10**(l-1))                       #Get the remain part.
        result=q*(l-1)*10**(l-2)              #From 0~10^i-1, there are i*10^(i-1) digit 1 in total. So, leave out the digit 1 in the first digit, there are q*(l-1)*10**(l-2) digit 1 in total from 0~q*10^(i-1).
        if q==1:                              #Consider the digit 1 in the first digit. If q is greater than 1, there are 10^(i-1) numbers beginning with 1. If q is 1, the amount of numbers beginning with 1 is r+1(from 0 to r).
            result+=r+1
        elif q>1:
            result+=10**(l-1)
        return result+self.countDigitOne(r)   #Deal with the remainder recursively.
