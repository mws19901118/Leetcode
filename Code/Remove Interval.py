class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []                                                                          #Initialize result list.
        for a, b in intervals:                                                               #Traverse intervals.
            left, right = [a, min(b, toBeRemoved[0])], [max(a, toBeRemoved[1]), b]           #Split remove toBeRemoved from [a, b] to form 2 intervals, left and right.
            if left[0] < left[1]:                                                            #If left is valid, append it to result.
                result.append(left)
            if right[0] < right[1]:                                                          #If right is valid, append it to result.
                result.append(right)
        return result
