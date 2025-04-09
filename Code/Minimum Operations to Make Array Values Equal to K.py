class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s, min_v = set(nums), min(nums)                          #Find distinct numbers and min value in nums.
        return -1 if k > min_v else len(s) - (k == min_v)        #If k > min_v, cannot make all numbers equal to k so return -1; otherwise, return len(s) - (k == min_v).
                                                                 #Basically, if k == min_v, we only need len(s) - 1 operations; otherwise, we need len(s) operations.
