class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        nums.append(-1)                              #Append -1 to the end of nums.
        stack = [len(nums) - 1]                      #Use stack to store the indexes whose numbers are in strictly increasing order when traversing backwards.
        count = 0                                    #Initialize count.
        for i in reversed(range(len(nums) - 1)):     #Traverse original nums from 
            while nums[stack[-1]] >= nums[i]:        #Pop stack until the number on the index which is on the top of stack is smaller than nums[i].
                stack.pop()
            count += stack[-1] - i                   #Add stack[-1] - i to count because each subarray starting at i and ending before stack[-1] is valid.
            stack.append(i)                          #Append i to stack.
        return count
