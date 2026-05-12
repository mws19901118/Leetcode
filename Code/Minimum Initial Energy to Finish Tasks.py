class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[1] - x[0])      #Sort the tasks by the diff of mininum - actual.
        result = 0
        for x in tasks:                              #Traverse tasks.
            result = max(result + x[0], x[1])        #Add current actual to result and compare with current minimum; update result with the larger value.
        return result
