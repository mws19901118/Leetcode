class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1                                #Initialize 2 pointers at the beginning and the end of nums.
        result = []
        while i <= j:                                          #Iterate while 2 pointers not meet.
            if abs(nums[i]) >= abs(nums[j]):                   #If abs(nums[i]) is not smaller than abs(nums[j]), append nums[i] * nums[i] and move i forward.
                result.append(nums[i] * nums[i])
                i += 1
            else:                                              #Otherwise, append nums[j] * nums[j] and move j backward.
                result.append(nums[j] * nums[j])
                j -= 1
        return result[::-1]                                    #Reverse the result and return.
