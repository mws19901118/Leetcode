class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0                                                       #Initialize matching count.
        currentCharacters = defaultdict(deque)                          #Store the pointer(index of word in words and index of character in word) to the current unmatched characters of each word in a queue and hashed by the character.
        for i, w in enumerate(words):                                   #Initially, every pointer is in the start of corresponding word.
            currentCharacters[w[0]].append((i, 0))
        for x in s:                                                     #Traverse s.
            c = len(currentCharacters[x])                               #Get length of the queue of current character.
          for i in range(c):                                            #Traverse the first c items in queue.
                i, j = currentCharacters[x].popleft()                   #Popleft item to get pointer.
                j += 1                                                  #Move pointer to next charcter in word.
                if j == len(words[i]):                                  #If reaches the end of the word, then that word is a subsequences, so increase count.
                    count += 1
                else:                                                   #Otherwise, push current pointer to the queue hashed by current character.
                    currentCharacters[words[i][j]].append((i, j))
        return count
