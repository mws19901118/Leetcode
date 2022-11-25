class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []                                                #Initialize a stack to store the index of min values so far and the sum of minimum of subarrays ending at them after taking modulo.
        division = 10 ** 9 + 7                                    #Division is 10 ** 9 + 7.
        result = 0                                                #Initialize result.
        for i, x in enumerate(arr):                               #Traverse arr.
            while stack and arr[stack[-1][0]] >= x:               #While stack and the value on index on top of stack is greater than or equal to x, pop stack.
                stack.pop()
            index, count = stack[-1] if stack else (-1, 0)        #Get the top of stack; if stack is empty, default value is -1 and 0.
            newCount = ((i - index) * x + count) % division       #Subarrays starting from arr[index + 1:i + 1] and ending at i will have minimum being x. So, the sum of minimum of subarrays ending at them after taking modulo is previous value + (i - index) * x, then taking modulo.
            stack.append((i, newCount))                           #Append (i, newCount) to stack.
            result = (result + newCount) % division               #Append newCount to stack and update result.
        return result                                             #Return result.
