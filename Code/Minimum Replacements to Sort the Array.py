class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count, upperBound = 0, nums[-1]                #Initialize operation count and upper bound.
        for x in reversed(nums):                       #Traverse nums backward from end, because one operation can only make number smaller, so we can only fix numbers in the back first then "sort" number in the front with operations.
            times = ceil(x / upperBound)               #Compute the times of current number to upper bound.
            upperBound = x // times                    #To divide x into multiple numbers which are all smaller than upper bound and keep the smallest number as large as posssible, we just need to divide x evenly. Then update upper bound.
            count += times - 1                         #It takes times - 1 operations to divide x into "times" number.
        return count
