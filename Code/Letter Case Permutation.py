class Solution:
    def DFS(self, S: str, stack: List[str], result: List[str]):       #DFS.
        if not S:                                                     #If reaches the end, join stack and append to result.
            result.append("".join(stack))
            return
        if S[0].isalpha():                                            #If S[0] is letter, DFS with its upper case and lower case respectively.
            stack.append(S[0].upper())
            self.DFS(S[1:], stack, result)
            stack.pop()
            stack.append(S[0].lower())
            self.DFS(S[1:], stack, result)
            stack.pop()
        else:                                                         #If S[0] is number, continue DFS with itself.
            stack.append(S[0])
            self.DFS(S[1:], stack, result)
            stack.pop()
    def letterCasePermutation(self, S: str) -> List[str]:
        result = []
        self.DFS(S, [], result)                                       #Start DFS.
        return result                                                 #Return result.
