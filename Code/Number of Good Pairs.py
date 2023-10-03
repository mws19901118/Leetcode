class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)                                          #Count each number in nums.
        return sum([x * (x - 1) // 2 for x in count.values()])         #For each number occurrence i, it can form i - 1 good pairs with occurrences before it. So, in total x * (0 + x - 1) // 2 for total occurrences x of any number.
