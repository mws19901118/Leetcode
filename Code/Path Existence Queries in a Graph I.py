class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        label = 0                                                          #Label each group.
        group = defaultdict(int)                                           #Store the group of each node.
        i = 0
        while i < len(nums):                                               #Traverse nums with 2 pointers.
            group[i] = label                                               #Assign the label to current node.
            j = i + 1
            while j < len(nums) and nums[j] - nums[j - 1] <= maxDiff:      #Traverse forward while the diff between nodes are not greater than maxDiff.
                group[j] = label                                           #Assign the label to j as well.
                j += 1
            label += 1
            i = j
        return [group[x] == group[y] for x, y in queries]                  #For each query, return if the 2 nodes are in the same group.
