class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjacentList = defaultdict(list)                                                                        #Build adjacent list.
        for x in range(n):
            if manager[x] != -1:
                adjacentList[manager[x]].append(x)

        def dfs(x: int) -> int:                                                                                 #DFS to calculate the total time needed to inform x and all subordinates.
            return 0 if not adjacentList[x] else informTime[x] + max([dfs(y) for y in adjacentList[x]])         #Return 0 if x has no subordinates; otherwise, return the max of DFS result of each subordinate plus informTime[x].
        
        return dfs(headID)                                                                                      #Return the dfs result from headID.
