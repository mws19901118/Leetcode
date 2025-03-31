class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        indexes = defaultdict(list)                             #Store the indexes of each letter in source.
        for i, x in enumerate(source):
            indexes[x].append(i)
        count, prevIndex = 0, -1                                #Initialize the count and prev index in source.
        for x in target:                                        #Traverse target.
            if x not in indexes:                                #Return -1 if x not in indexes, meaning x not in source as well.
                return -1
            index = bisect_right(indexes[x], prevIndex)         #Find the first index of x which is greater than prevIndex.
            if index == len(indexes[x]):                        #If not found, increase count and set prevIndex to first index of x.
                count += 1
                prevIndex = indexes[x][0]
            else:                                               #Otherwise, just update prevIndex to the found index.
                prevIndex = indexes[x][index]
        return count + 1                                        #Return count + 1.
