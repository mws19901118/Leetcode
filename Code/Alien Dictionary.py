class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjacentList, indegree, letters = defaultdict(list), Counter(), set()                            #Initialize adjacent list, indegree and letters.
        for x in words:                                                                                  #Traverse each word and add each leeter to letters.
            for y in x:
                letters.add(y)
        for i in range(len(words) - 1):                                                                  #Traverse each adjacent pair of words.
            j, k = 0, 0
            while j < len(words[i]) and k < len(words[i + 1]) and words[i][j] == words[i + 1][k]:        #Traverse 2 words simultonously until they diverge.
                j += 1
                k += 1
            if j < len(words[i]) and k == len(words[i + 1]):                                             #If k reaches end first, it is invalid, so return "" directly.
                return ""
            if j < len(words[i]) and k < len(words[i + 1]):                                              #Add words[i + 1][k] to the adjacent list of words[i][j] also increase indegree of words[i + 1][k].
                adjacentList[words[i][j]].append(words[i + 1][k])
                indegree[words[i + 1][k]] += 1
        result = []
        dq = deque([x for x in letters if not indegree[x]])                                              #Find the starting letters whose indegree is 0.
        while dq:                                                                                        #Topological sort in BFS.
            x = dq.popleft()
            result.append(x)
            for y in adjacentList[x]:
                indegree[y] -= 1
                if not indegree[y]:
                    dq.append(y)
        return "" if len(result) < len(letters) else "".join(result)                                     #If not all letters are in result, there are cycles, so return ""; otherwise, join result and return.
