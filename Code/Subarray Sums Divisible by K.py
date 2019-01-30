from collections import Counter
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        s = [0]                                               #Store remainder of prefix sum from A[0] to A[i]. Add 0 to represent that in the beginning, the sum is 0.
        for x in A:
            s.append((s[-1] + x) % K)                         #Append the newest remainder to s.
        count = Counter(s)                                    #Count the occurence of each remainder.
        return sum(v * (v - 1) / 2 for v in count.values())   #For each pair of indexes, i and j, if s[i] = s[j], then s[i] + (A[i] + ... + A[j]) % K = s[j].
                                                              #Thus, A[i] to A[j] is a subarray whose sum is divisible by K.
                                                              #Then, we only need to calculate for each remainder, how many pairs are there.
                                                              #If remainder s occurs v times, the number of pairs is v * (v - 1) / 2
