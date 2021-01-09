class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)                                                         #Put all words in wordList in a set.
        q = set([beginWord])
        currentLength = 1
        while q:                                                                        #BFS.
            newq = set()
            for currentWord in q:
                if currentWord == endWord:                                              #If reaches the end, return current length.
                    return currentLength
                for i in range(len(currentWord)):                                       #Enumerate each position of current word.
                    for c in "abcdefghijklmnopqrstuvwxyz":                              #Also, enumerate each letter.
                        if c != currentWord[i]:
                            nextWord = currentWord[:i] + c + currentWord[i + 1:]        #Generate new word.
                            if nextWord in wordSet:                                     #If it's in the word set, add it to new q and remove it from word set.
                                newq.add(nextWord)
                                wordSet.remove(nextWord)
            currentLength += 1                                                          #Increase current length.
            q = newq                                                                    #Replace q with new q.
        return 0                                                                        #If cannot reach end word, return 0.
