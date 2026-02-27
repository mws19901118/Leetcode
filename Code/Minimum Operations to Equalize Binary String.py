class Solution:
    def minOperations(self, s: str, k: int) -> int:
        unvisited = [SortedList(range(0, len(s) + 1, 2)), SortedList(range(1, len(s) + 1, 2))]    #Initialize unvisited sorted list, which is split by even and odd because 1 operation can only change the current count of 0 to either even or odd.
        q = [s.count('0')]                                                                        #Initialize q to be the current count of '0' in s.
        count = 0
        while q:                                                                                  #BFS.
            newq = []                                                                             #Initialize newq.
            for x in q:                                                                           #Traverse q.
                if not x:                                                                         #If x is 0, return count.
                    return count
                l, r = x + k - 2 * min(x, k), x + k - 2 * max(k - len(s) + x, 0)
                target = unvisited[l % 2]                                                         #Find the target by oddity.
                index = target.bisect_left(l)                                                     #Binary seaerch the left bound index in target.
                while index < len(target) and target[index] <= r:                                 #Iterate while index is not the end and target[index] is not greater than the upper bound.
                    newq.append(target[index])                                                    #Append target[index] to newq.
                    target.pop(index)                                                             #Pop the index from target.
            q = newq                                                                              #Replace q with newq.
            count += 1                                                                            #Increase count.
        return -1                                                                                 #Return -1 if cannot reach all '1'.
