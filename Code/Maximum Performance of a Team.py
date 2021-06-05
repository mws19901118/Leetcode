class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pairs = sorted(zip(efficiency, speed), reverse = True)        #Put the speed and effiiency of each engineer in a tuple, and sort them by efficiency in descending order.
        heap, speedSum, performance = [], 0, 0                        #Initialize a min heap for top k largest speed, sum of top k speed and max performance.
        for e, s in pairs:                                            #Traverse efficiency and speed pairs.
            if len(heap) == k:                                        #If heap size is already k, pop heap and update speedSum.
                speedSum -= heapq.heappop(heap)
            heapq.heappush(heap, s)                                   #Push speed to heap.
            speedSum += s                                             #Update speedSum.
            performance = max(performance, speedSum * e)              #Update performance. Because efficiency is sorted descendingly, it goes smaller while traversing, we have to keep sum of speed as large as possible to get a potential max performance.
        return performance % (10 ** 9 + 7)                            #Return the modulo.
