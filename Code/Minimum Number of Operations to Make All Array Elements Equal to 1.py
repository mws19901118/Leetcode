class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)                                              #Count numbers in nums.
        if count[1]:                                                       #If there are 1 in nums, return len(nums) - count[1], as the gcd of 1 and any number is 1.
            return len(nums) - count[1]
        length = inf                                                       #Initialize the min length of any subarray whose gcd is 1.
        for i, x in enumerate(nums):                                       #Traverse nums.
            g = x                                                          #Initialize the gcd of current subarray.
            for j in range(i + 1, len(nums)):                              #Traverse nums[i + 1:].
                g = gcd(g, nums[j])                                        #Calculate gcd.
                if g == 1:                                                 #If gcd is 1, update length and break.
                    length = min(length, j - i + 1)
                    break
        return -1 if length == inf else length - 1 + len(nums) - 1         #If length is inf, we cannot get an 1, so return -1; otherwise, it taks length - 1 to get an 1, then len)nums) - 1 to convert the rest of nums to 1.
