class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(x, i) for i, x in enumerate(nums)]    #Put all number and its index in a max heap.
        heapq.heapify(heap)
        for _ in range(k):                             #Iterate k times.
            _, i = heapq.heappop(heap)                 #Pop the top of heap.
            nums[i] *= multiplier                      #Multiply the multiplier for nums[i].
            heapq.heappush(heap, (nums[i], i))         #Push back nums[i[ and i to heap.
        return nums                                    #Return nums.
