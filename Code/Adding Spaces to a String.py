class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        indexes = [0] + spaces + [len(s)]                                                    #Add the start and end index of s to the ends of spaces respectively.
        return " ".join(s[indexes[i]:indexes[i + 1]] for i in range(len(indexes) - 1))       #Traverse indexes to cut s into small pieces and join with space then return.
