class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefixRemainder = [0]                                            #Store the prefix sum remainder by p.
        for i, x in enumerate(nums):
            prefixRemainder.append((x + prefixRemainder[-1]) % p)
        if not prefixRemainder[-1]:                                      #If the last prefix sum remainder is 0, then the sum of nums is divisible by p and no need to remove any subarray.
            return 0
        rightmostIndex = defaultdict(lambda: -1)                         #Store the rightmost index of each prefix sum remainder.
        result = len(nums)                                               #Initialize the result to be length of nums.
        for i, x in enumerate(prefixRemainder):                          #Traverse prefix sum remainders.
            rightmostIndex[x] = i                                        #Update the rightmost index of current prefix sum remainder.
            start = (x - prefixRemainder[-1]) % p                        #Calculate the start so that the sum of nums[rightmostIndex[start]:i] divide by p has remainder equals prefixRemainder[-1].
            if rightmostIndex[start] != -1:                              #If rightmostIndex[start] is not -1, update result if i - rightmostIndex[start] is smaller.
                result = min(result, i - rightmostIndex[start])
        return -1 if result == len(nums) else result                     #Return -1 if result is still length of nums; otherwise, return result.
