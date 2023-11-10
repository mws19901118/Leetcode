class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neighbors = defaultdict(list)                                                  #Store the neighbors of each number.
        for x, y in adjacentPairs:
            neighbors[x].append(y)
            neighbors[y].append(x)
        curr, prev = [x for x in neighbors if len(neighbors[x]) == 1][0], None         #The numbers on both side should only have one neighbor, we can start from either of them. Also initialize prev number as none.
        result = []
        while True:                                                                    #Start iteration.
            result.append(curr)                                                        #Append current number to result.
            next = [x for x in neighbors[curr] if x != prev]                           #Find the other neighbor of curr.
            if not next:                                                               #If it does not exist, we reach the end so break.
                break
            curr, prev = next[0], curr                                                 #Replace curr with next[0] and replace prev with curr to go to next number.
        return result
