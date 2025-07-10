class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        startTime, endTime = startTime + [eventTime], [0] + endTime        #Add eventTime to the end of startTime and 0 to the start of endTime.
        gaps = [s - e for s, e in zip(startTime, endTime)]                 #Calculate the gaps of each adjacent meetings, including the gap before first meeting and gap after last meeting.
        q = deque()                                                        #Store the consective gap in a queue.
        result, s = 0, 0                                                   #Intialize result and sum.
        for x in gaps:                                                     #Traverse gaps.
            s += x                                                         #Add x to s.
            q.append(x)                                                    #Append x to q.
            if len(q) > k + 1:                                             #If the length of q is greater than k + 1, pop left queue and deduct the popped number from s.
                s -= q.popleft()
            result = max(result, s)                                        #We can move the meetings to make a free time of length s, then update result if necessary.
        return result
