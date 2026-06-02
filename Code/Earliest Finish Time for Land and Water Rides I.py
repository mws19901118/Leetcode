class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def finishTime(start1: List[int], duration1: List[int], start2: List[int], duration2: List[int]) -> int:                                                            #Calculate finish time, either land ride first then water ride or water ride then land ride.
            earliest = min(s + d for s, d in zip(start1, duration1))                                                                                                        #Traverse start1 and duration1 to calculate the earliest time to finish the first ride.
            return min(max(s, earliest) + d for s, d in zip(start2, duration2))                                                                                             #Traverse start2 and durations to calculate the earliest time to finish the second ride, replace original start time to first ride finish time if it is larger.

        return min(finishTime(landStartTime, landDuration, waterStartTime, waterDuration), finishTime(waterStartTime, waterDuration, landStartTime, landDuration))          #Return the min value of either land ride first then water ride or water ride then land ride.
