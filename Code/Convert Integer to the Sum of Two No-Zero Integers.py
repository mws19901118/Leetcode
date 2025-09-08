class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):                                        #Traverse i.
            if '0' not in str(i) and '0' not in str(n - i):          #If both i and n - i is non-zero integer, return [i, n - i].
                return [i, n - i]
