# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def generate(self, possibleGuess, guessed, matchCount):                                         #Generate the index of word to guess given possible guesses, the guessed indexes and the matrix of match count between each pair of words. 
        guessGroup, finalGuess = possibleGuess, None                                                #Initialize guess group and final guess. Guess group should be as same as possible guesses.
        for guess in possibleGuess:                                                                 #Traverse each possible guess.
            row = matchCount[guess]
            groups = [[] for _ in range(7)]
            for j in possibleGuess:                                                                 #Group each index of word in possible guess other than guess itself by the match count between them and guess.
                if j != guess:
                    groups[row[j]].append(j)
            maxgroup = max(groups, key = len)                                                       #Find the longest length in current group.
            if len(maxgroup) < len(guessGroup):                                                     #Find the shortest longest length for each guess to be final guess, minimizing the maximum possible size of the resulting word list.
                guessGroup, finalGuess = maxgroup, guess

        return finalGuess
    
    def findSecretWord(self, wordlist, master):
        n = len(wordlist)
        matchCount = [[sum(a == b for a, b in zip(wordlist[i], wordlist[j]))                                        #Generate the matrix of match count between each pair of words.
                   for j in range(n)] for i in range(n)]

        possibleGuess, guessed = range(n), set()                                                                    #Initalize possible guesses and guessed.
        while possibleGuess:                                                                                        #While we have possible words to guess.
            guess = self.generate(possibleGuess, guessed, matchCount)                                               #Generate the word index to guess.
            matches = master.guess(wordlist[guess])                                                                 #Guess word.
            if matches == len(wordlist[0]):                                                                         #If matches guessed equals to word length, return.
                return
            guessed.add(guess)                                                                                      #Add current guess index to guessed.
            possibleGuess = [j for j in possibleGuess if matchCount[guess][j] == matches and j not in guessed]      #Generate possible guesses. Only words whose match count equals to matches are possible.
