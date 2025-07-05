class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)                    #Count each integer.
        result = -1
        for x in count:                         #Traverse count.
            if x == count[x]:                   #If x == count[x], update result if necessary.
                result = max(result, x)
        return result
