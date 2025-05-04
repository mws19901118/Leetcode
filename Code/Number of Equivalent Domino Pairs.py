class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = Counter(tuple(x) for x in dominoes)              #Count each type of dominioes.
        intra, inter = 0, 0                                      #Initialize count for intra(equivalant paris with in same type) and inter(equivalent pairs between types).
        for x, y in count.keys():                                #Traverse the type of dominoes.
            intra += count[(x, y)] * (count[(x, y)] - 1) // 2    #There are count[(x, y)] * (count[(x, y)] - 1) // 2 intra pairs for current domino.
            if (x, y) != (y, x):                                 #If current domino is not a pair of same numbers, add count[(x, y)] * count[(y, x)] to inter.
                inter += count[(x, y)] * count[(y, x)]
        return intra + inter // 2                                #Return intra + inter // 2 because inter pairs are counted twice.
