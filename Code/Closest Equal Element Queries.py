class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        indexes = defaultdict(list)                                                                                      #Store the indexes of each number.
        for i, x in enumerate(nums):
            indexes[x].append(i)
        result = []                                                                                                      #Initialize result.
        for x in queries:                                                                                                #Traverse queries.
            if len(indexes[nums[x]]) == 1:                                                                               #If nums[x] only appears once in nums, append -1 to result and continue.
                result.append(-1)
                continue
            i = bisect_left(indexes[nums[x]], x)                                                                         #Binary search the index of x in the indexes of nums[x].
            left = indexes[nums[x]][i - 1] if i - 1 >= 0 else indexes[nums[x]][-1] - len(nums)                           #Find the neareset left index in the circular array.
            right = indexes[nums[x]][i + 1] if i + 1 < len(indexes[nums[x]]) else indexes[nums[x]][0] + len(nums)        #Find the neareset right index in the circular array.
            result.append(min(x - left, right - x))                                                                      #Append the min distance from x to the nearest left index or nearest right index.
        return result
