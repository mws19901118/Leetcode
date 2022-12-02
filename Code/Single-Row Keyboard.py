class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        indexes = {x: i for i, x in enumerate(keyboard)}        #Find the indexes of each character in keyboard.
        location, count = 0, 0                                  #Initially finger at location 0.
        for x in word:                                          #Traverse word.
            count += abs(indexes[x] - location)                 #Add the distance from last location to index of current character to count.
            location = indexes[x]                               #Update location to index of current character.
        return count
