import math
class Solution(object):
    def backtracking(self, n, dict):
        if n in dict:                               #Use a dict to store temporary result.
            return dict[n]
        result = []
        for i in range(2, int(math.sqrt(n)) + 1):   #Traverse from 2 to int(sqrt(n)) + 1.
            if n % i == 0:                          #If i is a factor of n, append [i, n / i] to result.
                result.append([i, n / i])
                t = self.backtracking(n / i, dict)  #Find all the factor combination of n / i.
                for l in t:
                    if l[0] >= i:                   #Append i extending all the factor combination of n / i whose the first factor is not smaller than i to the result.
                        result.append([i] + l)
        dict[n] = result                            #Store temporaty result in dict.
        return result                               #Return result.
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        dict = {}
        return self.backtracking(n, dict)
