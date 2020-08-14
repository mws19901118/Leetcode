class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinationsInBinary = []                                                      #Store all possible combinations in binary(binary whose count of '1' equals combinationLength).
        self.index = 0                                                                      #Index of the iterator.
        self.characters = characters
        self.generateCombinationsInBinary(len(characters), combinationLength)               #Generate all combinations in binary.
        
    def next(self) -> str:
        binary = self.combinationsInBinary[self.index]                                      #Get the combination in binary string.
        self.index += 1                                                                     #Move to next index.
        s = "".join([self.characters[i] for i in range(len(binary)) if binary[i] == '1'])   #Convert from binary string to combination by joining all character in characters whose corresponding bit in binary is '1'.
        return s

    def hasNext(self) -> bool:
        return self.index < len(self.combinationsInBinary)                                  #Return if index has reached the end.

    def generateCombinationsInBinary(self, length: int, combinationLength: int):
        upperBound = (1 << length) - 1                                                      #The upper bound of binary is 2 ^ length - 1, length is the length of characters.
        for i in range(upperBound, 0, -1):                                                  #From upper bound to 0, find possible combinations in binary.
            b = "{0:b}".format(i).zfill(length)                                             #Convert to binary string.
            if b.count("1") == combinationLength:                                           #If the count of '1' equals combinationLength, add it to combinationsInBinary list.
                self.combinationsInBinary.append(b)
                
# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
