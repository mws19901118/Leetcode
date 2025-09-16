class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []                                                            #Store numbers in a stack.
        for x in nums:                                                        #Traverse nums.
            stack.append(x)                                                   #Append x to stack.
            while len(stack) >= 2 and gcd(stack[-1], stack[-2]) != 1:         #While there are at least 2 numbers in stack and the top 2 numbers are not coprime, pop them and append their LCM back to stack.
                stack.append(lcm(stack.pop(), stack.pop()))
        return stack                                                          #Return stack.
