class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        length, r = 1, 1 % K          #Initialize length and the remainder of N % K.
        for i in range(K):            #Since its remainder, there are at most K different value of r.
            if r == 0:                #If the remainder is 0, N is divisible by K, return length.
                return length
            r = (r * 10 + 1) % K      #Calculate the remainder of next N, (N * 10 + 1) % K.
            length += 1               #Increase length by 1.
        return -1                     #Return -1 if no N is divisible by K.
