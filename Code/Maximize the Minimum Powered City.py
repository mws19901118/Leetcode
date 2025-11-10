class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        prefixSum = [0]                                                                                                    #Populate prefix sum.
        for x in stations:
            prefixSum.append(prefixSum[-1] + x)
        power = [prefixSum[min(len(stations), i + r + 1)] - prefixSum[max(0, i - r)] for i in range(len(stations))]        #The power at each city is sum(stations[max(0, i - r):min(len(stations), i + r + 1)]

        @cache                                                                                                             #Cache result.
        def check(minPower: int) -> bool:                                                                                  #Check if we can fufil the given min power.
            delta, remain = 0, k                                                                                           #Initialize the power delta by new stations, and remain stations to built.
            dq = deque()                                                                                                   #Store the end reach index of built stations along with the count in a queue.
            for i, x in enumerate(power):                                                                                  #Traverse power.
                while dq and dq[0][0] < i:                                                                                 #While the queue is not empty and i is greater than the end reach index of the head of the queue, deduct count of the head of the queue from delta and pop queue. 
                    delta -= dq[0][1]
                    dq.popleft()
                if x + delta >= minPower:                                                                                  #If current power plus delta is greater than or equal to min power, we don't need to do anything.
                    continue
                gap = minPower - x - delta                                                                                 #Calculate the gap to make min power.
                if gap > remain:                                                                                           #If not enough stations to build to fill the gap, return false.
                    return False
                remain -= gap                                                                                              #Decrease gap from remain.
                delta += gap                                                                                               #Increase gap to delta.
                dq.append((i + 2 * r, gap))                                                                                #Append (i + 2 * r, gap) to queue.
            return True                                                                                                    #Return true at the end.

        start, end = min(power), max(power) + k                                                                            #Binary search from min(power) to max(power) + k.
        while start <= end:
            mid = (start + end) // 2
            if check(mid) and not check(mid + 1):                                                                          #If can build stations optimally to make mid the min power but not mid + 1, return mid.
                return mid
            elif not check(mid):                                                                                           #If cannot make mid the min power, set end to mid - 1.
                end = mid - 1
            else:                                                                                                          #Otherwise, set start to mid + 1.
                start = mid + 1
