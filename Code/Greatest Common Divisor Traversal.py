class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        primeToIndex, indexToPrime = defaultdict(list), defaultdict(list)        #Using adjacent list to store the connection between each index and each prime number if the prime is a factor of number on index.
        for i, x in enumerate(nums):                                             #Traverse nums.
            for j in range(2, floor(sqrt(x)) + 1):                               #Traverse from 2 to floor(sqrt(x)) + 1).
                if x % j == 0:                                                   #If x can be divided by j, build an edge from index i to prime j and vice versa.
                    primeToIndex[j].append(i)
                    indexToPrime[i].append(j)
                    while x % j == 0:                                            #Divide all j from x.
                        x //= j
            if x > 1:                                                            #If x > 1, then x is a prime now, also build an edge from index i to prime j and vice versa.
                primeToIndex[x].append(i)
                indexToPrime[i].append(x)

        visitedIndex, visitedPrime = set(), set()                                #Store visited index and visited prime.
        q = deque([0])                                                           #Initialize queue from index 0.
        while q:                                                                 #BFS.
            index = q.popleft()                                                  #Popleft the first index.
            if index in visitedIndex:                                            #If it is already visited, continue.
                continue
            visitedIndex.add(index)                                              #Add current index to visited.
            for p in indexToPrime[index]:                                        #Traverse all prime factors of number on current index.
                if p in visitedPrime:                                            #If p is visited, continue.
                    continue
                visitedPrime.add(p)                                              #Add p to visited.
                for x in primeToIndex[p]:                                        #Traverse all index whose number has a factor p.
                    if x not in visitedIndex:                                    #If x is not visited, append x to q.
                        q.append(x)

        return len(visitedIndex) == len(nums)                                    #Return if the length of visitedIndex is same as length of nums, basically meaning that all indexes are connected in graph.
