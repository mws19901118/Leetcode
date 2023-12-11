class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        candidates = [arr[len(arr) // 4], arr[len(arr) // 2], arr[3 * len(arr) // 4]]      #The integer occurs more than 25% of the time must be on either the 25 percentile, 50 percentile or 75 percentile.
        threshold = len(arr) / 4                                                           #Calculate the threshold.
        for candidate in candidates:                                                       #Check each candidate.
            left, right = bisect_left(arr, candidate), bisect_right(arr, candidate) - 1    #Find the leftmost and rightmost index of candidate.
            if right - left + 1 > threshold:                                               #If the span is beyond threshold, return candidate.
                return candidate
