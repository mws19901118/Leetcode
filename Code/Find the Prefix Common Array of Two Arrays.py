class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result, count = [], 0          #Initialize result and count of prefix common number.
        frequency = Counter()          #Store the frequency of each number. 
        for x, y in zip(A, B):         #Traverse A and B simultaneously.
            frequency[x] += 1          #Increase the frequency of x.
            if frequency[x] == 2:      #If the frequency reaches 2, increase count.
                count += 1
            frequency[y] += 1          #Increase the frequency of y.
            if frequency[y] == 2:      #If the frequency reaches 2, increase count.
                count += 1
            result.append(count)       #Append count to result.
        return result
