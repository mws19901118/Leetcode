class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x<0:                                         #Negative number can't be palindrome.
            return False
        l=0                                             #Calculate the number of digits.
        while x>=10**l:
            l+=1
        for i in range(l/2):                            #Judge palindrome digit by digit.
            if (x/(10**i))%10!=(x/(10**(l-1-i)))%10:
                return False
        return True
