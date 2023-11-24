class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minVal, maxVal, result = arrays[0][0], arrays[0][-1], 0                  #Initialize min value and max value to be the min value and max value of first arary; also initialize result.
        for x in arrays[1:]:                                                     #Traverse the rest of arrays.
            result = max(result, abs(x[0] - maxVal), abs(x[-1] - minVal))        #Update result if a new distance, either current array min value with previous max value aor current array max value with previous min value, is greater tban result.
            minVal, maxVal = min(minVal, x[0]), max(maxVal, x[-1])               #Update min value and max value if necessary.
        return result
