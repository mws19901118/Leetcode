class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        if dividend==-2147483648 and divisor==-1:         #Deal with the overflow case.              
            return 2147483647
        flag=(dividend>0)^(divisor>0)                     #Get the sign of quotient.
        de=abs(dividend)                                  #Get the absolute value of dividend.
        ds=abs(divisor)                                   #Get the absolute value of divisor.
        quotient=0
        while de>=ds:
            a=ds
            i=1
            while a<=de:                                  #Calculate the integer i such that ds*2^(i-2)<=de<ds*2^(i-1).
                a<<=1
                i+=1
            quotient+=(1<<(i-2))                          #The quotient gain 2^(i-2)
            de-=(ds<<(i-2))                               #de minus ds*2^(i-2)
        if flag:
            return -quotient
        else:
            return quotient
