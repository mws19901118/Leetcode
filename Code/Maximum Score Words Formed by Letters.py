class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letterCount = Counter(letters)                                                                                #Count each letter.
        wordLetterCount, wordScore = defaultdict(Counter), defaultdict(int)                                           #Count letters in each word and calculate the score for each word.
        for word in words:                                                                                            #Populate wordLetterCount and wordScore.
            wordLetterCount.append(Counter(word))
            wordScore.append(sum(v * score[ord(k) - ord('a')] for k, v in wordLetterCount[-1].items()))

        def backtracking(index: int) -> int:                                                                          #Backtracking.
            if index == len(words):                                                                                   #If reaches the end of words, return 0.
                return 0
            result = backtracking(index + 1)                                                                          #Calculate result of not picking current word.
            if all(wordLetterCount[index][x] <= letterCount[x] for x in wordLetterCount[index]):                      #We can pick current word if for each letter in current word, there are no fewer count in letterCount.
                for x in wordLetterCount[index]:                                                                      #Update letter count for each letter in current word.
                    letterCount[x] -= wordLetterCount[index][x]
                result = max(result, backtracking(index + 1) + wordScore[index])                                      #Calculate result of picking current word.
                for x in wordLetterCount[index]:                                                                      #Restore letter count for each letter in current word.
                    letterCount[x] += wordLetterCount[index][x]
            return result
        return backtracking(0)                                                                                        #Return the result of backtracking starting at index 0.
