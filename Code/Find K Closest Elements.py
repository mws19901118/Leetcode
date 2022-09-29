class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = bisect_right(arr, x)                                                                        #Binary search for the index of x in arr.
        start, end = index - 1, index                                                                       #Initialize the start and end pointer of K closest elements.
        less, more = [], []                                                                                 #Create 2 lists, "less" for the closest elements smaller than x and "more" for the closest elements larger than x.
        while len(less) + len(more) < k:                                                                    #While the sum of length of less and more is smaller than k, we haven't find enough closest elements.
            if start >= 0 and (end == len(arr) or x - arr[start] <= arr[end] - x):                          #"start" and "end" works as 2 pointers.
                less.append(arr[start])                                                                     #If "end" reaches the right boundary or the number on "start" is not larger than the number on "end", append the number in "start" to "less".
                start -= 1                                                                                  #"start" moves left.
            else:                                                                                           #Otherwise, append the number on "end" to "more".
                more.append(arr[end])                                                                       #"end" moves right.
                end += 1
        return less[::-1] + more                                                                            ##Reverse "less"(currently it's in desending order) and extend result by "more", then return.
