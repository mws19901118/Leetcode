class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        start = 0                                                        #Find the possible start of a power subarray in nums[:k - 1].
        for i in range(1, k - 1):
            if nums[i] != nums[i - 1] + 1:
                start = i
        result = []
        for i in range(k - 1, len(nums)):                                #Traverse every end of k-size subarray.
            if nums[i] == nums[start] + k - 1 and i - start == k - 1:    #If nums[start:i + 1] is consecutive increasing, append nums[i] to result and move forward start.
                result.append(nums[i])
                start += 1
            else:                                                        #Otherwise, append -1 to result.
                result.append(-1)
                if nums[i] != nums[i - 1] + 1:                           #If nums[i] is not consecutive increasing with previous number, it is the new possible start.
                    start = i
        return result
