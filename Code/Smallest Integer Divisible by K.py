class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        length, r = 1, 1 % k          #Initialize length and the remainder of N % k.
        for i in range(k):            #Since its remainder, there are at most k different value of r.
            if r == 0:                #If the remainder is 0, N is divisible by k, return length.
                return length
            r = (r * 10 + 1) % k      #Calculate the remainder of next N, (N * 10 + 1) % k.
            length += 1               #Increase length by 1.
        return -1                     #Return -1 if no N is divisible by k.
