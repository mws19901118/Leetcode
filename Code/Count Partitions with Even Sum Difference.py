class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total, s, result = sum(nums), 0, 0          #Initialize total sum, running sum from beginning of nums and result.
        for x in nums[:-1]:                         #Traverse nums[:-1].
            s += x                                  #Update s.
            result += 1 - abs(total - s * 2) & 1    #Check if the partition difference is even then update result.
        return result
