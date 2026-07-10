class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sortedNums = sorted(enumerate(nums), key = lambda x: x[1])                          #Sort nums and keep its original index.
        newIndex = [0] * n                                                                  #Store and populate the new index of each original index.
        for i, (x, _) in enumerate(sortedNums):
            newIndex[x] = i

        m = ceil(log2(n)) + 1                                                               #Calculate the max power of 2 to reach n.
        reach = [[0] * m for _ in range(n)]                                                 #Initialize the reach array for each node; reach[i][j] means the max index can reach to the right from i after 2 ** j steps. 
        j = 0                                                                               #Initialize pointer j.
        for i in range(n):                                                                  #Traverse n.
            while j < n and sortedNums[j][1] - sortedNums[i][1] <= maxDiff:                 #While j is valid and can reach j from i, move forward j/ 
                j += 1
            reach[i][0] = j - 1                                                             #The direct(2 ** 0 steo) reach from i is j - 1/

        for j in range(1, m):                                                               #Traverse from 1 to m - 1.
            for i in range(n):                                                              #Traverse from 1 to n.
                reach[i][j] = reach[reach[i][j - 1]][j - 1]                                 #If i can reach reach[i][j - 1] in 2 ** (j - 1) steps and reach[i][j - 1] can reach reach[reach[i][j - 1]][j - 1] in 2 ** (j - 1) steps; then i can reach reach[reach[i][j - 1]][j - 1] in 2 ** j steps.

        result = []
        for u, v in queries:                                                                #Traverse queries.
            x, y = min(newIndex[u], newIndex[v]), max(newIndex[u], newIndex[v])             #Get the min new index(x) and max new index(y).
            if x == y:                                                                      #If they are already the same, just append 0 to result then continue.
                result.append(0)
                continue
            curr, steps = x, 0                                                              #Initialize current index and total steps.
            for j in reversed(range(m)):                                                    #Traverse from m - 1 to 0 like traversing left to right on a binary number.
                if reach[curr][j] < y:                                                      #If reach[curr][j] < y, move curr to reach[curr][j] and add 2 ** j to steps.
                    curr = reach[curr][j]
                    steps += (1 << j)
            result.append(steps + 1 if reach[curr][0] >= y else -1)                         #If one more step can reach y, append steps + 1 to result; otherwise, append -1 to result.
        return result
