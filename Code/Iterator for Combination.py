class CombinationIterator:
    
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []                                                                  #Initialize combinations.
        self.index = 0                                                                          #Initialize pointer in combinations.
        self.DFS([], list(characters), combinationLength)                                       #Generate all combinations.
        
    def next(self) -> str:
        result = self.combinations[self.index]                                                  #Get result.
        self.index += 1                                                                         #Move pointer.
        return result                                                                           #Return result.

    def hasNext(self) -> bool:
        return self.index < len(self.combinations)                                              #Return if pointer has reached the end.

    def DFS(self, stack: List[str], characters: List[str], combinationLength: int) -> None:     #DFS.
        if len(stack) == combinationLength:                                                     #If stack length equals combinationLength, join the characters in stack and append to self.combinations.
            self.combinations.append("".join(stack))
            return
        remainLength = combinationLength - len(stack)                                           #Calculate remain length.
        for i in range(len(characters) - remainLength + 1):                                     #Traverse the rest of characters until cannot make valid combination.
            stack.append(characters[i])                                                         #Append current character to stack.
            self.DFS(stack, characters[i + 1:], combinationLength)                              #Keep DFS.
            stack.pop()                                                                         #Pop stack.
                
# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
