class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        count = Counter([x - int(str(x)[::-1]) for x in nums])                                #Count numbers by x - rev(x).
        return sum(count[x] * (count[x] - 1) // 2 for x in count) % (10 ** 9 + 7)             #nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]) is equivalent to nums[i] - rev(nums[i]) == nums[j] - rev(nums[j]).
                                                                                              #So, sum up count[x] * (count[x] - 1) // 2 for each key in count, then return after taking mod.
