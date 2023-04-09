class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        capacity = float('inf')                                                                       #Initialize the wast to be infinite.
        packages.sort()                                                                               #Sort packages.
        for x in boxes:                                                                               #Traverse boxes.
            x.sort()                                                                                  #Sort boxes of current provider.
            if x[-1] < packages[-1]:                                                                  #If the largest box is smaller than largest package, cannot fit packges in current box provider, continue.
                continue
            count, i = 0, 0                                                                           #Initialize the count of capacity used and the index of lower bound of binary search in packages.
            for y in x:                                                                               #Traverse each box.
                j = bisect_right(packages, y, i)                                                      #Binary search the right most place to insert y in packages.
                count += y * (j - i)                                                                  #All packages in packages[i + 1:j + 1] can fit into y, add the capacity used to count. 
                i = j                                                                                 #Replace i with j.
            capacity = min(capacity, count)                                                           #Update total capacity used.
        return -1 if capacity == float('inf') else (capacity - sum(packages)) % (10 ** 9 + 7)         #If capacity is still infinite, return -1 as no boxes provider can fit all packages; otherwise, return waste = capacity - sum(packages), then take the modulo by 10 ** 9 + 7.
