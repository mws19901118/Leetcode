class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = Counter(x - i for i, x in enumerate(nums))                                                #Count nums[i] - i.
        return len(nums) * (len(nums) - 1) // 2 - sum(x * (x - 1) // 2 for x in count.values())           #If 2 pairs i, j (i < j) are not bad, then nums[i] - i = nums[j] - j. So calculate total pairs and then substract the not bad pairs.
