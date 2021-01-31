class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        for i in range(len(nums)):                        #Even element can divide until it's odd; odd element can only double once to even.
            if nums[i] & 1:                               #So, double all even elements in nums, so from now on all the operations are divide.
                nums[i] <<= 1
            nums[i] = -nums[i]                            #Make element negative to maintain a max heap.
        minV = max(nums)                                  #Get the min value(in negative).
        heapq.heapify(nums)                               #Heapify nums.
        deviation = minV - nums[0]                        #Get the initial deviation.
        while not -nums[0] & 1:                           #Iterate while the max value(heap top) is even. If it's odd, we cannot further divide the max value, thus we cannot decrease deviation.
            maxV = heapq.heappop(nums)                    #Pop heap top.
            heapq.heappush(nums, maxV // 2)               #Divide max value and push to heap.
            minV = max(maxV // 2, minV)                   #Update min value.
            deviation = min(deviation, minV - nums[0])    #Update min deviation.
        return deviation
