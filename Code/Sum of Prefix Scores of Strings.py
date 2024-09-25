class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        score = Counter()                            #Count the score of each prefix.
        for w in words:                              #Traverse words.
            for i in range(len(w)):                  #Traverse each prefix of w.
                score[w[:i + 1]] += 1                #Increase its score.
        result = [0] * len(words)                    #Initialize result.
        for index, w in enumerate(words):            #Traverse words.
            for i in range(len(w)):                  #Traverse each prefix of w.
                result[index] += score[w[:i + 1]]    #Add its score to corresponding result.
        return result
