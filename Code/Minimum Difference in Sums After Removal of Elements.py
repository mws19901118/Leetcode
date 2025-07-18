class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3                                                            #Calculate n.
        min_sum, max_heap = [0] * 3 * n, []                                           #Initialize the min sum of n elements from front at each index, also initialize a max heap.
        max_sum, min_heap = [0] * 3 * n, []                                           #Initialize the max sum of n elements from back at each index, also initialize a min heap.
        s_front, s_back = 0, 0                                                        #Initialize the min sum of n elements from front and max sum of n elements from back.
        for i in range(2 * n):                                                        #Traverse from 0 to 2 * n - 1; we don't need calculate beyond 2 * n - 1 because we have to reserve at least n elements for the opposite side.
            s_front += nums[i]                                                        #Add nums[i] to s_front.
            heapq.heappush(max_heap, -nums[i])                                        #Push nums[i] to the max heap.
            if len(max_heap) > n:                                                     #If there are more than n elements in the max heap, pop the max heap and reduce that element from s_front.
                s_front += heapq.heappop(max_heap)
            if i >= n - 1:                                                            #If i >= n - 1, update min_sum[i].
                min_sum[i] = s_front
            s_back += nums[-(i + 1)]                                                  #Add nums[-(i + 1)] to s_back.
            heapq.heappush(min_heap, nums[-(i + 1)])                                  #Push nums[-(i + 1)] to the min heap.
            if len(min_heap) > n:                                                     #If there are more than n elements in the min heap, pop the min heap and reduce that element from s_back.
                s_back -= heapq.heappop(min_heap)
            if i >= n - 1:                                                            #If i >= n - 1, update max_sum[-(i + 1)].
                max_sum[-(i + 1)] = s_back
        return min(min_sum[i] - max_sum[i + 1] for i in range(n - 1, 2 * n))          #For the n indexes in the middle(n - 1 <= i <= 2 * n - 1), calculate the min value of min_sum[i] - max_sum[i + 1].
