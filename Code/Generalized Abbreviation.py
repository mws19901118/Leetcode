class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        result = set()                                                        #Initialize result set.
        def backtracking(index: int, stack: List[str]) -> None:               #Backtracking for word[index:].
            if index == len(word):                                            #If index reaches the end, join stack and add to result.
                result.add("".join(stack))
            for i in range(index, len(word)):                                 #Traverse word[index:].
                if not (stack and stack[-1].isdigit()):                       #If stack is empty or the last in stack is not digit, we can abbreviate word[index:i + 1].
                    stack.append(str(i - index + 1))                          #Append str(i - index + 1) to stack.
                    backtracking(i + 1, stack)                                #Keep backtracking.
                    stack.pop()                                               #Pop stack.
                stack.append(word[index:i + 1])                               #Also handle not abbreviate by adding word[index:i + 1] to stack.
                backtracking(i + 1, stack)                                    #Keep backtracking.
                stack.pop()                                                   #Pop stack.
        
        backtracking(0, [])                                                   #Start backtracking from 0 and empty stack.
        return list(result)                                                   #Convert result to list and return.
