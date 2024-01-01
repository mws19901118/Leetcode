class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()                                    #Sort g in ascending order.
        s.sort()                                    #Sort s in ascending order.
        i, j, count = 0, 0, 0                       #Initialize pointer in s, pointer in g and content children count.
        while i < len(s) and j < len(g):            #Traverse while i and j is valid.
            while i < len(s) and s[i] < g[j]:       #While i is valid and s[i] < g[j], increase i.
                i += 1
            count += int(i < len(s))                #Increase count if i is still valid.
            i += 1                                  #Assign current cookie to current child, then increase i and j.
            j += 1
        return count
