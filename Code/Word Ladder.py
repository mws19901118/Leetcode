class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):             #This is a BFS problem
        alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        dict.add(end)                                     #add end string to dict
        length=len(start)
        queue=collections.deque([(start,1)])
        while queue:
            current=queue.popleft()
            currentWord=current[0]
            currentLength=current[1]
            if currentWord==end:
               return currentLength
            for i in range(0,length):
                formerPart=currentWord[:i]
                latterPart=currentWord[i+1:]
                for j in alphabet:                        #traverse the alphabet, thus the time complexity is O(length*26)
                    if j!=currentWord[i]:
                        nextWord=formerPart+j+latterPart
                        if nextWord in dict:
                            queue.append((nextWord,currentLength+1))
                            dict.remove(nextWord)
        return 0
