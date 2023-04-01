class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.indexes = defaultdict(list)                                                        #Use a dict to store the list of indexes of every word.
        for i, x in enumerate(wordsDict):
            self.indexes[x].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        result, i, j = float('inf'), 0, 0                                                       #Use 2 pointers to traverse the indexes of word1 and word2 respectively.
        while i < len(self.indexes[word1]) and j < len(self.indexes[word2]):
            result = min(result, abs(self.indexes[word1][i] - self.indexes[word2][j]))          #Update result.
            if self.indexes[word1][i] < self.indexes[word2][j]:                                 #If current index of word1 is smaller than that of word2, move forward i.
                i += 1
            else:                                                                               #Otherwise, move forward j.
                j += 1
        return result
