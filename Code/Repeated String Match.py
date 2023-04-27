class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        start, end = 1, ceil(len(b) / len(a)) + 1                         #Get the lowest possible and highest possible answer.
        while start <= end:                                               #Binary search the result.
            mid = (start + end) // 2
            if b in a * mid and not b in a * (mid - 1):
                return mid
            elif not b in a * mid:
                start = mid + 1
            else:
                end = mid - 1
            
        return -1                                                         #Return -1 if no result.
