class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        @cache                                                                              #Cache result.
        def canDistribute(threshold: int) -> bool:                                          #Determine if possible to distribute products given max product threshold per store.
            return threshold and sum(ceil(x / threshold) for x in quantities) <= n          #Threshold must be greater than 0 and the the number of stores needed shhouldn't be greater than n.

        start, end = 1, max(quantities)                                                     #Start binary search from 1 to max(quantities).
        while start <= end:
            mid = (start + end) // 2                                                        #Calculate mid.
            if canDistribute(mid) and not canDistribute(mid - 1):                           #If can distribute with mid as max product but cannot distribute with mid - 1 as max product, mid is the min max product, so return mid.
                return mid
            elif not canDistribute(mid):                                                    #If can not distribute with mid - 1 as max prodcut, move start to mid + 1.
                start = mid + 1
            else:                                                                           #Otherwise, move end to mid - 1.
                end = mid - 1
