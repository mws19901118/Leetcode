class Solution:
    def backtracking(self, endWord: str, stack: List[str], previousWord: defaultdict(list), result: List[List[str]]) -> None:
        if not stack:                                                                                                       #If stack is empty, return.      
            return
        if stack[-1] == endWord:                                                                                            #If the top of stack is target, add a deepcopy of stack to result and then return.
            result.append(deepcopy(stack))
            return
        for x in previousWord[stack[-1]]:                                                                                   #Traverse each word in previousWord[stack[-1]].
            stack.append(x)                                                                                                 #Append x to stack.
            self.backtracking(endWord, stack, previousWord, result)                                                         #Keep backtracking.
            stack.pop()                                                                                                     #Pop stack.
        
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:                                                                                         #If endWord not in wordList, return [] directly.
            return []
        extendedWordSet = set(wordList + [beginWord])                                                                       #Add beginWord to workList and de-dupe.
        adjacentList = {w:[] for w in extendedWordSet}                                                                      #Initialize the adjacent list of each word.
        for w in extendedWordSet:                                                                                           #Traverse the extendedWordSet and build the adjacent list.
            for i in range(len(w)):                                                                                         #Replace each letter with another possible letter.
                for x in 'abcdefghijklmnopqrstuvwxyz':
                    if x == w[i]:                                                                                           #If new letter is same as old one, skip.
                        continue
                    newWord = w[:i] + x + w[i + 1:]                                                                         #Construct new word.
                    if newWord in adjacentList:                                                                             #If newWord is in adjacentList, append newWord to adjacentList[w].
                        adjacentList[w].append(newWord)
        q, visited = set([endWord]),  set([endWord])                                                                        #Start BFS from endWord.
        previousWord = defaultdict(list)                                                                                    #Store the previous words of each word.
        while q and beginWord not in q:                                                                                     #BFS while q is not empty and beginWord not in q.
            newq = set()                                                                                                    #Initialize newq.
            for x in q:                                                                                                     #Traverse each word in q.
                for y in adjacentList[x]:                                                                                   #Append the word in adjacentList[x] to newq if it's not visited.
                    if y not in visited:
                        newq.add(y)
                        previousWord[y].append(x)                                                                           #Also append x to previousWord[y].
            q = newq                                                                                                        #Replace q with newq.
            visited |= newq                                                                                                 #Update visited.
        result = []
        self.backtracking(endWord, [beginWord], previousWord, result)                                                       #Construct all paths from beginWord to endWord.
        return result                                                                                                       #Return result.
    
