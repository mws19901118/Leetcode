class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums[:k])          #Count each number in nums[:k].
        result = [len(count)]              #Initialize result with the length of count.
        for i in range(k, len(nums)):      #Traverse from k to the end of nums.
            count[nums[i]] += 1            #Increase count[nums[i]].
            count[nums[i - k]] -= 1        #Decrease count[nums[i - k]].
            if not count[nums[i - k]]:     #If count[nums[i - k]] is 0, pop it from count.
                count.pop(nums[i - k])
            result.append(len(count))      #Append the length of count to result.
        return result
