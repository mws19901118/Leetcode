from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        time = ""
        maxm = -1                                                                 #Largest time in minutes, starting from -1.
        permutation = permutations(A)                                             #Calculate all the permutations of A.
        for p in permutation:
            hour = p[0] * 10 + p[1]                                               #For each permutation, calculate hour and minute.
            minute = p[2] * 10 + p[3]
            if hour < 24 and minute < 60:                                         #If hour and minute are both valid, check if it's larger than maxm.
                if hour * 60 + minute > maxm:
                    maxm = hour * 60 + minute                                     #If so, update maxm and time.
                    time = str(p[0]) + str(p[1]) + ":" + str(p[2]) + str(p[3])
        return time
