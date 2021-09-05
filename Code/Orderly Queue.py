class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:                                                                  #If k == 1, find the smallest letter in s.
            minX = min(s)
            return min(s[i:] + s[:i] for i, x in enumerate(s) if x == minX)         #For each occurance of minX, rotate s at it and return the min result of each rotation.
        else:                                                                       #If k > 1, s can always be sorted in this way, so just return sorted s.
            return ''.join(sorted(s))                                               #Suppose s = yX, where X is already sorted and y should be inserted at index i.
                                                                                    #Because k > 1, we can always move X[:i] to the end. Now s = yX[i:]X[:i].
                                                                                    #Then, move yX[i:] to end. Now, s = X[:i]yX[i:] and is sorted.
