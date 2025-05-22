class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()                                                #Sort queries.
        heap = []                                                     #Use a max heap to store the right end of queries that impact current index.
        diff = [0] * (len(nums) + 1)                                  #Store the overall diff at each index. 
        index, s = 0, 0                                               #Initialize index to traverse queries and s as the max value we can decrease at current index.
        for i, x in enumerate(nums):                                  #Traverse nums.
            s += diff[i]                                              #Apply the diff at i.
            while index < len(queries) and queries[index][0] == i:    #While index hasn't reach the end and the current query starts at i, push the right end to heap and move to next index.
                heappush(heap, -queries[index][1])
                index += 1
            while s < x and heap and -heap[0] >= i:                   #While we cannot decrease x to 0 and heap is not empty and the top of heap is greater than or equal to i, increase s.
                s += 1
                diff[-heappop(heap) + 1] -= 1                         #Also pop heap and update the ending effect on diff of the popped query, because we will use this query.
            if s < x:                                                 #If we still cannot decrease x to 0, it is not possible to convert nums to a zero array, so return -1.
                return -1
        return len(heap)                                              #Return the length of heap, which is the count of unnecessary queries.
