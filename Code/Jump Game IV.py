class Solution:
    def minJumps(self, arr: List[int]) -> int:
        indexes = collections.defaultdict(set)                                      #Store the indexes in set by value.
        for i, x in enumerate(arr):
            indexes[x].add(i)
        q, visited = set([0]), set([0])                                             #Initialize queue and visited set.
        count = 0
        while q:                                                                    #BFS.
            newq = set()                                                            #Initialize new queue.
            for x in q:                                                             #Traverse q.
                if x == len(arr) - 1:                                               #If x is the end, return count.
                    return count
                if x - 1 >= 0 and x - 1 not in visited:                             #If x - 1 is valid and not visited, add (x - 1) to newq.
                    newq.add(x - 1)
                if x + 1 < len(arr) and x + 1 not in visited:                       #If x + 1 is valid and not visited, add (x + 1) to newq.
                    newq.add(x + 1)
                newq |= indexes[arr[x]]                                             #Add all indexes whose value is same as arr[x] to newq.
                indexes[arr[x]].clear()                                             #Clear indexes[arr[x]].
                if x in newq:                                                       #Remove if from newq if x is in newq.
                    newq.remove(x)
            q = newq                                                                #Replace q with newq.
            visited |= newq                                                         #Update visited.
            count += 1                                                              #Increase count.
        return count
