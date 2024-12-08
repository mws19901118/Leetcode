class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()                                                  #Sort events by startTime in asending order.
        max_values = [0] * (len(events) + 1)                           #Initialize the max values of events[i:] for each index i in events.
        for i in reversed(range(len(events))):                         #Traverse events from backwards.
            max_values[i] = max(events[i][2], max_values[i + 1])       #Update max_values[i] to be the max value of events[i] and max_values[i + 1].
        result = 0                                                     #Initialize result.
        for i, (s, e, v) in enumerate(events):                         #Traverse events.
            index = bisect_left(events, [e + 1, -1, -1], lo = i + 1)   #Binary search in events[i + 1:] to find the leftmost index to insert [e + 1, -1, -1].
            result = max(result, v + max_values[index])                #The max value of taking current event is the value of current event plus max_values[index]; also update result if necessary.
        return result
