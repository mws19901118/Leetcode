class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1, map2 = {}, {}                                                                                                 #Map characters in s to t and characters in t to s.
        for x, y in zip(s, t):                                                                                              #Traverse s and t simultaneously.
            if x not in map1 and y not in map2:                                                                             #If both x and y is not mapped, map x to y and y to x.
                map1[x], map2[y] = y, x
            elif (x not in map1 and y in map2) or (x in map1 and y not in map2) or y != map1[x] or x != map2[y]:            #If one is mapped but the other is not or x and y are not mapped to each other, s and t are not isomorphic strings, return false.
                return False
        return True                                                                                                         #Return true.
