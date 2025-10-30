class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return target[0] + sum(max(target[i] - target[i - 1], 0) for i in range(1, len(target)))    #The increment to the minumal number will divide the array to several subarrays, so the delta between current number and previous number is required increments to fulfil current number.
