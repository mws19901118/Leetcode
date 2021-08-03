class Solution:
    def DFS(self, c: dict, k: List[int]):                               #DFS.
        if not k:                                                       #If not k, return a list containing one empty list.
            return [[]]
        result = []                                                     #Initialize result of current level.
        r = self.DFS(c, k[1:])                                          #DFS k[1:].
        t = []                                                          #Initialzie a list containing differrent count of k[0].
        for i in range(c[k[0]] + 1):                                    #Iterate c[k[0]] + 1 times.
            if i > 0:                                                   #If i > 0, append k[0] to t.
                t.append(k[0])
            for x in r:                                                 #For each list in r.
                result.append(t + x)                                    #Append t + x to result.
        return result                                                   #Return result.
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)                                               #Count each number in nums.
        return self.DFS(c, sorted(list(d.keys())))                      #Return the result from DFS with the count of each number and sorted de-duped number list..
