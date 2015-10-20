class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        flag=False
        if x<0:                                         #Deal with negative integer.
            x=abs(x)
            flag=True
        l=0
        d=1
        while x>=d:                                     #Get the length of integer.
            l+=1
            d*=10
        d/=10
        answer=0
        m=1
        for i in range(l):                              #Reverse integer. Use d(10^(l-1-i)) and m(10^i) to accelerate.
            answer+=(x/d)*m
            x%=d
            d/=10
            m*=10
        if flag:
            answer=-answer
        if answer>2147483647 or answer<-2147483648:     #Deal with overflow.
            return 0
        return answer
