class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sums = [0] * (len(nums) + 1)                                #Populate prefix sum.
        for i in range(1, len(nums) + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]
        indexes = deque()                                                  #Store possible indexes of starting subarray in a deque.
        result = inf                                                       #Initialize result to be inf.
        for i, x in enumerate(prefix_sums):                                #Traverse prefix sums.
            while indexes and x - prefix_sums[indexes[0]] >= k:            #Remove indexes from front of deque if the subarray sum is at least k.
                result = min(result, i - indexes.popleft())                #Update the result if necessary.
            while indexes and x <= prefix_sums[indexes[-1]]:               #Remove indexes from end of deque if its prefix sum is at least x to keep the numbers on the indexes monotonically increasing.
                indexes.pop()                                              #Because subarrays with sum at least k starting from them are guaranteed to have a shorted such subarray starting from i.
            indexes.append(i)                                              #Append current index to indexes.
        return result if result != inf else -1                             #Return -1 if result is inf; otherwise, return result.
