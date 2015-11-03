class Solution:
    def buildpath(self, stack, path, start, result):                            #Use backtracking to construct all the pathes.
        if len(stack) == 0:
            return
        if stack[-1] == start:                                                  #If reaches start, append the reverse of stack to result.
            t = list(stack)                                                     #Watch out! Never ever shallow copy!!!
            t.reverse()
            result.append(t)
        else:
            for x in path[stack[-1]]:                                           #For every word that points to current word, append it to stack.
                stack.append(x)
                self.buildpath(stack, path, start, result)
                stack.pop()
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        if start == end:                                                        #If start equals end, just return it only.
            return [[start]]
        l = len(start)                                                          #Record the length of word.
        result = []
        path = {}                                                               #Use a dict to store all the words from that we can go to current key word.
        q = [start]                                                             #A queue to store all the words in current step.
        flag = False                                                            #Indicate if we have reach the end.
        while q != []:                                                          #BFS
            newq = []                                                           #Store all the words could be reached in next step.
            for x in q:
                for i in range(l):                                              #Traverse through every index of current word.
                    for j in range(26):                                         #Traverse the alphabet.
                        t = x[:i] + chr(ord('a') + j) + x[i + 1:]               #Form the new word.
                        if t != x:                                              #The new word has to be different from current word.
                            if t == end:                                        #If we reach the end, update path and flag.
                                flag = True
                                if end not in path:
                                    path[end] = [x]
                                else:
                                    path[end].append(x)
                            elif t in dict:                                     #If the new word is in dict, update path.
                                if t not in path:
                                    path[t] = [x]
                                    newq.append(t)                              #Append it to newq on its first appearance.
                                else:
                                    path[t].append(x)
            if flag is True:                                                    #If we reach the end, break.
                break
            for x in newq:                                                      #Remove existed word from dict.
                dict.remove(x)
            q = newq                                                            #Update the queue.
        if q == []:                                                             #If q is empty, i.e. can not find a path from start to end, return an empty list.
            return []
        stack = [end]                                                           #Use stack to store the path from end to start.
        self.buildpath(stack, path, start, result)                              #Use backtracking to construct all the pathes.
        return result
