class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(list(set(arr2)))                                        #Dedupe arr2 and sort in ascending order.
        
        @cache                                                                #Cache result.
        def DFS(i: int, prev: int) -> int:                                    #DFS to find the minimum number of moves to make arr1[:i] strictly increasing with arr1[i - 1](if exist) is prev.
            if i == len(arr1):                                                #If i reaches the end of arr1, return 0.
                return 0
            cost = float('inf')                                               #Initialize cost at positive infinite.
            if arr1[i] > prev:                                                #If arr1[i] is already greater than prev, we can just skip it. 
                cost = DFS(i + 1, arr1[i])
            index = bisect_right(arr2, prev)                                  #Find smallest value in arr2 that is greater than prev so it can replace arr1[i].
            if index < len(arr2):                                             #If such number exist, we can replace arr1[i], even if arr1[i] is already greater than prev to make further replacement easier.
                cost = min(cost, 1 + DFS(i + 1, arr2[index]))
            return cost                                                       #Return cost.
                
        return DFS(0, -1) if DFS(0, -1) < float('inf') else -1                #Return DFS(0, -1) if the result is not positive infinite; otherwise return -1 because cannot make arr1 strictly increasing.
