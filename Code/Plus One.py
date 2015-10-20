class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        carry=1
        l=len(digits)-1
        while l>=0 and carry==1:
            ncarry=(digits[l]+carry)/10
            digits[l]=(digits[l]+carry)%10
            carry=ncarry                                          #New carry.
            l-=1
        if carry==1:                                              #If the length of new number is longer than the old one, insert 1 in the front.
            digits.insert(0,1)
        return digits
