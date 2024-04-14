class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minV, maxV = min(nums), max(nums)                #Find the min value and max value in nums.
        count = [0] * (maxV - minV + 1)                  #Initialzie a list for the count of each number in [minV, maxV].
        for x in nums:                                   #Traverse nums.
            count[x - minV] += 1                         #Populate count.
        for i in reversed(range(len(count))):            #Traverse count backwards.
            k -= count[i]                                #Reduce count[i] from k.
            if k <= 0:                                   #If k <= 0, return the corresponding number minV + i.
                return minV + i
