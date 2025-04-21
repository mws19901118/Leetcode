class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        result, min_delta, max_delta, prefix_sum = 0, 0, 0, 0                                #Initialize result, min delta from start, max delta from start and prefix sum.
        for x in differences:                                                                #Traverse differences.
            prefix_sum += x                                                                  #Add x to prefix sum.
            min_delta = min(min_delta, prefix_sum)                                           #Update min delta if necessary.
            max_delta = max(max_delta, prefix_sum)                                           #Update max delta if necessary.
        return max(0, (upper - max(0, max_delta)) - (lower - min(0, min_delta)) + 1)         #The real upper bound of start should be upper - max(0, max_delta).
                                                                                             #The real lower bound of start should be lower - min(0, min_delta).
                                                                                             #So, the number of hidden dequence should be real upper bould - real lower bound + 1.
                                                                                             #And make sure the result is not smaller than 0.
