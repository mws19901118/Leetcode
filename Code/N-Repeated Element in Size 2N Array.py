from collections import Counter
class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = Counter(A)                      #Count each element.
        for k in count:
            if count[k] == int(len(A) / 2):     #Find the element repated N times.
                return k
