class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        buildings = [0] * n                                                      #Store net change of each building.
        def backtracking(i: int) -> int:                                         #Backtracking.
            if i == len(requests):                                               #If reaches the end of requests, return 0 if all buildings net change is 0; otherwise return -len(requests) meaning it's not valid.
                return 0 if all(x == 0 for x in buildings) else -len(requests)
            result = backtracking(i + 1)                                         #Keep backtracking without current request.
            buildings[requests[i][0]] -= 1                                       #Takeing current request and update buildings.
            buildings[requests[i][1]] += 1
            result = max(result, 1 + backtracking(i + 1))                        #Keep backtracking with current request and update result if necessary.
            buildings[requests[i][0]] += 1                                       #Restore buildings.
            buildings[requests[i][1]] -= 1
            return result

        return backtracking(0)                                                   #Start backtracking from 0 and return.
