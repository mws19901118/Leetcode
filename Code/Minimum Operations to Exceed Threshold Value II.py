class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0
        heapq.heapify(nums)                                      #Convert nums to a min heap.
        while len(nums) >= 2 and nums[0] < k:                    #Iterate while there are at aleast 2 elements in heap and the heap top is smaller than k.
            x = heapq.heappop(nums)                              #Pop heap.
            y = heapq.heappop(nums)                              #Pop heap.
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))      #Push min(x, y) * 2 + max(x, y) back to heap.
            result += 1                                          #Increase result.
        return result
