class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = Counter([nums[i] * nums[j] for i in range(len(nums)) for j in range(i + 1, len(nums))])        #Count the tuple product.
        return sum(x * (x - 1) * 4 for x in count.values())                                                    #For each permutation of tuple (a, b) and (c, d), there are 4 sub-permutations. So, sum up and return.
