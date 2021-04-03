class Solution:
    def find(self, strs: List[str], cache: defaultdict, m: int, n: int, i: int, zero: int, one: int) -> int:
        if i >= len(strs) or (zero <= 0 and one <= 0):                                                                  #If i reaches the end of strs or zero and one are both not greater than 0, return 0 cause we cannot form subset further.
            return 0
        if (i, zero, one) in cache:                                                                                     #If the combination of (i, zero, one) is already in cache, return the value in cache.
            return cache[(i, zero, one)]
        else:
            x, y = strs[i].count('0'), strs[i].count('1')                                                               #Count '0' and '1' in strs[i].
            a = 1 + self.find(strs, cache, m, n, i + 1, zero - x, one - y) if zero - x >= 0 and one - y >= 0 else 0     #Calculate the max size of subset we can form beyond if we include str[i].
            b = self.find(strs, cache, m, n, i + 1, zero, one)                                                          #Calculate the max size of subset we can form beyond if we exclude str[i].
            cache[(i, zero, one)] = max(a, b)                                                                           #Store the max of a and b in cache for the combination in cache.
            return cache[(i, zero, one)]                                                                                #Return the value.
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = defaultdict(int)                                                                                        #Store the max size of subset we can form with strs[i:], zero as the limit of 0 and one as the limit as 1.
        return self.find(strs, cache, m, n, 0, m, n)                                                                    #Find the max size of subset from the beginning of strs with memorization.
