class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)                            #Get the length.
        prefix = [0] * n + [1] + [0] * n         #Suppose we transform nums to an array delta that at the position, set the value to 1 if it is target, -1 otherwise. The prefix sum of delta is from -n to n, inclusive. Then intialize prefix, which is the count(offset by n) of each prefix sum value of delta.
        result, curr, count = 0, 0, n            #Initialize result, valid subarrays ending at current index and count. The initial value of count because it is used to find the value in prefix array; the actual count is offset by n.
        for i, x in enumerate(nums):             #Traverse nums.
            if x == target:                      #Handle the case if current number is target.
                curr += prefix[count]            #There are prefix[count] more subarrays ending at current index. Because for index j such that delta[j] == count, sum(delta[j + 1:i + 1]) > 0, which means nums[j + 1:i + 1] has target as the majority element.
                count += 1                       #Increase count.
            else:                                #Handle the case if current number is not target.
                count -= 1                       #Decrease count.
                curr -= prefix[count]            #Revert the effect of line 8.
            prefix[count] += 1                   #Increase prefix[count].
            result += curr                       #Add curr to result.
        return result
