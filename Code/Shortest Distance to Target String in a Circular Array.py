class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:                                                                                                                                      #If target is not in words, return -1.
            return -1
        return min(min(abs(i - startIndex), abs(i + len(words) - startIndex), abs(startIndex + len(words) - i)) for i, x in enumerate(words) if x == target)         #Traverse words, and find the shortest distance if current word is target among direct from start index to current idnex, go right circularly from start index or go left circularly from start index.
