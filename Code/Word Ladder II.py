class Solution:
    def DFS(self, stack: List[int], wordList: List[str], target: int, wordIndex: defaultdict, prev: defaultdict(list), result: List[List[str]]):
        if stack[-1] == target:                                                                                 #If the top of stack is target, convert each index to its word and append the converted stack to result, then return.
            result.append([wordList[i] for i in stack])
            return
        for x in prev[stack[-1]]:                                                                               #Traverse each index in prev[stack[-1]].
            stack.append(x)                                                                                     #Append x to stack.
            self.DFS(stack, wordList, target, wordIndex, prev, result)                                          #Keep DFS.
            stack.pop()                                                                                         #Pop stack.
        
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:                                                                             #If endWord not in wordList, return [] directly.
            return []
        wordList.append(beginWord)                                                                              #Append beginWord to wordList.
        wordIndex = {w: i for i, w in enumerate(wordList)}                                                      #Get the word to index mapping.
        adjacentList = defaultdict(list)                                                                        #Intialize adjacent list.
        for i, w in enumerate(wordList):                                                                        #Traverse wordList.
            for j in range(len(w)):                                                                             #Try replace each letter in w with other letters.
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == w[j]:
                        continue
                    newWord =w[:j] + c + w[j + 1:]                                                              #Get the word after replacing one letter.
                    if newWord in wordIndex:                                                                    #If it's in wordIndex, build an edge from i to wordIndex[newWord].
                        adjacentList[i].append(wordIndex[newWord])
        
        q, visited = set([wordIndex[endWord]]), t([wordIndex[endWord]])                                         #Initalize queue set and visited set for BFS, starting with endWord.
        prev = defaultdict(list)                                                                                #Initalize the previous words in BFS for each word.
        while q:                                                                                                #BFS.
            newq = set()                                                                                        #Initalize new queue.
            for w in q:                                                                                         #Traverse each index in q.
                if w == wordIndex[beginWord]:                                                                   #If current index is the index of beginWord, break.
                    break
                for x in adjacentList[w]:                                                                       #Traverse the indexes in adjacent list of w.
                    if x not in visited:                                                                        #If x is not visited, add it to newq and append w to prev[x].
                        newq.add(x)
                        prev[x].append(w)
            q = newq                                                                                            #Replace q with newq.
            visited |= newq                                                                                     #Update visited so all indexes in newq are visited.
        
        if not prev[wordIndex[beginWord]]:                                                                      #If beginWord index has no previous word index, we can not reach from beginWord to endWord, return []. 
            return []
        result = []                                                                                             #Initialize result.
        self.DFS([wordIndex[beginWord]], wordList, wordIndex[endWord], wordIndex, prev, result)                 #DFS to build all sequences.
        return result                                                                                           #Return result.
