class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lisf = [0] * len(nums)                                                                              #Find the length of longest increasing subsequence for each index from front.
        for i in range(len(nums)):
            lis = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    lis = max(lis, lisf[j])
            lisf[i] = lis + 1
        lisb = [0] * len(nums)                                                                              #Find the length of longest increasing subsequence for each index from behind.
        for i in reversed(range(len(nums))):
            lis = 0
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    lis = max(lis, lisb[j])
            lisb[i] = lis + 1
        return len(nums) - max(x + y for x, y in zip(lisf[1:-1], lisb[1:-1]) if x > 1 and y > 1) + 1        #To find the minimum number of removals is equivalent to find the max length of mountain array, which is the max of sum of longest increasing subsequence from front and longest increasing subsequence from behind(index cannot be the first or the last).
