class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        times = []                              #Break intervals into times.
        for x, y in intervals:                  #Traverse intervals.
            times.append((x, -1))               #Append x and -1 to times.
            times.append((y, 1))                #Append y and 1 to times.
        times.sort()                            #Sort times.
        groups, result = 0, 0
        for _, flag in times:                   #Traverse times. The minimal number of groups is the max number of overlapped intervals at any time.
            groups -= flag
            result = max(groups, result)
        return result
