class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lastOne = -1                                            #Record the index of last 1.
        for i, x in enumerate(nums):
            if x:
                if lastOne != -1 and i - lastOne < k + 1:       #If the gap between current 1 and last one is smaller than k + 1, return false directly.
                    return False
                else:                                           #Otherwise, update index of last 1.
                    lastOne = i
        return True                                             #Return true.
