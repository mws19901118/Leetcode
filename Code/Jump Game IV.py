class Solution:
    def minJumps(self, arr: List[int]) -> int:
        indexes = defaultdict(list)
        i = 0
        while i < len(arr):                                             #Find the indexes in arr of each number.
            j = i + 1
            while j < len(arr) and arr[j] == arr[i]:
                j += 1
            indexes[arr[i]].append(i)
            if j - i >= 2:                                              #For a number that appears at least 2 consecutive times in arr, we only need the start and end index.
                indexes[arr[i]].append(j - 1)
            i = j

        steps = 0                                                       #Count steps.
        q = [0]
        visited = {0}
        while q:                                                        #BFS.
            newq = []
            for x in q:
                if x == len(arr) - 1:                                   #If reach the end, return steps.
                    return steps
                for y in indexes[arr[x]]:                               #Iterate over indexes with same value of arr[x].
                    if y not in visited:                                #If it's not visited, add it to newq and visited.
                        newq.append(y)
                        visited.add(y)
                indexes[arr[x]].clear()                                 #All indexes in indexes[arr[x]] are visited. Clear indexes[arr[x]] to avoid duplicate visit.
                for y in [x - 1, x + 1]:                                #Visit the adjacent indexes if they are valid and not visited. 
                    if 0 <= y < len(arr) and y not in visited:
                        newq.append(y)
                        visited.add(y)
            steps += 1                                                  #Increase steps.
            q = newq                                                    #Replace q with newq.
