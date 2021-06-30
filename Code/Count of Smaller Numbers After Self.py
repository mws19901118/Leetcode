class BinaryIndexedTree:
    def __init__(self, n: int):                                                             #Initialize a binary indexed tree of size n.
        self.size = n + 1
        self.tree = [0] * self.size
        
    def add(self, index: int, value: int) -> None:                                          #Add given value to the number at given index.
        i = index + 1
        while i < self.size: 
            self.tree[i] += value
            i += i & -i
            
    def query(self, start: int, end: int) -> int:                                           #Return sum of all numbers in from start to end(inclusive).
        if start == 0:
            i = end + 1
            result = 0
            while i:
                result += self.tree[i]
                i -= i & - i
            return result
        else:
            return self.query(0, end) - self.query(0, start - 1)
        
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        indexes = {n: i for i, n in enumerate(sorted(list(set(nums))))}                     #Dedupe nums, next sort, then generate the map from value to index.
        tree = BinaryIndexedTree(len(indexes))                                              #Initialize binary indexed tree, storing the occurrence of the number at each index so far.
        result = []                                                                         #Initialize result.
        for i, x in enumerate(reversed(nums)):                                              #Traverse nums backwards.
            index = indexes[x]                                                              #Find the index of x in sorted du-duped nunms.
            result.append(tree.query(0, index - 1))                                         #Get current sum of all recorded indices in binary indexed tree from 0 to index - 1, the corresponding number is all smaller than x.
            tree.add(index, 1)                                                              #Add 1 to the value at index in binary indexed tree.
        return result[::-1]
