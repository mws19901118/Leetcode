class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        sortedCount = sorted(Counter(arr).values(), reverse = True)       #Count of each integer and sort the count in descending order.
        size = 0                                                          #Initialize reduced size.
        for i, x in enumerate(sortedCount):                               #Traverse sortedCount.
            size += x                                                     #Reduce current count.
            if size >= len(arr) // 2:                                     #If size reaches half of arr, return i + 1 which is the number of reduced integer.
                return i + 1
