class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        seq=[]                          #Store the sequence of number.
        while 1:
            if n==1:                    #If n=1, return True.
                return True
            elif n in seq:              #If n is already in the sequence, it falls into a endless loop, so return False.
                return False
            else:
                seq.append(n)           #Append current n to the sequence.
                s=0
                temp=n
                while temp!=0:          #Calculate the sum of square of each digit.
                    s+=(temp%10)**2
                    temp/=10
                n=s                     #Update n.
