class Solution:
    def getBitMask(self, word: str) -> int:                                                   #Compute the bit mask for a string.
        mask = 0
        for c in word:
            mask |= 1 << ord(c) - ord('a')
        return mask
    
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        letterFrequencies = defaultdict(int)                                                  #Count the appearance of each bit mask of words.
        for word in words:
            mask = self.getBitMask(word)
            letterFrequencies[mask] += 1
        
        result = []                                                                           #Initialize result.
        
        for puzzle in puzzles:                                                                #Traverse puzzles.
            mask = self.getBitMask(puzzle)                                                    #Get the bit mask of puzzle.
            subMask = mask                                                                    #Initialize the bit mask of each subset of letters in puzzle, initially it's same as mask.
            count = 0                                                                         #Initialize count.
            firstLetterBitMask = 1 << (ord(puzzle[0]) - ord('a'))                             #Get the bit mask of first letter of puzzle.
            while subMask:                                                                    #Loop while submask is not 0.
                if subMask & firstLetterBitMask:                                              #If current subMask contains the first letter of puzzle, add the number of words whose bit mask is same as subMask to count because all their letters are in a subset of puzzle.
                    count += letterFrequencies[subMask]
                subMask = (subMask - 1) & mask                                                #Go to next subset.
            result.append(count)                                                              #Append count to result/
        return result
