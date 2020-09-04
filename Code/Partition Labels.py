class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lastIndex = {x: i for i, x in enumerate(S)}         #Store the last index of each letter.
        result = []
        i, previousEnd = 0, -1                              #Initially, the end of previous partition is -1.
        while i < len(S):                                   #Traverse through S.
            end = i                                         #For a new partition, initially, the end is also start,
            while i <= end:                                 #Traverse through current partition.
                end = max(end, lastIndex[S[i]])             #Dynamically update end with the largest last index of letters in the partition.
                i += 1
            result.append(end - previousEnd)                #Add partition length to result after traversing through current partition.
            previousEnd = end                               #Update the end of previous partition.
        return result
