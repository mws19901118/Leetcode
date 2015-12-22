class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.words = words
        self.dict = {}                                    #Use a dict to store the list of indices of every word.
        for i in range(len(self.words)):
            if self.words[i] not in self.dict:
                self.dict[words[i]] = [i]
            else:
                self.dict[words[i]].append(i)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = self.dict[word1]                             #Get the corresponding lists of indices.
        l2 = self.dict[word2]
        i = 0                                             #Pointer in l1.
        j = 0                                             #Pointer in l2.
        result = len(self.words)
        while i < len(l1) and j < len(l2):                #Find the shortest distance.
            result = min(result, abs(l1[i] - l2[j]))
            if l1[i] > l2[j]:                             #If current index of word1 is larger than that of word2, move forward j.
                j += 1
            else:                                         #Otherwise, move forward i.
                i += 1
        return result

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
