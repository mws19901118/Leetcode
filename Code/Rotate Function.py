class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s = sum(nums)                                    #Calculate sum of nums.
        f = sum(i * x for i, x in enumerate(nums))       #Calculate F(0).
        result = f                                       #Initialize result to be F(0).
        for x in reversed(nums[1:]):                     #Traverse nums[1:] backwards.
            f += s - len(nums) * x                       #F(0) = 0 * nums[0] + 1 * nums[1] + ... + (n - 1) * nums[n - 1]. F(1) = 0 * nums[n - 1] + 1 * nums[2] + ... + (n - 1) * nums[n - 2] = F(0) + s - n * nums[n - 1]. In same fashion, we can derive the equaltion that F(i + 1) = F(i) + s - n * nums[-i]. 
            result = max(result, f)                      #Update result if necessary.
        return result
