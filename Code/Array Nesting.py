class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)         #Initialize visited array.
        result = 0                            #Because nums is a permutation of the numbers in the range [0, n - 1], no 2 indexes pointing to same value. So, elements in nums can be divided to a number of cycles with no intersections.
        for i in range(len(nums)):            #Traverse from 0 to len(nums) - 1.
            count = 0                         #Count the length in current set.
            node = i                          #Start node is i.
            while not visited[node]:          #While node is unvisited, keep DFS.
                count += 1                    #Increase count.
                visited[node] = True          #Mark current node as visited.
                node = nums[node]             #Update node to nums[node].
            result = max(result, count)       #Update result.
        return result
