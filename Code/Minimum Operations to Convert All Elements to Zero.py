class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []                                  #Store visited number is an increasing stack.
        count = 0                                   #Count the operations.
        for x in nums:                              #Traverse nums.
            while stack and stack[-1] > x:          #While stack is not empty and top of the stack is greater than x, pop stack(the operations of these numbers are already counted and no 2 equal numbers can be changed to 0 if there is a smaller number in between).
                stack.pop()
            if x and (not stack or stack[-1] < x):  #If x is not 0 and stack is empty or top of the stack is smaller than x, we need a new operation to change x to 0.
                count += 1
                stack.append(x)                     #Also append x to stack.
        return count
