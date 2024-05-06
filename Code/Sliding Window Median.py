class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def getMean() -> float:                                                                                              #Get the median from low half max heap and high half min heap, ge tthe median.
            return -low[0] if k & 1 else (-low[0] + high[0]) / 2                                                             #If k is odd, return top of max heap; otherwise, return the average of 2 heap top.

        def insert(x: int) -> int:                                                                                           #Insert a new number and return its contribution to balance factor.
            if x <= -low[0]:                                                                                                 #If x is not greater than top of max heap, push it to max heap and return 1.
                heapq.heappush(low, -x)
                return 1
            else:                                                                                                            #Otherwise, push it to min heap and return -1.
                heapq.heappush(high, x)
                return -1

        def reBalance(balanceFactor: int) -> None:                                                                           #Rebalance 2 heaps.
            if balanceFactor < 0:                                                                                            #If balance factor is smaller than 0, max heap needs more number, so pop top of min heap and push it to max heap.
                heapq.heappush(low, -heapq.heappop(high))
            elif balanceFactor > 0:                                                                                          #Otherwise, min heap needs more number, so pop top of max heap and push it to min heap.
                heapq.heappush(high, -heapq.heappop(low))

        def pop() -> None:                                                                                                   #Pop items from heaps if items are already moved out of sliding window.
            while low and toBeRemoved[-low[0]]:                                                                              #While top of max heap is removed, pop it from max heap and decrease its count in toBeRemoved.
                toBeRemoved[-heapq.heappop(low)] -= 1
            while high and toBeRemoved[high[0]]:                                                                             #While top of min heap is removed, pop it from min heap and decrease its count in toBeRemoved.
                toBeRemoved[heapq.heappop(high)] -= 1

        initialWindow = sorted(nums[:k])                                                                                     #Initialize sliding window with first k numbers in nums.
        low, high = initialWindow[:(len(initialWindow) + 1) // 2], initialWindow[(len(initialWindow) + 1) // 2:]             #Divide them into 2 parts, a max heap for low half and a min heap for high half.
        low = [-x for x in low]
        heapq.heapify(low)
        heapq.heapify(high)
        result = [getMean()]                                                                                                 #Initialize result with current median.
        toBeRemoved = Counter()                                                                                              #Count the numbers to be removed from sliding window.
        for i in range(k, len(nums)):                                                                                        #Traverse the rest of nums and at the start of each iteration, the 2 heaps are balanced.
            balanceFactor = -1 if nums[i - k] <= -low[0] else 1                                                              #If the number to be removed is smaller than top of max heap, balance factor is -1 as we have to move it out of max heap; otherwise balance factor is 1.
            toBeRemoved[nums[i - k]] += 1                                                                                    #Increase the count of to be removed number.
            balanceFactor += insert(nums[i])                                                                                 #Insert new number.
            reBalance(balanceFactor)                                                                                         #Rebalance the heaps.
            pop()                                                                                                            #Pop to be removed numbers.
            result.append(getMean())                                                                                         #Append current median to result.
        return result
