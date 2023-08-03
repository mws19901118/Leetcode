class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}        #Initialize mapping.
        result, stack = [], []                                                                                                #Initialize result and stack.
        def backtrack() -> None:                                                                                              #Backtracking.
            if len(stack) == len(digits):                                                                                     #If all digits are mapped, backtrack comes to end. 
                if len(digits) > 0:                                                                                           #If digits is not empty, join stack and append it to result.
                    result.append("".join(stack))
                return
            for x in letterMap[digits[len(stack)]]:                                                                           #Traverse the mapping letters of current digit.
                stack.append(x)                                                                                               #Append x to stack.
                backtrack()                                                                                                   #Keep backtracking.
                stack.pop()                                                                                                   #Pop stack.
        backtrack()                                                                                                           #Start backtracking.
        return result
