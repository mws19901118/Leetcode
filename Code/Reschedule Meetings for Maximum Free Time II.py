class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        meetings = [e - s for s, e in zip(startTime, endTime)]                                                #Calculate meetings.
        can_be_moved = [False] * len(meetings)                                                                #Indicate if a meeting can be moved to a non-adjacent gap.
        startTime, endTime = startTime + [eventTime], [0] + endTime                                           #Add eventTime to the end of startTime and 0 to the start of endTime.
        gaps = [s - e for s, e in zip(startTime, endTime)]                                                    #Calculate the gaps of each adjacent meetings, including the gap before first meeting and gap after last meeting.
        left_max_gap, right_max_gap = 0, 0                                                                    #Initialize the max gap from left and from right respectively,
        for i in range(len(meetings)):                                                                        #Traverse meetings in both directions.
            if meetings[i] <= left_max_gap:                                                                   #If the current meeting in forward traverse is not greater than max gap from left, if can be moved into the gap that is non-adjacent.
                can_be_moved[i] = True
            left_max_gap = max(left_max_gap, gaps[i])                                                         #Update the max gap from left.
            if meetings[-(i + 1)] <= right_max_gap:                                                           #If the current meeting in backward traverse is not greater than max gap from right, if can be moved into the gap that is non-adjacent.
                can_be_moved[-(i + 1)] = True
            right_max_gap = max(right_max_gap, gaps[len(meetings) - i])                                       #Update the max gap from right.
        return max(gaps[i] + gaps[i + 1] + x * int(can_be_moved[i]) for i, x in enumerate(meetings))          #If a meeting can be moved to a non-adjacent gap, then we can create a free time with the meeting and adjacent gaps; otherwise, we can only create a free time with adjacent gaps. Thus, return the max free time following this rule.
