class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        start, end = 1, k
        while start < end:                                            #Binary search from 1 to k.
            mid = (start + end) // 2                                  #Compute mid.
            count = sum(min(mid // x, n) for x in range(1, m + 1))    #Calculate the numbers in multiplication table that are not greater than mid.
            if count < k:                                             #If count < k, set start to mid + 1.
                start = mid + 1
            else:                                                     #Otherwise, set end to mid.
                end = mid
        return start                                                  #Return start when binary search finishes.
