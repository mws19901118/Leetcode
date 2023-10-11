class Solution:
    def minOperations(self, nums: List[int]) -> int:
        distinct_nums = sorted(set(nums))                      #Sort distinct elements in nums.
        result = len(nums)                                     #Initialize result to be length pf nums, meaning all numbers have to be replaced.
        for i, x in enumerate(distinct_nums):                  #Traverse distinct elements.
            right = x + len(nums) - 1                          #Suppose x is the min number after replacement. Then valid max number is x + len(nums) - 1.
            index = bisect_right(distinct_nums, right)         #Binary search for the index of first element greater than right in distinct elements.
            result = min(result, len(nums) - index + i)        #Then all elements in distinct_nums[i:index] don't have to be replaced and we replace the rest(n - index + i). Update result if it is smaller.
        return result
