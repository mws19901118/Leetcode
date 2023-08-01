class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(length: int, last: int) -> None:             #Backtracking with current length and last value.
            if length == k:                                        #If the length is k, add a copy of stack to result and return.
                result.append(stack.copy())
                return
            for v in range(last + 1, n - k + length + 2):          #Traverse all the possible value.
                stack.append(v)                                    #Push value to stack.
                backtrack(length + 1, v)                           #Keep backtracking.
                stack.pop()                                        #Pop value from stack.
        result, stack = [], []                                     #Initialize result and stack.
        backtrack(0, 0)                                            #Start from length 0 and last value 0.
        return result
