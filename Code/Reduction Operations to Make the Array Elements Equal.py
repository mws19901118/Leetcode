class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = Counter(nums)                                            #Count each number in nums.
        keys = sorted(count.keys())                                      #Sort the distinct numbers.
        return sum(i * count[x] for i, x in enumerate(keys))             #For each num x in keys whose index is i, we need i operation to make it to the smallest number and i * x for all numbers equals to x.
