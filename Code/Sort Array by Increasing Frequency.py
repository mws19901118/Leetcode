class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)                                      #Count each number.
        return sorted(nums, key = lambda x: (count[x], -x))        #Sort by count then the negative value.
