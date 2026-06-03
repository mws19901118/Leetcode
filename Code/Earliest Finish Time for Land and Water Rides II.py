class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:                          #Same as Earliest Finish Time for Land and Water Rides I.py
        def finishTime(start1: List[int], duration1: List[int], start2: List[int], duration2: List[int]) -> int:
            first = min(s + d for s, d in zip(start1, duration1))
            return min(max(s, first) + d for s, d in zip(start2, duration2))

        return min(finishTime(landStartTime, landDuration, waterStartTime, waterDuration), finishTime(waterStartTime, waterDuration, landStartTime, landDuration))
