class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        division = 10 ** 9 + 7                                                      #Initialize division.
        nums.sort()                                                                 #Sort nums in asending order, since it's asking for subsequence, so order doesn't matter.
        result = 0                                                                  #Initialize result.
        rightBound = len(nums)                                                      #Initialize the right bound for binary search.
        for i, x in enumerate(nums):                                                #Traverse nums.
            index = bisect_right(nums, target - x, i, rightBound)                   #Binary search the rightmost index to insert target - x between i and rightBound. 
            if index > i:                                                           #If index > i, there is at least one non-empty sebsequence guranteed.
                result = (result + (1 << (index - i - 1))) % division               #Add 2 ** (index - i - 1) to result and take modulo, because there are 2 ** (index - i - 1) to form valid subseqence starting with x. 
                rightBound = index                                                  #Update rightBound, because next binary search will be searching for value not larger than target - x.
        return result                                                               #Return result.
