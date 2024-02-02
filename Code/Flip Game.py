class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        return (currentState[:i] + "--" + currentState[i + 2:] for i in range(len(currentState )- 1) if currentState[i:i + 2] == '++')            #Flip each '++' to '--'.
