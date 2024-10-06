class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        def areSimilar(longer: str, shorter: str) -> bool:                                                                          #Determine if a longer sentence is similar with a shorted sentence.
            wordsLonger, wordsShorter = longer.split(" "), shorter.split(" ")                                                       #Split longer sentence and shorted sentence to words respectively.
            i = 0                                                                                                                   #Traverse from front in both longer words and shorted words until reaches end or they diverge.
            while i < len(wordsLonger) and i < len(wordsShorter) and wordsLonger[i] == wordsShorter[i]:
                i += 1
            j = -1                                                                                                                  #Traverse from behind in both longer words and shorted words until reaches i or they diverge.
            while len(wordsLonger) + j >= i and len(wordsShorter) + j >= i and wordsLonger[j] == wordsShorter[j]:
                j -= 1
            return len(wordsShorter) + j < i                                                                                        #If i meets j in shorter words, then we can insert wordsLonger[i:len(wordsLonger) + j + 1] at wordsShorter[i] to make 2 sentences equal, thus 2 sentences are similar.

        return areSimilar(sentence1, sentence2) if len(sentence1) >= len(sentence2) else areSimilar(sentence2, sentence1)           #Return areSimilar(sentence1, sentence2) if sentence1 is longer; otherwise return areSimilar(sentence2, sentence1).
