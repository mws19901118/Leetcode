class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []                                            #Use a stack to store the index so that the numbers on these index form a monon decreasing array.
        for i, x in enumerate(nums):                          #Traverse nums.
            if not stack or nums[stack[-1]] > x:              #If stack is empty or the number on the index of top of stack is greater than x, append i to stack.
                stack.append(i)
        maxWidth = 0                                          #Initialize max width.
        for i in reversed(range(len(nums))):                  #Traverse nums from behind.
            while stack and nums[stack[-1]] <= nums[i]:       #While stack and the number on the index of top of stack is not greater than current number, it forms a ramp.
                maxWidth = max(maxWidth, i - stack.pop())     #Pop stack and update max width.
        return maxWidth                                       #Return max width.
