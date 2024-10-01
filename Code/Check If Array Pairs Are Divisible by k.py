class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        groups = defaultdict(list)                        #For each number x, put it in to the gourp x % k.
        for x in arr:
            groups[x % k].append(x)
        for x in groups:                                  #Traverse each group.
            if not x or (not k & 1 and x == k // 2):      #If x is 0 or exactly k // 2(if k is even), the group size must be even.
                if len(groups[x]) & 1:
                    return False
            elif len(groups[x]) != len(groups[k - x]):    #Otherwise, the group size of x must be same as group size of k - x.
                return False
        return True                                       #Return true at the end.
