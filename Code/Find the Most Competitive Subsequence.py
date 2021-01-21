class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []                                                #Use a stack to store the possible smallest number starting from the previous smallest number, so the numbres in stack is in non-desending order.
        selected = 0                                              #Indicate how many numbers from the beginning of the stack have been selected into the most competitive subsequence.
        for i, x in enumerate(nums):                              #Traverse nums.
            while len(stack) > selected and stack[-1] > x:        #While the length of stack is larger than selected and stack top is larger than current value, pop stack.
                stack.pop()
            stack.append(x)                                       #Push current value to stack.
            if i >= len(nums) - k:                                #Increse selected if current index is greater than len(nums) - k.
                selected += 1
        return stack[:selected]                                   #Return the first k numbers in stack.
