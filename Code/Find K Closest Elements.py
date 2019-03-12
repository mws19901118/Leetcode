class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start, end = 0, len(arr) - 1
        while start <= end:                                                                                 #Binary search x in arr.
            mid = (start + end) >> 1
            if arr[mid] == x:                                                                               #If find x, set start to be the idnex of x and end to be the index of x plus 1.
                start = mid
                end = mid + 1
                break
            elif arr[mid] < x:
                start = mid + 1
            else:
                end = mid - 1
        
        if start > end:                                                                                     #If start is larger than end, x is not in arr, reverse start and end.
            start, end = end, start
        less, more = [], []                                                                                 #Create 2 lists, "less" for the closest elements smaller than x and "more" for the closest elements larger than x.
        while len(less) + len(more) < k:                                                                    #While the sum of length of less and more is smaller than k, we haven't find enough closest elements.
            if (start >= 0 and end < len(arr) and x - arr[start] <= arr[end] - x) or end == len(arr):       #"start" and "end" works as 2 pointers.
                less.append(arr[start])                                                                     #If "end" reaches the right boundary or the number on "start" is not larger than the number on "end", append the number in "start" to "less".
                start -= 1                                                                                  #"start" moves left.
            else:                                                                                           #Otherwise, append the number on "end" to "more".
                more.append(arr[end])                                                                       #"end" moves right.
                end += 1
        result = []                                                                                         #Create a new list for result.
        result.extend(less[::-1])                                                                           #Reverse "less"(currently it's in desending order) and extend result by "less".
        result.extend(more)                                                                                 #Extend result by "more".
        return result
