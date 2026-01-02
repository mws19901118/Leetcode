class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = Counter(nums)                        #Count each element.
        for x in count:                              #Traverse count.
            if count[x] == len(nums) // 2:           #Find the N-repeated element and return.
                return x
