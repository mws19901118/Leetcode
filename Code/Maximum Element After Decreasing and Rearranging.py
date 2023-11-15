class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        counts = [0] * (len(arr) + 1)                  #Count each number. Because the max valid number is len(arr), we can treat any number greater than len(arr) as len(arr).
        for x in arr:
            counts[min(x, len(arr))] += 1
        result = 1                                     #Initialize result.
        for i, x in enumerate(counts):                 #Traverse counts.
            result = min(result + x, i)                #Update result. Either we decrease i x times to make it consecutive increasing from result + 1 to result + x and still smaller than i, then new result is result + i; otherwise it will reach i and new resultis i.
        return result
