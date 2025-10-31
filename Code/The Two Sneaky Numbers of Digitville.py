class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = Counter(nums)                            #Count numbers.
        return [x for x in count if count[x] == 2]       #Return the numbers occurred twice.
